#!/usr/bin/env python3
"""주간 다이제스트 후보 수집기 (테크뉴스 / Indie Radar / 도서).

기존 weekly_digest.py가 "선택·렌더링"까지 하던 것과 달리, 이 스크립트는
섹션별 후보와 인기 신호(점수·순위·매출)만 모아 JSON/Markdown으로 저장한다.
최종 선정과 요약 작성은 weekly-digest 스킬(Claude)이 담당한다.
"""
from __future__ import annotations

import argparse
import html
import json
import logging
import re
import sys
import time
from datetime import date, datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path

import feedparser

import weekly_digest as wd

SCRIPT_DIR = Path(__file__).resolve().parent
KST = timezone(timedelta(hours=9))

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"
GEEKNEWS_PAST_URL = "https://news.hada.io/past?day={day}"
AITIMES_URL = "https://www.aitimes.com/"
TECHMEME_FEED_URL = "https://www.techmeme.com/feed.xml"
PRODUCTHUNT_FEED_URL = "https://www.producthunt.com/feed"
BETALIST_FEED_URL = "https://feeds.feedburner.com/BetaList"
ITCH_FEED_URL = "https://itch.io/games/new-and-popular.xml"
REDDIT_TOP_FEED_URL = "https://www.reddit.com/r/{sub}/top/.rss?t=week"
TRUSTMRR_URL = "https://trustmrr.com/"
GITHUB_TRENDING_URL = "https://github.com/trending?since=weekly"
ALADIN_BEST_URL = (
    "https://www.aladin.co.kr/shop/common/wbest.aspx"
    "?BestType=Bestseller&BranchType=1&CID={cid}"
)
ALADIN_NEW_URL = (
    "https://www.aladin.co.kr/shop/common/wnew.aspx"
    "?NewType=SpecialNew&BranchType=1&CID={cid}"
)

REDDIT_SUBS = ["SideProject", "SaaS"]
ALADIN_CATEGORIES = {"소설": 1, "IT": 351, "인문": 656}

# 뉴스 섹션에서 기존 RSS 소스 중 GitHub Trending은 Indie Radar로 보낸다
NEWS_SOURCE_TYPES = {"rss", "atom", "json"}

logger = logging.getLogger("weekly_radar")


def _text(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def _get(url: str, **kwargs) -> str | None:
    return wd._http_get(url, timeout=20, retries=1, **kwargs)


def _week_epoch_range(date_from: date, date_to: date) -> tuple[int, int]:
    start = datetime.combine(date_from, datetime.min.time(), KST)
    end = datetime.combine(date_to + timedelta(days=1), datetime.min.time(), KST)
    return int(start.timestamp()), int(end.timestamp())


def _in_range(published: str, date_from: date, date_to: date) -> bool:
    d = wd._parse_date_safe(published)
    return d is not None and date_from <= d <= date_to


def _previous_post_urls(posts_dir: Path, count: int = 2) -> set[str]:
    posts = sorted(posts_dir.glob("*weekly-dev-links*.md"))[-count:]
    urls: set[str] = set()
    for p in posts:
        for u in re.findall(r"\]\((https?://[^)\s]+)\)", p.read_text(encoding="utf-8")):
            urls.add(wd.normalize_url(u))
    return urls


# ---------------------------------------------------------------------------
# 1) 테크뉴스
# ---------------------------------------------------------------------------
def fetch_hn(tags: str, date_from: date, date_to: date, min_points: int, limit: int) -> list[dict]:
    start, end = _week_epoch_range(date_from, date_to)
    text = _get(
        f"{HN_SEARCH_URL}?tags={tags}&hitsPerPage=100"
        f"&numericFilters=created_at_i%3E{start},created_at_i%3C{end},points%3E{min_points}",
        extra_headers={"Accept": "application/json"},
    )
    if not text:
        return []
    hits = sorted(json.loads(text).get("hits", []), key=lambda h: -h.get("points", 0))
    return [
        {
            "title": h["title"],
            "url": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
            "discussion": f"https://news.ycombinator.com/item?id={h['objectID']}",
            "signals": {"hn_points": h.get("points", 0), "hn_comments": h.get("num_comments", 0)},
        }
        for h in hits[:limit]
    ]


@lru_cache(maxsize=4)
def fetch_geeknews_week(date_from: date, date_to: date) -> list[dict]:
    """GeekNews 일자별 past 페이지에서 제목·포인트·댓글 수를 수집한다."""
    items: list[dict] = []
    day = date_from
    while day <= date_to:
        text = _get(GEEKNEWS_PAST_URL.format(day=day.isoformat())) or ""
        for row in text.split("<div class='topic_row'")[1:]:
            title = re.search(r"<h2 class='topic-title-heading'>(.*?)</h2>", row, flags=re.DOTALL)
            points = re.search(r"<span id='tp(\d+)'>(\d+)</span>", row)
            if not title or not points:
                continue
            comments = re.search(r"data-topic-comment-count='(\d+)'", row)
            domain = re.search(r"<span class=topicurl>\((.*?)\)</span>", row)
            items.append({
                "title": _text(title.group(1)),
                "url": f"https://news.hada.io/topic?id={points.group(1)}",
                "date": day.isoformat(),
                "domain": domain.group(1) if domain else "",
                "signals": {
                    "geeknews_points": int(points.group(2)),
                    "geeknews_comments": int(comments.group(1)) if comments else 0,
                },
            })
        day += timedelta(days=1)
        # 연속 요청 시 403이 반환되므로 간격을 둔다
        time.sleep(1.5)
    items.sort(key=lambda x: (-x["signals"]["geeknews_points"], -x["signals"]["geeknews_comments"]))
    return items


def fetch_aitimes_popular() -> list[dict]:
    """aitimes 메인의 Most Popular 목록 (조회 시점 기준 스냅샷)."""
    text = _get(AITIMES_URL) or ""
    start = text.find("Most<br/>Popular")
    block = text[start:start + 20000] if start >= 0 else ""
    items = []
    for rank, url, title in re.findall(
        r'<div class="number[^"]*">(\d+)</div>\s*<a href="([^"]+)"[^>]*>\s*<H2[^>]*>(.*?)</H2>',
        block,
        flags=re.DOTALL | re.IGNORECASE,
    ):
        items.append({"title": _text(title), "url": url, "signals": {"aitimes_rank": int(rank)}})
    return items


def fetch_feed(url: str, date_from: date | None = None, date_to: date | None = None,
               limit: int = 50) -> list[dict]:
    text = _get(url, use_curl_fallback=True)
    if not text:
        return []
    items = []
    for rank, entry in enumerate(feedparser.parse(text).entries, start=1):
        published = entry.get("published") or entry.get("updated") or ""
        if date_from and not _in_range(published, date_from, date_to):
            continue
        pub_date = wd._parse_date_safe(published)
        items.append({
            "title": _text(entry.get("title", "")),
            "url": (entry.get("link") or "").strip(),
            "date": pub_date.isoformat() if pub_date else "",
            "summary": wd._compress_summary(_text(entry.get("summary", "")), 2, 220),
            "signals": {"feed_rank": rank},
        })
        if len(items) >= limit:
            break
    return items


def collect_news(date_from: date, date_to: date) -> dict:
    sources = [
        s for s in wd.load_sources(SCRIPT_DIR / "sources.yml")
        if s.get("type", "rss") in NEWS_SOURCE_TYPES
    ]
    raw, warnings = wd.collect(sources, date_from, date_to)
    items = wd.dedup_by_title(wd.dedup_by_url(wd.normalize_items(raw)))
    prev_urls = _previous_post_urls(SCRIPT_DIR.parent / "normal" / "_posts")
    rss_items = [
        {"title": i.title, "url": i.url, "source": i.source_id, "date": i.published_date,
         "summary": i.summary}
        for i in items if i.url not in prev_urls
    ]
    return {
        "hn_top": fetch_hn("story", date_from, date_to, min_points=300, limit=40),
        "geeknews_top": [
            g for g in fetch_geeknews_week(date_from, date_to)
            if not g["title"].startswith("Show GN")
        ][:40],
        "aitimes_popular": fetch_aitimes_popular(),
        "techmeme": fetch_feed(TECHMEME_FEED_URL, date_from, date_to, limit=40),
        "rss": rss_items,
        "warnings": warnings,
    }


# ---------------------------------------------------------------------------
# 2) Indie Radar
# ---------------------------------------------------------------------------
def fetch_trustmrr() -> dict[str, list[dict]]:
    """TrustMRR 메인에 내장된 Next.js 데이터에서 매출 검증 스타트업을 추출한다."""
    text = _get(TRUSTMRR_URL) or ""
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', text, flags=re.DOTALL)
    blob = "".join(json.loads(f'"{c}"') for c in chunks)
    decoder = json.JSONDecoder()
    lists: dict[str, list[dict]] = {}
    for m in re.finditer(r'"(\w+)":\[\{"_id"', blob):
        if m.group(1) in lists:
            continue
        arr, _ = decoder.raw_decode(blob, m.end() - len('[{"_id"'))
        lists[m.group(1)] = arr

    def pick(s: dict) -> dict:
        return {
            "title": s.get("name"),
            "url": f"https://trustmrr.com/startup/{s.get('slug')}",
            "summary": _text(s.get("description") or "")[:300],
            "founder_x": s.get("xHandle"),
            "signals": {
                "mrr_usd": round(s.get("currentMrr") or 0),
                "last30d_revenue_usd": round(s.get("currentLast30DaysRevenue") or 0),
                "total_revenue_usd": round(s.get("currentTotalRevenue") or 0),
                "growth_30d_pct": round(s.get("cachedGrowth30d") or 0, 1),
                "on_sale": bool(s.get("onSale")),
            },
        }

    def visible(s: dict) -> bool:
        name = (s.get("name") or "").lower()
        return not s.get("stealthMode") and not any(
            w in name for w in ("stealth", "hidden business", "private venture")
        )

    # 성장률 목록은 매출이 아주 작은 곳이 상위를 차지하므로 최소 매출로 거른다
    growth = [
        pick(s) for s in lists.get("growth", [])
        if visible(s) and (s.get("currentLast30DaysRevenue") or 0) >= 1000
    ][:20]
    # 초대형(Gumroad 등)을 제외한 "1인~소규모" 매출 구간
    mid_mrr = [
        pick(s) for s in lists.get("mrr", [])
        if visible(s) and 2000 <= (s.get("currentMrr") or 0) <= 100000
        and (s.get("cachedGrowth30d") or 0) > 10
    ][:20]
    return {"trustmrr_growth": growth, "trustmrr_growing_mrr": mid_mrr}


def fetch_github_trending(limit: int = 15) -> list[dict]:
    text = _get(GITHUB_TRENDING_URL, use_curl_fallback=True) or ""
    items = []
    for block in re.findall(r"<article[^>]*Box-row[^>]*>.*?</article>", text, flags=re.DOTALL):
        repo = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([\w.-]+/[\w.-]+)"', block)
        if not repo:
            continue
        desc = re.search(r"<p(?:\s[^>]*)?>(.*?)</p>", block, flags=re.DOTALL)
        stars = re.search(r"([\d,]+)\s+stars this week", block)
        items.append({
            "title": repo.group(1),
            "url": f"https://github.com/{repo.group(1)}",
            "summary": _text(desc.group(1)) if desc else "",
            "signals": {"stars_this_week": int(stars.group(1).replace(",", "")) if stars else 0},
        })
    return items[:limit]


def collect_indie(date_from: date, date_to: date) -> dict:
    result: dict = {
        "hn_show": fetch_hn("show_hn", date_from, date_to, min_points=40, limit=30),
        "geeknews_show": [
            g for g in fetch_geeknews_week(date_from, date_to)
            if g["title"].startswith("Show GN")
        ][:20],
        "producthunt": fetch_feed(PRODUCTHUNT_FEED_URL, date_from, date_to, limit=30),
        "betalist": fetch_feed(BETALIST_FEED_URL, date_from, date_to, limit=30),
        "itch_new_popular": fetch_feed(ITCH_FEED_URL, limit=20),
        "github_trending": fetch_github_trending(),
    }
    for sub in REDDIT_SUBS:
        # Reddit은 연속 요청 시 429를 반환하므로 간격을 두고 한 번 더 시도한다
        for wait in (5, 30):
            time.sleep(wait)
            items = fetch_feed(REDDIT_TOP_FEED_URL.format(sub=sub), limit=20)
            if items:
                break
        result[f"reddit_{sub.lower()}"] = items
    result.update(fetch_trustmrr())
    return result


# ---------------------------------------------------------------------------
# 3) 도서 (알라딘)
# ---------------------------------------------------------------------------
def _parse_aladin_list(text: str, limit: int) -> list[dict]:
    books = []
    for block in re.findall(r'<div class="ss_book_list"><ul>(.*?)</ul></div>', text, flags=re.DOTALL):
        title = re.search(
            r'<a href="(https://www\.aladin\.co\.kr/shop/wproduct\.aspx\?ItemId=\d+)" class="bo3">'
            r"(?:<b>)?(.*?)(?:</b>)?</a>(?:<span class=\"ss_f_g2\">(.*?)</span>)?",
            block, flags=re.DOTALL,
        )
        if not title:
            continue
        meta = re.search(r"AuthorSearch=.*?</li>", block, flags=re.DOTALL)
        meta_text = _text("<" + meta.group(0)) if meta else ""
        sales = re.search(r'sales_point">\s*([\d,]+)', block)
        books.append({
            "title": _text(title.group(2)),
            "subtitle": _text(title.group(3) or "").lstrip("- "),
            "url": title.group(1),
            "meta": re.sub(r"^[^>]*>\s*", "", meta_text),
            "signals": {"sales_point": int(sales.group(1).replace(",", "")) if sales else 0},
        })
        if len(books) >= limit:
            break
    return books


def _aladin_prev_week_url(base_url: str, text: str) -> str | None:
    m = re.search(r"Year=(\d+)&Month=(\d+)&Week=(\d+)", text)
    if not m:
        return None
    year, month, week = map(int, m.groups())
    if week > 1:
        return f"{base_url}&Year={year}&Month={month}&Week={week - 1}"
    prev = date(year, month, 1) - timedelta(days=1)
    return f"{base_url}&Year={prev.year}&Month={prev.month}&Week=5"


def collect_books(limit: int = 20) -> dict:
    result = {}
    for name, cid in ALADIN_CATEGORIES.items():
        best_url = ALADIN_BEST_URL.format(cid=cid)
        best_text = _get(best_url) or ""
        best = _parse_aladin_list(best_text, limit)
        prev_titles: set[str] = set()
        prev_url = _aladin_prev_week_url(best_url, best_text)
        if prev_url:
            prev_text = _get(prev_url) or ""
            # 5주차가 없는 달이면 4주차로 재시도
            if not _parse_aladin_list(prev_text, 1) and prev_url.endswith("Week=5"):
                prev_text = _get(prev_url[:-1] + "4") or ""
            prev_titles = {b["title"] for b in _parse_aladin_list(prev_text, 50)}
        for rank, book in enumerate(best, start=1):
            book["signals"]["rank"] = rank
            book["signals"]["new_entry"] = bool(prev_titles) and book["title"] not in prev_titles
        result[name] = {
            "bestseller": best,
            "special_new": _parse_aladin_list(_get(ALADIN_NEW_URL.format(cid=cid)) or "", limit),
        }
    return result


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def _signals_str(signals: dict) -> str:
    return ", ".join(f"{k}={v}" for k, v in signals.items() if v not in (None, "", False))


def render_section_md(data: dict, section: str) -> str:
    """스킬이 섹션별로 나눠 읽을 수 있도록 후보 목록을 Markdown으로 만든다."""
    titles = {"news": "테크 뉴스", "indie": "Indie Radar", "books": "도서"}
    lines = [f"# {titles[section]} 후보 {data['date_from']} ~ {data['date_to']}", ""]
    if section == "books":
        for cat, lists in data["books"].items():
            for kind, books in lists.items():
                lines += [f"## {cat} / {kind} ({len(books)})", ""]
                for b in books:
                    sub = f" — {b['subtitle']}" if b.get("subtitle") else ""
                    lines.append(f"- [{b['title']}]({b['url']}){sub} | {b['meta']} `{_signals_str(b['signals'])}`")
                lines.append("")
        return "\n".join(lines)
    for group, items in data[section].items():
        if group == "warnings":
            continue
        lines += [f"## {group} ({len(items)})", ""]
        for it in items:
            extra = _signals_str(it.get("signals", {}))
            src = it.get("source") or it.get("date") or ""
            lines.append(f"- [{it['title']}]({it['url']}) `{extra or src}`")
            if it.get("summary"):
                lines.append(f"  - {_text(it['summary'])[:120]}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="주간 다이제스트 후보 수집 (뉴스/Indie Radar/도서)")
    today = date.today()
    parser.add_argument("--from", dest="date_from", default=(today - timedelta(days=6)).isoformat())
    parser.add_argument("--to", dest="date_to", default=today.isoformat())
    parser.add_argument("--sections", default="news,indie,books", help="수집할 섹션 (쉼표 구분)")
    parser.add_argument("--out-dir", default=None, help="기본: jobs/data/runs/<to>/")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
        stream=sys.stdout,
    )
    date_from = date.fromisoformat(args.date_from)
    date_to = date.fromisoformat(args.date_to)
    sections = {s.strip() for s in args.sections.split(",")}
    out_dir = Path(args.out_dir) if args.out_dir else SCRIPT_DIR / "data" / "runs" / date_to.isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)

    data: dict = {
        "date_from": date_from.isoformat(),
        "date_to": date_to.isoformat(),
        "collected_at": datetime.now(KST).isoformat(),
        "news": {}, "indie": {}, "books": {},
    }
    if "news" in sections:
        data["news"] = collect_news(date_from, date_to)
    if "indie" in sections:
        data["indie"] = collect_indie(date_from, date_to)
    if "books" in sections:
        data["books"] = collect_books()

    for section in ("news", "indie"):
        for group, items in data[section].items():
            if group != "warnings":
                logger.info("%s/%s: %d", section, group, len(items))
                if not items:
                    logger.warning("empty group: %s/%s", section, group)
    for cat, lists in data["books"].items():
        logger.info("books/%s: best=%d new=%d", cat, len(lists["bestseller"]), len(lists["special_new"]))

    (out_dir / "radar_candidates.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    for section in sections & {"news", "indie", "books"}:
        path = out_dir / f"radar_{section}.md"
        path.write_text(render_section_md(data, section), encoding="utf-8")
        logger.info("Candidates saved: %s", path)


if __name__ == "__main__":
    main()
