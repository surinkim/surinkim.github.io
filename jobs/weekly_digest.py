#!/usr/bin/env python3
"""주간 테크/개발 뉴스 링크 모음 자동 큐레이션 도구.

RSS 피드를 수집하고, 정규화/중복제거/품질필터/분류를 거쳐
Jekyll 블로그용 Markdown 초안을 생성한다.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import logging
import os
import re
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass, asdict
from datetime import datetime, date, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

import feedparser
import httpx
import yaml
from dateutil import parser as dateutil_parser
from jinja2 import Environment, FileSystemLoader
from rapidfuzz import fuzz

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)
TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid",
}
AD_KEYWORDS = {"sponsored", "promo", "광고", "제휴", "advertisement"}
CATEGORY_PRIORITY = ["AI", "Backend", "InfraCloud", "Tools"]
SECTION_ORDER = ["AI", "Backend", "Infra/Cloud", "Tools", "Etc"]
CATEGORY_DISPLAY = {"InfraCloud": "Infra/Cloud"}

logger = logging.getLogger("weekly_digest")


def _strip_html(text: str) -> str:
    """HTML 태그를 제거하고 엔티티를 디코딩한다."""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


_JUNK_SUMMARY_PATTERNS = re.compile(
    r"^(comments|댓글|read more\.?|continue reading\.?|\.{3,})$",
    re.IGNORECASE,
)
_REDDIT_BOILERPLATE = re.compile(
    r"\s*submitted by\s+/u/\S+\s*\[link\]\s*\[(?:comments|댓글)\]\s*$",
    re.IGNORECASE,
)


def _clean_summary(text: str) -> str:
    """의미 없는 요약(예: 'Comments')을 빈 문자열로, Reddit 보일러플레이트를 제거한다."""
    text = _REDDIT_BOILERPLATE.sub("", text).strip()
    if _JUNK_SUMMARY_PATTERNS.match(text):
        return ""
    return text


def _is_probably_english(text: str) -> bool:
    """영문 본문 비중이 높고 한글이 거의 없으면 True."""
    if not text:
        return False
    has_hangul = bool(re.search(r"[가-힣]", text))
    if has_hangul:
        return False
    alpha = sum(1 for ch in text if ch.isalpha())
    ascii_alpha = sum(1 for ch in text if "a" <= ch.lower() <= "z")
    if alpha == 0:
        return False
    return (ascii_alpha / alpha) >= 0.8


def _compress_summary(text: str, max_sentences: int, max_chars: int) -> str:
    """요약을 1~2문장/길이 제한으로 압축하고, 초과 시 말줄임표를 붙인다."""
    cleaned = _strip_html(text or "")
    if not cleaned:
        return ""

    # 한국어/영어/일반 문장부호 기준으로 문장 경계 분리
    sentences = re.split(r"(?<=[.!?。！？])\s+", cleaned)
    sentences = [s.strip() for s in sentences if s.strip()]
    if sentences:
        cleaned = " ".join(sentences[:max(1, max_sentences)])

    if len(cleaned) > max_chars:
        cut = cleaned[:max_chars]
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        cleaned = cut.rstrip(" ,.;:/") + "..."
    return cleaned


class GoogleTranslator:
    """Google Translate (무료)를 이용해 영문 요약을 한글로 번역한다."""

    def __init__(self):
        from deep_translator import GoogleTranslator as _GT
        self._gt = _GT(source="en", target="ko")
        self._cache: dict[str, str] = {}

    def translate_to_korean(self, text: str) -> str:
        if not text:
            return text
        if text in self._cache:
            return self._cache[text]
        try:
            out = self._gt.translate(text)
            if out:
                self._cache[text] = out
                return out
        except Exception as exc:
            logger.warning("Google translation failed, fallback to original: %s", exc)
        self._cache[text] = text
        return text


class OpenAITranslator:
    """OPENAI API를 이용해 영문 요약을 한글로 번역한다 (선택 기능)."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self._cache: dict[str, str] = {}
        self._client = httpx.Client(timeout=20)

    def translate_to_korean(self, text: str) -> str:
        if not text:
            return text
        if text in self._cache:
            return self._cache[text]

        body = {
            "model": self.model,
            "input": [
                {
                    "role": "system",
                    "content": (
                        "You are a technical translator. Translate English to Korean. "
                        "Keep 1-2 sentences, preserve proper nouns and technical terms. "
                        "Output only Korean translation."
                    ),
                },
                {"role": "user", "content": text},
            ],
        }

        try:
            resp = self._client.post(
                "https://api.openai.com/v1/responses",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json=body,
            )
            resp.raise_for_status()
            data = resp.json()
            out = (data.get("output_text") or "").strip()
            if out:
                self._cache[text] = out
                return out
        except Exception as exc:
            logger.warning("Summary translation failed, fallback to original: %s", exc)
        self._cache[text] = text
        return text


def postprocess_summaries(
    items: list[NormalizedItem],
    max_sentences: int,
    max_chars: int,
    translate_en_to_ko: bool = False,
    translator: GoogleTranslator | OpenAITranslator | None = None,
) -> list[NormalizedItem]:
    """선택된 항목의 요약을 번역(옵션) + 길이 제한 처리."""
    for item in items:
        summary = item.summary or ""
        if translate_en_to_ko and translator and _is_probably_english(summary):
            summary = translator.translate_to_korean(summary)
        item.summary = _compress_summary(summary, max_sentences, max_chars)
    return items


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------
@dataclass
class RawItem:
    source_id: str
    source_name: str
    title: str
    url: str
    published_at: str
    summary: str
    fetched_at: str


@dataclass
class NormalizedItem:
    id: str
    source_id: str
    title: str
    url: str
    domain: str
    published_date: str
    source_name: str
    summary: str
    category: str = "Etc"
    score: float = 0.0


# ---------------------------------------------------------------------------
# Loading helpers
# ---------------------------------------------------------------------------
def load_sources(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return [s for s in data.get("sources", []) if s.get("enabled", False)]


def load_category_rules(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Collection
# ---------------------------------------------------------------------------
def _http_get(
    url: str,
    timeout: int = 10,
    retries: int = 2,
    extra_headers: dict | None = None,
    use_curl_fallback: bool = False,
) -> str | None:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, text/xml;q=0.9, */*;q=0.8",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    if extra_headers:
        headers.update(extra_headers)

    got_forbidden = False
    for attempt in range(1, retries + 2):
        try:
            with httpx.Client(follow_redirects=True, timeout=timeout) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()
                return resp.text
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code if exc.response is not None else None
            logger.debug(
                "Attempt %d for %s failed with status %s",
                attempt, url, status,
            )
            # 권한/정책 차단은 재시도해도 동일한 경우가 많아 즉시 중단
            if status in (401, 403, 404):
                if status == 403:
                    got_forbidden = True
                break
            if attempt <= retries:
                time.sleep(2)
        except Exception as exc:
            logger.debug("Attempt %d for %s failed: %s", attempt, url, exc)
            if attempt <= retries:
                time.sleep(2)

    if use_curl_fallback:
        curl_cmd = [
            "curl", "-fsSL", "-L", "--max-time", str(timeout), url,
            "-H", f"User-Agent: {headers.get('User-Agent', USER_AGENT)}",
            "-H", f"Accept: {headers.get('Accept', '*/*')}",
            "-H", f"Accept-Language: {headers.get('Accept-Language', 'en-US,en;q=0.9')}",
        ]
        for key, value in headers.items():
            if key in {"User-Agent", "Accept", "Accept-Language"}:
                continue
            curl_cmd.extend(["-H", f"{key}: {value}"])
        try:
            proc = subprocess.run(
                curl_cmd,
                text=True,
                capture_output=True,
                check=False,
            )
            if proc.returncode == 0 and proc.stdout:
                logger.info("curl fallback succeeded for %s", url)
                return proc.stdout
            logger.debug(
                "curl fallback failed for %s (code=%s): %s",
                url, proc.returncode, (proc.stderr or "").strip(),
            )
        except Exception as exc:
            logger.debug("curl fallback failed for %s: %s", url, exc)

    if got_forbidden:
        logger.warning("403 forbidden for %s", url)
    return None


def fetch_rss(source: dict, timeout: int = 10, retries: int = 2) -> list[RawItem]:
    text = _http_get(
        source["url"],
        timeout,
        retries,
        extra_headers=source.get("headers"),
        use_curl_fallback=bool(source.get("curl_fallback", False)),
    )
    if text is None:
        return []
    feed = feedparser.parse(text)
    now_iso = datetime.now(timezone.utc).isoformat()
    items: list[RawItem] = []
    for entry in feed.entries:
        published = entry.get("published") or ""
        updated = entry.get("updated") or ""
        title = (entry.get("title") or "").strip()

        # published가 있으면 그것을 사용, 없으면 updated를 사용하되
        # 제목에 날짜 힌트가 있으면 updated와 교차 검증한다.
        if published:
            pub = published
        elif updated:
            title_hint = _extract_date_hint_from_title(title)
            updated_date = _parse_date_safe(updated)
            if title_hint and updated_date:
                # 제목 힌트 월과 updated 월이 30일 넘게 차이나면
                # 제목 힌트를 발행일로 사용
                diff = abs((updated_date - title_hint).days)
                if diff > 30:
                    logger.debug(
                        "Title date hint %s differs from updated %s for '%s', "
                        "using title hint",
                        title_hint, updated_date, title,
                    )
                    pub = title_hint.isoformat()
                else:
                    pub = updated
            else:
                pub = updated
        else:
            pub = ""

        raw_summary = (entry.get("summary") or entry.get("description") or "").strip()
        items.append(RawItem(
            source_id=source["id"],
            source_name=source["name"],
            title=title,
            url=(entry.get("link") or "").strip(),
            published_at=pub,
            summary=_clean_summary(_strip_html(raw_summary)),
            fetched_at=now_iso,
        ))
    return items


def fetch_json_feed(source: dict, timeout: int = 10, retries: int = 2) -> list[RawItem]:
    text = _http_get(
        source["url"],
        timeout,
        retries,
        extra_headers=source.get("headers"),
        use_curl_fallback=bool(source.get("curl_fallback", False)),
    )
    if text is None:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        logger.warning("Invalid JSON from %s", source["id"])
        return []
    if not isinstance(data, list):
        data = data.get("items", [])
    fm = source.get("field_map", {})
    now_iso = datetime.now(timezone.utc).isoformat()
    items: list[RawItem] = []
    for entry in data:
        items.append(RawItem(
            source_id=source["id"],
            source_name=source["name"],
            title=str(entry.get(fm.get("title", "title"), "")).strip(),
            url=str(entry.get(fm.get("url", "url"), "")).strip(),
            published_at=str(entry.get(fm.get("published_at", "published_at"), "")),
            summary=str(entry.get(fm.get("summary", "summary"), "")),
            fetched_at=now_iso,
        ))
    return items


def load_manual_items(path: Path) -> list[RawItem]:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not data or not data.get("items"):
        return []
    now_iso = datetime.now(timezone.utc).isoformat()
    items: list[RawItem] = []
    for entry in data["items"]:
        items.append(RawItem(
            source_id="manual",
            source_name=entry.get("source_name", "Manual"),
            title=entry.get("title", ""),
            url=entry.get("url", ""),
            published_at=entry.get("published_at", ""),
            summary=entry.get("summary", ""),
            fetched_at=now_iso,
        ))
    return items


def _extract_date_hint_from_title(title: str) -> date | None:
    """제목에서 날짜/연월 힌트를 추출한다.

    예: "FE News 25년 12월 소식" → 2025-12-01
        "2025년 11월 뉴스레터"   → 2025-11-01
    """
    # "25년 12월" or "2025년 12월"
    m = re.search(r"(\d{2,4})년\s*(\d{1,2})월", title)
    if m:
        y = int(m.group(1))
        if y < 100:
            y += 2000
        mo = int(m.group(2))
        if 1 <= mo <= 12:
            try:
                return date(y, mo, 1)
            except ValueError:
                pass
    # "2025-12" or "2025/12"
    m = re.search(r"(20\d{2})[-/](\d{1,2})", title)
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        if 1 <= mo <= 12:
            try:
                return date(y, mo, 1)
            except ValueError:
                pass
    return None


def _parse_date_safe(s: str) -> date | None:
    if not s:
        return None
    try:
        return dateutil_parser.parse(s).date()
    except (ValueError, OverflowError):
        return None


def collect(
    sources: list[dict], date_from: date, date_to: date,
) -> tuple[list[RawItem], list[str]]:
    all_items: list[RawItem] = []
    warnings: list[str] = []
    success_count = 0
    total_count = 0

    for src in sources:
        src_type = src.get("type", "rss")
        total_count += 1
        try:
            if src_type in ("rss", "atom"):
                raw = fetch_rss(src)
            elif src_type == "json":
                raw = fetch_json_feed(src)
            elif src_type == "manual":
                raw = load_manual_items(SCRIPT_DIR / "data" / "manual_items.yml")
            else:
                logger.warning("Unknown source type %s for %s", src_type, src["id"])
                warnings.append(f"unknown type: {src['id']}")
                continue

            if not raw and src_type != "manual":
                warnings.append(f"source empty or failed: {src['id']}")
            else:
                success_count += 1

            filtered = []
            for item in raw:
                # 발행일 기준으로 기간 필터를 적용한다.
                # 발행일이 없으면 피드에 올라온 최신 글로 간주하여
                # 수집 종료일(date_to)을 발행일로 사용한다.
                pub_date = _parse_date_safe(item.published_at)
                if not pub_date:
                    item.published_at = date_to.isoformat()
                    pub_date = date_to
                if date_from <= pub_date <= date_to:
                    filtered.append(item)
            all_items.extend(filtered)
            logger.info(
                "Source %s: %d collected, %d after date filter",
                src["id"], len(raw), len(filtered),
            )
        except Exception as exc:
            warnings.append(f"source timeout: {src['id']}: {exc}")
            logger.warning("Failed to collect from %s: %s", src["id"], exc)

    logger.info(
        "Collected %d items from %d/%d sources",
        len(all_items), success_count, total_count,
    )
    return all_items, warnings


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------
def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()
    path = parsed.path
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    qs = parse_qs(parsed.query, keep_blank_values=False)
    cleaned_qs = {k: v for k, v in qs.items() if k.lower() not in TRACKING_PARAMS}
    query = urlencode(cleaned_qs, doseq=True)
    return urlunparse((scheme, netloc, path, parsed.params, query, ""))


def normalize_items(raw_items: list[RawItem]) -> list[NormalizedItem]:
    items: list[NormalizedItem] = []
    for raw in raw_items:
        n_url = normalize_url(raw.url)
        item_id = hashlib.sha1(n_url.encode()).hexdigest()
        domain = urlparse(n_url).netloc
        pub_date = (
            _parse_date_safe(raw.published_at) or _parse_date_safe(raw.fetched_at)
        )
        pub_str = pub_date.isoformat() if pub_date else ""
        items.append(NormalizedItem(
            id=item_id,
            source_id=raw.source_id,
            title=raw.title,
            url=n_url,
            domain=domain,
            published_date=pub_str,
            source_name=raw.source_name,
            summary=raw.summary,
        ))
    return items


# ---------------------------------------------------------------------------
# Dedup
# ---------------------------------------------------------------------------
def dedup_by_url(items: list[NormalizedItem]) -> list[NormalizedItem]:
    seen: dict[str, NormalizedItem] = {}
    for item in items:
        if item.id not in seen:
            seen[item.id] = item
    result = list(seen.values())
    logger.info("URL dedup: %d → %d", len(items), len(result))
    return result


def dedup_by_title(items: list[NormalizedItem], threshold: int = 92) -> list[NormalizedItem]:
    if not items:
        return items
    removed: set[int] = set()
    for i in range(len(items)):
        if i in removed:
            continue
        for j in range(i + 1, len(items)):
            if j in removed:
                continue
            ratio = fuzz.token_sort_ratio(items[i].title, items[j].title)
            if ratio >= threshold:
                removed.add(j)
    result = [item for idx, item in enumerate(items) if idx not in removed]
    logger.info("Title dedup: %d → %d", len(items), len(result))
    return result


def dedup_by_history(
    items: list[NormalizedItem], history_path: Path,
) -> tuple[list[NormalizedItem], int]:
    if not history_path.exists():
        return items, 0
    known_ids: set[str] = set()
    with open(history_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    known_ids.add(json.loads(line)["id"])
                except (json.JSONDecodeError, KeyError):
                    pass
    before = len(items)
    result = [item for item in items if item.id not in known_ids]
    removed = before - len(result)
    logger.info("History dedup: %d → %d (removed %d)", before, len(result), removed)
    return result, removed


# ---------------------------------------------------------------------------
# Quality filter
# ---------------------------------------------------------------------------
def quality_filter(
    items: list[NormalizedItem],
    source_filter_map: dict[str, dict] | None = None,
) -> list[NormalizedItem]:
    result: list[NormalizedItem] = []
    source_filter_map = source_filter_map or {}
    for item in items:
        title_lower = item.title.lower()
        summary_lower = item.summary.lower()
        text_lower = f"{title_lower} {summary_lower}"
        if len(item.title) < 8:
            continue
        if any(kw in title_lower or kw in summary_lower for kw in AD_KEYWORDS):
            continue
        if not item.summary and len(item.title) < 20:
            continue

        # 소스별 포함/제외 키워드 필터
        sf = source_filter_map.get(item.source_id, {})
        include_keywords = [k.lower() for k in sf.get("include_keywords", [])]
        exclude_keywords = [k.lower() for k in sf.get("exclude_keywords", [])]
        if include_keywords and not any(k in text_lower for k in include_keywords):
            continue
        if exclude_keywords and any(k in text_lower for k in exclude_keywords):
            continue

        result.append(item)
    logger.info("Quality filter: %d → %d", len(items), len(result))
    return result


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------
def classify(items: list[NormalizedItem], rules: dict) -> list[NormalizedItem]:
    categories = rules.get("categories", {})
    default = rules.get("default", "Etc")
    for item in items:
        text = (item.title + " " + item.summary).lower()
        matched = None
        for cat in CATEGORY_PRIORITY:
            keywords = categories.get(cat, [])
            for kw in keywords:
                if kw.lower() in text:
                    matched = cat
                    break
            if matched:
                break
        item.category = matched or default
    return items


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------
def score_and_select(
    items: list[NormalizedItem],
    max_links: int,
    source_trust_map: dict[str, float],
) -> list[NormalizedItem]:
    if not items:
        return items

    pub_dates = [_parse_date_safe(it.published_date) for it in items]
    valid_dates = [d for d in pub_dates if d]
    latest = max(valid_dates) if valid_dates else date.today()
    recent_cutoff = latest - timedelta(days=3)

    for item in items:
        item.score = source_trust_map.get(item.source_name, 0.5)

    for item in items:
        d = _parse_date_safe(item.published_date)
        if d and d >= recent_cutoff:
            item.score += 0.1

    domain_counts = Counter(it.domain for it in items)
    for item in items:
        if domain_counts[item.domain] > 3:
            item.score -= 0.2

    cat_counts = Counter(it.category for it in items)
    total = len(items)
    for cat, cnt in cat_counts.items():
        if cnt / total > 0.5:
            for item in items:
                if item.category == cat:
                    item.score -= 0.1

    # 소스 다양성: 소스당 상한을 두고 선택
    items.sort(key=lambda x: x.score, reverse=True)
    num_sources = len(set(it.source_name for it in items))
    per_source_cap = max(3, max_links // max(num_sources, 1))
    source_taken: dict[str, int] = {}
    selected: list[NormalizedItem] = []
    overflow: list[NormalizedItem] = []
    for item in items:
        cnt = source_taken.get(item.source_name, 0)
        if cnt < per_source_cap:
            selected.append(item)
            source_taken[item.source_name] = cnt + 1
        else:
            overflow.append(item)
        if len(selected) >= max_links:
            break
    # 상한에 못 미치면 overflow에서 채움
    if len(selected) < max_links:
        for item in overflow:
            selected.append(item)
            if len(selected) >= max_links:
                break
    logger.info("Scored and selected: %d → %d", len(items), len(selected))
    return selected


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def render_markdown(
    items: list[NormalizedItem], template_path: Path, date_to: date,
    date_from: date | None = None,
) -> str:
    if date_from is None:
        date_from = date_to - timedelta(days=6)
    title = (
        f"주간 테크/개발 뉴스 #{date_to.year} "
        f"{date_from.month}/{date_from.day} ~ {date_to.month}/{date_to.day}"
    )

    sections: dict[str, list[NormalizedItem]] = {}
    for display_name in SECTION_ORDER:
        sections[display_name] = []

    for item in items:
        display = CATEGORY_DISPLAY.get(item.category, item.category)
        if display not in sections:
            sections[display] = []
        sections[display].append(item)

    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        keep_trailing_newline=True,
    )
    template = env.get_template(template_path.name)
    return template.render(
        title=title,
        date=date_to.isoformat(),
        sections=sections,
        total_count=len(items),
        range_from=date_from.isoformat(),
        range_to=date_to.isoformat(),
    )


def save_report(
    report_data: dict, run_dir: Path,
    collected: list, filtered: list, selected: list,
) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    with open(run_dir / "report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    for name, data in [
        ("collected.jsonl", collected),
        ("filtered.jsonl", filtered),
        ("selected.jsonl", selected),
    ]:
        with open(run_dir / name, "w", encoding="utf-8") as f:
            for item in data:
                obj = asdict(item) if hasattr(item, "__dataclass_fields__") else item
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
    logger.info("Report saved to %s", run_dir)


def append_history(items: list[NormalizedItem], history_path: Path) -> None:
    history_path.parent.mkdir(parents=True, exist_ok=True)
    today_str = date.today().isoformat()

    with open(history_path, "a", encoding="utf-8") as f:
        for item in items:
            record = {
                "id": item.id,
                "url": item.url,
                "published_date": item.published_date,
                "run_date": today_str,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # Clean entries older than 90 days
    cutoff = (date.today() - timedelta(days=90)).isoformat()
    if history_path.exists():
        lines = history_path.read_text(encoding="utf-8").strip().split("\n")
        kept = []
        for line in lines:
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
                if rec.get("run_date", "") >= cutoff:
                    kept.append(line)
            except json.JSONDecodeError:
                pass
        history_path.write_text(
            "\n".join(kept) + "\n" if kept else "", encoding="utf-8",
        )

    logger.info("History updated: %d items appended", len(items))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="주간 테크/개발 뉴스 링크 모음 생성")
    today = date.today()
    parser.add_argument(
        "--from", dest="date_from",
        default=(today - timedelta(days=6)).isoformat(),
        help="수집 시작일 (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--to", dest="date_to", default=today.isoformat(),
        help="수집 종료일 (YYYY-MM-DD)",
    )
    parser.add_argument("--max-links", type=int, default=50, help="최종 링크 상한")
    parser.add_argument("--output-dir", default="normal/_posts", help="MD 저장 경로")
    parser.add_argument("--dry-run", action="store_true", help="파일 미생성, 콘솔 출력만")
    parser.add_argument("--sources", default=None, help="소스 파일 경로")
    parser.add_argument("--no-history", action="store_true", help="히스토리 중복 체크 건너뛰기")
    parser.add_argument("--verbose", action="store_true", help="상세 로그")
    parser.add_argument(
        "--summary-max-sentences",
        type=int,
        default=2,
        help="요약 최대 문장 수 (기본: 2)",
    )
    parser.add_argument(
        "--summary-max-chars",
        type=int,
        default=220,
        help="요약 최대 글자 수 (기본: 220)",
    )
    parser.add_argument(
        "--translate-en-summary-to-ko",
        action="store_true",
        help="영문 요약을 한글로 번역",
    )
    parser.add_argument(
        "--translator",
        choices=["google", "openai"],
        default="google",
        help="번역 엔진 선택 (기본: google, openai는 OPENAI_API_KEY 필요)",
    )
    parser.add_argument(
        "--openai-model",
        default="gpt-4o-mini",
        help="번역에 사용할 OpenAI 모델 (기본: gpt-4o-mini)",
    )
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
        stream=sys.stdout,
    )

    date_from = date.fromisoformat(args.date_from)
    date_to = date.fromisoformat(args.date_to)
    sources_path = Path(args.sources) if args.sources else SCRIPT_DIR / "sources.yml"
    rules_path = SCRIPT_DIR / "category_rules.yml"
    template_path = SCRIPT_DIR / "templates" / "weekly_digest.md.j2"
    history_path = SCRIPT_DIR / "data" / "history" / "url_history.jsonl"
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = SCRIPT_DIR.parent / output_dir

    logger.info("=== Weekly Digest: %s ~ %s ===", date_from, date_to)

    # 1. Load sources & rules
    sources = load_sources(sources_path)
    rules = load_category_rules(rules_path)
    source_trust_map = {s["name"]: s.get("trust", 0.5) for s in sources}
    source_filter_map = {
        s["id"]: {
            "include_keywords": s.get("include_keywords", []),
            "exclude_keywords": s.get("exclude_keywords", []),
        }
        for s in sources
    }
    logger.info("Loaded %d enabled sources", len(sources))

    # 2. Collect
    raw_items, warnings = collect(sources, date_from, date_to)
    total_sources = len(sources)
    failed = len([
        w for w in warnings
        if "failed" in w or "timeout" in w or "empty" in w
    ])
    success = total_sources - failed
    if total_sources > 0 and success / total_sources < 0.3:
        logger.error("Too few sources succeeded: %d/%d", success, total_sources)
        sys.exit(2)

    # 3. Normalize
    normalized = normalize_items(raw_items)
    after_date_filter = len(normalized)

    # 4. Dedup
    deduped = dedup_by_url(normalized)
    deduped = dedup_by_title(deduped)
    history_removed = 0
    if not args.no_history:
        deduped, history_removed = dedup_by_history(deduped, history_path)
    after_dedup = len(deduped)

    # 5. Quality filter
    filtered = quality_filter(deduped, source_filter_map=source_filter_map)
    after_quality = len(filtered)

    # 6. Classify
    classified = classify(filtered, rules)

    # 7. Score & select
    selected = score_and_select(classified, args.max_links, source_trust_map)

    # 7.5 Summary postprocess (translate + compress)
    translator = None
    if args.translate_en_summary_to_ko:
        if args.translator == "google":
            translator = GoogleTranslator()
            logger.info("Using Google Translate for EN→KO translation")
        else:
            api_key = os.getenv("OPENAI_API_KEY", "").strip()
            if not api_key:
                logger.warning(
                    "--translator=openai but OPENAI_API_KEY is missing. "
                    "Fallback to original summaries.",
                )
            else:
                translator = OpenAITranslator(api_key=api_key, model=args.openai_model)
    selected = postprocess_summaries(
        selected,
        max_sentences=max(1, args.summary_max_sentences),
        max_chars=max(60, args.summary_max_chars),
        translate_en_to_ko=args.translate_en_summary_to_ko,
        translator=translator,
    )

    # 8. Render
    markdown = render_markdown(selected, template_path, date_to, date_from)

    # Category breakdown for report
    cat_breakdown = dict(Counter(it.category for it in selected))
    cat_display_breakdown = {}
    for k, v in cat_breakdown.items():
        cat_display_breakdown[CATEGORY_DISPLAY.get(k, k)] = v

    # Report data
    run_dir = SCRIPT_DIR / "data" / "runs" / date_to.isoformat()
    week_num = date_to.isocalendar()[1]
    filename = (
        f"{date_to.isoformat()}-weekly-dev-links-{date_to.year}w{week_num:02d}.md"
    )
    output_path = output_dir / filename

    if output_path.exists() and not args.dry_run:
        for v in range(2, 100):
            alt = output_dir / filename.replace(".md", f"_v{v}.md")
            if not alt.exists():
                output_path = alt
                break

    report_data = {
        "run_date": date.today().isoformat(),
        "range": {"from": date_from.isoformat(), "to": date_to.isoformat()},
        "source_count": total_sources,
        "collected": len(raw_items),
        "after_date_filter": after_date_filter,
        "after_dedup": after_dedup,
        "after_quality_filter": after_quality,
        "selected": len(selected),
        "output_file": (
            str(output_path.relative_to(SCRIPT_DIR.parent))
            if not args.dry_run else "(dry-run)"
        ),
        "warnings": warnings,
        "category_breakdown": cat_display_breakdown,
        "history_duplicates_removed": history_removed,
    }

    if args.dry_run:
        print("\n" + "=" * 60)
        print("DRY RUN — Generated Markdown:")
        print("=" * 60)
        print(markdown)
        print("=" * 60)
        print("\nReport:")
        print(json.dumps(report_data, ensure_ascii=False, indent=2))
        save_report(report_data, run_dir, raw_items, filtered, selected)
    else:
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown, encoding="utf-8")
            logger.info("Markdown saved to %s", output_path)
        except OSError as exc:
            logger.error("Failed to write output: %s", exc)
            sys.exit(3)
        save_report(report_data, run_dir, raw_items, filtered, selected)
        append_history(selected, history_path)

    logger.info("Done. Selected %d items.", len(selected))


if __name__ == "__main__":
    main()
