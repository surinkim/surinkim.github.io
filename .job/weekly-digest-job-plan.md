# 주간 개발 소식 링크 모음 자동화 구현 계획서

## 1. 문서 목적
이 문서는 `주말 수동 실행` 방식의 주간 링크 큐레이션 프로그램을 실제로 구현하기 위한 기준 문서다.
방향성 문서가 아니라, 바로 코드를 작성할 수 있는 수준의 요구사항과 입출력 스펙을 정의한다.

## 2. 범위
- 포함
  - 최근 7일 기사/포스트 수집
  - 정규화/중복 제거/기본 품질 필터
  - 카테고리 분류
  - Jekyll Markdown 초안 파일 생성
  - 실행 로그 생성
  - 주간 중복 방지(히스토리 기반)
- 제외
  - 자동 배포
  - 완전 자동 승인
  - 고급 NLP 품질 평가

## 3. 운영 모델
- 실행 주체: 사용자(로컬)
- 실행 시점: 주말 1회(토/일)
- 승인 방식: 생성된 MD를 사람이 최종 편집 후 커밋/푸시
- 실패 허용: 일부 소스 실패 시 전체 중단하지 않고 경고 후 계속 진행

## 4. 기술 선택 (MVP)
- 언어: Python 3.11+
- 의존성
  - `feedparser` (RSS/Atom 수집)
  - `httpx` (HTTP 요청)
  - `pyyaml` (소스 설정 로딩)
  - `jinja2` (템플릿 렌더링)
  - `python-dateutil` (날짜 파싱)
  - `rapidfuzz` (제목 유사도 비교 — 9.3 중복 제거용)
- 저장 형식
- 중간 결과: JSONL
- 설정: YAML
- 출력: Markdown

## 5. 디렉터리 구조
```text
jobs/
  run_weekly_digest.sh      # venv 활성화 + weekly_digest.py 호출 래퍼
  weekly_digest.py           # 메인 엔트리포인트
  requirements.txt
  sources.yml
  category_rules.yml
  templates/
    weekly_digest.md.j2      # Jinja2 출력 템플릿
  data/
    manual_items.yml         # manual 타입 소스용 수동 항목
    cache/                   # (미래 확장) HTTP ETag/Last-Modified 캐시
    history/
      url_history.jsonl      # 과거 발행 URL 해시 누적 기록 (주간 중복 방지)
    runs/
      2026-02-07/
        collected.jsonl
        filtered.jsonl
        selected.jsonl
        report.json
```

## 6. CLI 명세
```bash
python jobs/weekly_digest.py \
  --from 2026-02-01 \
  --to 2026-02-07 \
  --max-links 20 \
  --output-dir _posts.1 \
  --dry-run
```

- 옵션
- `--from`: 수집 시작일 (기본: today-6)
- `--to`: 수집 종료일 (기본: today)
- `--max-links`: 최종 링크 상한 (기본: 20)
- `--output-dir`: MD 저장 경로 (기본: `_posts.1`)
- `--dry-run`: 파일 미생성, 콘솔/리포트만 출력
- `--sources`: 소스 파일 경로 override (기본: `jobs/sources.yml`)
- `--no-history`: 히스토리 중복 체크 건너뛰기 (테스트 용도)
- `--verbose`: 상세 로그 출력 (DEBUG 레벨)

## 7. 입력 스펙

### 7.1 `jobs/sources.yml`
```yaml
sources:
  - id: hn_hada
    name: News.hada
    type: rss
    url: https://news.hada.io/rss
    trust: 0.9
    enabled: true
  - id: github_blog
    name: GitHub Blog
    type: rss
    url: https://github.blog/feed/
    trust: 0.8
    enabled: true
```

- 필드
- `id`: 고유 ID
- `name`: 표시 이름
- `type`: `rss` | `atom` | `json` | `manual`
- `url`: 피드/엔드포인트 URL
- `trust`: 0.0~1.0
- `enabled`: 사용 여부
- `language`: `ko` | `en` (기본: `en`, 표시용 참고 정보)

#### 소스 타입별 동작
- `rss` / `atom`: `feedparser`로 파싱. `url`은 피드 URL.
- `json`: HTTP GET으로 JSON 배열 수신. 각 항목에서 `title`, `url`, `published_at` 필드를 추출. 필드 매핑이 다른 경우 소스 설정에 `field_map`을 추가.
  ```yaml
  - id: example_json
    type: json
    url: https://api.example.com/posts
    field_map:
      title: headline
      url: link
      published_at: date
  ```
- `manual`: URL 수집 대상이 아님. `jobs/data/manual_items.yml`에 직접 항목을 작성하면 수집 단계에서 합류.
  ```yaml
  # jobs/data/manual_items.yml
  - title: "수동 추가 링크 제목"
    url: https://example.com/article
    published_at: "2026-02-05"
    summary: "직접 작성한 요약"
    source_name: "Manual"
  ```

### 7.2 `jobs/category_rules.yml`
```yaml
categories:
  AI:
    - llm
    - gpt
    - agent
  Backend:
    - api
    - database
    - postgres
  InfraCloud:
    - kubernetes
    - aws
    - gcp
  Tools:
    - github
    - vscode
    - cli
default: Etc
```

## 8. 내부 데이터 모델

### 8.1 RawItem
```json
{
  "source_id": "github_blog",
  "source_name": "GitHub Blog",
  "title": "...",
  "url": "https://...",
  "published_at": "2026-02-04T10:22:00Z",
  "summary": "...",
  "fetched_at": "2026-02-07T12:10:33Z"
}
```

### 8.2 NormalizedItem
```json
{
  "id": "sha1(normalized_url)",
  "title": "...",
  "url": "https://example.com/path",
  "domain": "example.com",
  "published_date": "2026-02-04",
  "source_name": "GitHub Blog",
  "summary": "...",
  "category": "Tools",
  "score": 0.82
}
```

## 9. 파이프라인 규칙

### 9.1 수집
- enabled 소스만 순회
- 네트워크 타임아웃 10초, 재시도 2회 (재시도 간격 2초)
- 발행일이 기간 밖이면 제외
- 발행일 필드가 없는 항목: `fetched_at`을 기준 날짜로 대체
- 요약(`summary`)이 없는 피드 항목: 빈 문자열로 설정 (품질 필터에서 후속 처리)
- User-Agent 헤더: `WeeklyDigestBot/1.0 (+https://github.com/your-repo)`

### 9.2 URL 정규화
- `utm_*`, `fbclid`, `gclid` 제거
- 스킴/호스트 소문자화
- 말단 슬래시 통일

### 9.3 중복 제거
- 1차: normalized URL 해시 중복 제거
- 2차: 제목 유사도(`rapidfuzz.fuzz.token_sort_ratio`) 92 이상 시 중복 후보
- 3차: `data/history/url_history.jsonl` 내 과거 발행 URL과 해시 비교 → 이전 주에 이미 소개한 링크 제외
- 중복 시 `trust` 높은 소스 1개만 채택

### 9.4 품질 필터
- 제목 길이 < 8자 제외 (한글 기준으로도 동일 적용)
- 광고 키워드(예: "sponsored", "promo", "광고", "제휴") 포함 시 제외
- 본문 요약이 비어 있고 제목도 20자 미만이면 제외
- 영어가 아닌 비ASCII 문자 비율이 극히 높은 비개발 콘텐츠 제외 (선택)

### 9.5 카테고리 분류
- 규칙 기반 키워드 매칭 우선
- 다중 매칭 시 상위 우선순위: `AI > Backend > InfraCloud > Tools > Etc`

### 9.6 점수화 및 상한
- 기본 점수 = `trust`
- 최신성 가점: 최근 3일 +0.1
- 도메인 다양성 조정: 동일 도메인 3건 초과분 -0.2
- 카테고리 균형: 단일 카테고리가 전체 50% 초과 시 해당 카테고리 하위 항목 -0.1
- 최종 `--max-links`개 선택 (점수 내림차순 정렬 후 상위 N개)

## 10. 출력 스펙

### 10.1 파일명 규칙
- 기본: `_posts.1/YYYY-MM-DD-weekly-dev-links-YYYYwWW.md`
- 충돌 시: `_v2`, `_v3` suffix

### 10.2 Front Matter
```yaml
---
layout: post
title: "주간 개발 소식 #2026-W06"
date: 2026-02-07
categories: [normal]
tags: [weekly, links, dev-news]
---
```

### 10.3 본문 구조
- 오프닝 2~3문장
- 섹션: `AI`, `Backend`, `Infra/Cloud`, `Tools`, `Etc`
- 링크 줄 포맷
- `- [제목](URL) - 출처: SOURCE / 요약: ...`
- 마지막에 검수 체크리스트 블록

### 10.4 Jinja2 템플릿 컨텍스트
템플릿 `weekly_digest.md.j2`에 전달되는 변수:
```python
{
  "title": "주간 개발 소식 #2026-W06",
  "date": "2026-02-07",
  "sections": {
    "AI": [NormalizedItem, ...],
    "Backend": [...],
    "Infra/Cloud": [...],
    "Tools": [...],
    "Etc": [...]
  },
  "total_count": 20,
  "range_from": "2026-02-01",
  "range_to": "2026-02-07"
}
```

## 11. 리포트 스펙 (`report.json`)
```json
{
  "run_date": "2026-02-07",
  "range": {"from": "2026-02-01", "to": "2026-02-07"},
  "source_count": 8,
  "collected": 214,
  "after_date_filter": 97,
  "after_dedup": 61,
  "after_quality_filter": 33,
  "selected": 20,
  "output_file": "_posts.1/2026-02-07-weekly-dev-links-2026w06.md",
  "warnings": ["source timeout: xyz"],
  "category_breakdown": {"AI": 5, "Backend": 4, "Infra/Cloud": 3, "Tools": 5, "Etc": 3},
  "history_duplicates_removed": 2
}
```

## 12. 히스토리 관리

### 12.1 `data/history/url_history.jsonl`
성공적으로 MD 파일이 생성된 후, 선택된 항목의 URL 해시를 누적 기록한다.
```json
{"id": "sha1_hash", "url": "https://...", "published_date": "2026-02-04", "run_date": "2026-02-07"}
```

### 12.2 동작
- MD 생성 성공 시에만 히스토리에 append (dry-run 시 기록하지 않음)
- 중복 제거 단계(9.3)에서 이 파일을 읽어 과거 발행 URL을 제외
- 히스토리 파일이 없으면 빈 상태로 시작 (첫 실행 호환)
- 90일 이상 된 항목은 자동 정리 (파일 비대화 방지)

## 13. `run_weekly_digest.sh` 래퍼 스펙

```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

# venv가 없으면 생성
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
  "$VENV_DIR/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"
fi

source "$VENV_DIR/bin/activate"
python "$SCRIPT_DIR/weekly_digest.py" "$@"
```

- venv 자동 생성/활성화
- 모든 CLI 인자를 `weekly_digest.py`에 그대로 전달
- 기본 사용법: `bash jobs/run_weekly_digest.sh` 또는 `bash jobs/run_weekly_digest.sh --dry-run`

## 14. 로깅

- Python `logging` 모듈 사용
- 기본 레벨: `INFO` (stdout)
- `--verbose` 시: `DEBUG` 레벨
- 로그 포맷: `[%(asctime)s] %(levelname)s %(name)s: %(message)s`
- 각 파이프라인 단계 시작/종료 시 항목 수 로깅
  - 예: `INFO collector: Fetched 45 items from 8 sources`
  - 예: `INFO dedup: 61 → 55 after URL dedup, 55 → 48 after title dedup`
- 소스별 수집 실패 시 `WARNING` 레벨로 기록

## 15. 초기 소스 목록 (실사용 후보)

| 분류 | 이름 | 피드 URL | type |
|------|------|----------|------|
| 커뮤니티 | GeekNews (hada) | `https://news.hada.io/rss` | rss |
| 커뮤니티 | Lobsters | `https://lobste.rs/rss` | rss |
| 커뮤니티 | r/programming | `https://www.reddit.com/r/programming/.rss` | rss |
| 벤더 | GitHub Blog | `https://github.blog/feed/` | rss |
| 벤더 | Google Developers | `https://developers.googleblog.com/feeds/posts/default` | atom |
| 미디어 | InfoQ | `https://feed.infoq.com/` | rss |
| 미디어 | ITWorld Korea | `https://www.itworld.co.kr/rss/` | rss |

> **참고**: OpenAI, Anthropic 등은 공개 RSS 피드를 제공하지 않을 수 있으므로, 실제 구현 시 피드 URL 유효성을 확인 후 `sources.yml`에 등록한다. 피드가 없는 소스는 `manual` 타입으로 대체.

## 16. 수동 승인 체크리스트
- 링크 100% 클릭 확인
- 중복 이슈 제거 확인
- 과장/낚시 제목 수정
- 카테고리 오분류 수정
- 최종 링크 수 10~25개 범위 확인

## 17. 실패/예외 처리 정책
- 소스 30% 이하 성공 시 실행 실패 코드 반환(`exit 2`)
- 출력 파일 생성 실패 시 즉시 중단(`exit 3`)
- 경고는 `report.json`과 stdout 모두 기록

## 18. MVP 완료 기준 (Definition of Done)
- 명령 1회로 MD 초안이 생성된다.
- 최근 7일 기준 필터가 동작한다.
- URL 중복 제거가 동작한다.
- 카테고리 최소 4개 섹션으로 정리된다.
- `report.json`이 생성되고 수치가 일관된다.
- 동일 날짜 재실행 시 파일 충돌을 안전하게 처리한다.

## 19. 구현 순서
1. `sources.yml`, `category_rules.yml`, 템플릿 파일 생성
2. 수집기(피드 파서) 구현
3. 정규화/중복 제거/필터 구현
4. 분류/점수화/선택 구현
5. Markdown 렌더러 + report 생성 구현
6. `run_weekly_digest.sh` 래퍼 작성
7. 샘플 실행 및 수동 검증

## 20. Git 관리
- `jobs/data/` 디렉터리는 `.gitignore`에 추가 (캐시, 히스토리, 실행 기록은 로컬만 유지)
- `jobs/.venv/`도 `.gitignore`에 추가
- 커밋 대상: `weekly_digest.py`, `sources.yml`, `category_rules.yml`, `templates/`, `requirements.txt`, `run_weekly_digest.sh`
