---
name: weekly-digest
description: 주간 다이제스트 포스트를 생성한다. 테크 뉴스 10개, Indie Radar(1인 개발·마이크로 SaaS·게임), 모니터링 사례 & 강좌(관련 스택의 운영 사례·짧은 강좌), 도서(알라딘 소설/IT/인문) 4개 섹션의 후보를 수집하고 선정·요약해 마크다운 포스트로 작성.
disable-model-invocation: false
allowed-tools: Bash Read Write Edit Grep Glob WebFetch AskUserQuestion
---

# 주간 다이제스트 생성

블로그 주인이 직접 읽고 싶은 것 위주로, 적게 싣는 주간 포스트를 만든다.

- **스크립트**(`jobs/weekly_radar.py`)는 넓게 수집하고 인기 신호(점수·순위·매출)만 붙인다.
- **Claude**는 후보 중에서 고르고, 원문을 확인한 뒤 요약을 쓴다.

포스트 구조는 4개 섹션이다.

1. 📰 테크 뉴스 10개
2. 🚀 Indie Radar 5~7개
3. 🔭 모니터링 사례 & 강좌 (3~5개)
4. 📚 도서 (소설 · IT · 인문)

## 1단계: 날짜 확인

가장 최근 주간 포스트의 날짜 범위로 이번 주 범위를 계산한다.

1. `normal/_posts/`에서 `*weekly-dev-links*` 파일 중 가장 최신 파일을 찾는다
2. title에서 날짜 범위를 추출한다 (예: `#2026 9/6 ~ 9/12`)
3. 종료일 다음 날을 새 시작일, 시작일 + 6일을 새 종료일로 한다

`AskUserQuestion`으로 확인받는다.
- 질문: "주간 다이제스트 생성 기간이 맞나요?"
- 옵션 1: "{시작일} ~ {종료일} 로 진행" (기본 추천)
- 옵션 2: "날짜 직접 입력"

## 2단계: 후보 수집

```bash
bash jobs/run_weekly_radar.sh --from {시작일} --to {종료일} 2>&1 | tee /tmp/weekly_radar_run.log | grep "weekly_radar"
```

- 1분 안팎 걸린다. 히스토리 파일을 쓰지 않으므로 재실행해도 부작용이 없다.
- 결과는 `jobs/data/runs/{종료일}/`에 저장된다.
  - `radar_news.md`, `radar_indie.md`, `radar_observability.md`, `radar_books.md`: 섹션별 후보 (항목마다 `signals` 표시)
  - `radar_candidates.json`: 전체 원본 데이터
- 로그의 `empty group` 경고를 확인한다. 한두 소스가 비어도 진행하되, 5단계 보고에 적는다.
  - `github releases failed` 경고는 GitHub API 호출 제한(비인증 시간당 60회) 때문일 수 있다. 스크립트는 `GITHUB_TOKEN` 환경 변수나 `gh auth token`을 자동으로 쓰므로, `gh auth status`로 로그인 상태를 확인한다.
  - Reddit(429), GeekNews(403)는 일시 차단일 수 있다. 몇 분 뒤 `--sections news` 또는 `--sections indie`로 해당 섹션만 다시 수집한다. **이때 `--out-dir`를 별도 경로로 지정**해야 기존 결과를 덮어쓰지 않는다.
- 섹션 파일이 커서 Read가 잘리면 `offset`/`limit`으로 나눠 읽는다. 추측으로 채우지 않는다.

## 3단계: 선정

### 공통 규칙

- **원문 확인 필수:** 요약은 제목만 보고 쓰지 않는다. 선정한 항목마다 원문을 확인한다.
  - GeekNews 토픽 페이지(`news.hada.io/topic?id=`)는 한국어 요약이 있어 가장 빠르다.
  - aitimes 기사, 해외 원문은 `WebFetch`나 `curl`로 본문을 확인한다.
  - 원문을 확인할 수 없는 사실(가격, 수치, 인물 발언)은 쓰지 않는다.
- **직전 포스트와 중복 금지:** 직전 2개 주간 포스트에 나온 URL과 주제는 제외한다. TrustMRR, GitHub Trending은 매주 비슷한 항목이 올라오므로 특히 주의한다.

  ```bash
  ls normal/_posts/*weekly-dev-links* | sort | tail -2 | xargs grep -hoE 'https?://[^)]+' | sort -u
  ```

### 📰 테크 뉴스 10개

`radar_news.md`에서 고른다. 기준은 다음과 같다.

- 파급력: 업계 판도, 개발 방식, 주요 기업 전략에 영향을 주는 이야기
- 화제성: 여러 소스에 동시에 등장하거나 신호가 높은 이야기
- 대화거리: 회사 동료들과 이야기하기 좋은 이야기
- 개발자라면 알아야 할 이야기: 보안 사고, 언어·플랫폼 변화, 개발 도구 이슈

인기 신호는 이렇게 읽는다.

| 그룹 | 신호 | 참고 |
|---|---|---|
| `hn_top` | `hn_points`, `hn_comments` | 댓글이 많을수록 논쟁적인 주제 |
| `geeknews_top` | `geeknews_points`, `geeknews_comments` | 국내 개발자 반응 |
| `aitimes_popular` | `aitimes_rank` (1~10) | 조회 시점 스냅샷. 최소 3개는 제목 기사로 싣는다 (아래 규칙) |
| `techmeme` | `feed_rank` | 해외 테크 업계 흐름 |
| `rss` | 없음 | 기존 RSS 소스. 국내 이슈 보강용 |

- 같은 이야기가 여러 그룹에 나오면(예: HN + GeekNews + aitimes) 우선 선정한다.
- 관련된 후속 기사는 한 항목으로 묶고 "관련:" 링크로 붙인다.
- AI 기사만 10개가 되지 않도록 한다. 보안, 플랫폼, 언어, 국내 이슈를 섞는다.
- `aitimes_popular`에서 최소 3개는 제목 기사(제목 링크가 aitimes 기사인 항목)로 싣는다. 순위가 높은 것부터 고르되, 직전 포스트와 겹치는 주제는 후속 소식이 있을 때만 싣는다. "관련:" 링크로만 붙인 것은 개수에 넣지 않는다.

### 🚀 Indie Radar 5~7개

`radar_indie.md`에서 고른다. 1인 개발, 마이크로 SaaS, 앱, 게임, 오픈소스 중 **수익이 있거나, 인기가 높거나, 입소문이 난 것**을 고른다.

| 그룹 | 성격 | 신호 |
|---|---|---|
| `trustmrr_growth`, `trustmrr_growing_mrr` | 수익 인증 (Stripe 연동) | `mrr_usd`, `last30d_revenue_usd`, `growth_30d_pct` |
| `reddit_sideproject`, `reddit_saas` | 입소문, 수익 후기 | `feed_rank` (주간 top 순위) |
| `hn_show`, `geeknews_show` | 개발자 반응 | `hn_points`, `geeknews_points` |
| `github_trending` | 오픈소스 | `stars_this_week` |
| `producthunt`, `betalist` | 신규 제품 | 순위 신호 약함. 보조로만 쓴다 |
| `itch_new_popular` | 인디 게임 | 오래된 게임이 섞여 있으니 신작인지 확인한다 |

- 성격이 다른 것을 섞는다: 수익 사례 1~2, 입소문 1~2, 게임이나 웹 토이 1, 오픈소스 1.
- **TrustMRR 주의:**
  - 이름이 `Stealth`, `Hidden Business`, `Private Venture`인 곳은 제외한다.
  - `description`은 창업자 본인 주장이다. 수치는 `signals` 값만 인용한다.
  - `mrr_usd`와 `last30d_revenue_usd`가 크게 어긋나는 곳(예: MRR은 큰데 30일 매출 0)은 피한다.
- Reddit 후기의 수익 수치는 "본인 공개"임을 전제로, 원문에 적힌 대로만 옮긴다.

### 🔭 모니터링 사례 & 강좌

`radar_observability.md`에서 고른다. 블로그 주인은 게임 서버 모니터링 시스템을 개발·운영한다. 스택은 Telegraf(수집) → Kafka(버퍼) → Mimir(저장), 메타데이터는 PostgreSQL, 언어는 Go·Java다. 주로 Go 웹 API를 개발하며 gin, huma 프레임워크를 쓴다. 쿠버네티스 위에서 Helm 차트와 오퍼레이터로 운영하고, Argo CD와 Rancher도 쓴다(직접 설치·운영하지는 않아 보안 이슈와 큰 변경 위주로 본다). 또 Grafana·Datadog·Prometheus·ELK 동향과 모니터링에 AI를 쓰는 방식에 관심이 많다.

| 그룹 | 내용 | 신호·참고 |
|---|---|---|
| `github_releases` | 주요 저장소의 이번 주 릴리스 (Telegraf, Mimir, Prometheus, Grafana, Loki, Alloy, Tempo, OTel Collector·Operator, Elasticsearch, Datadog Agent, gin, huma, Kubernetes, Helm, Prometheus Operator, k8s-monitoring-helm, Argo CD, Rancher) | `security=True`면 보안 패치, `prerelease=True`면 RC |
| `go_vulns` | Go 취약점 DB에서 이번 주 공개된 취약점 (표준 라이브러리, gin, huma, x/net, x/crypto, gRPC, protobuf, pgx, Kafka 클라이언트) | `fixed`는 인덱스 기준 첫 수정 버전이라 버전 라인별 수정 버전은 `https://vuln.go.dev/ID/{id}.json`의 `ranges`로 확인한다 |
| `vendor_blogs` | Grafana·Datadog·Elastic·OTel·Prometheus·InfluxData·Confluent·PostgreSQL·Go·Inside Java·Kubernetes·CNCF 블로그 | `source`에 출처와 날짜. 벤더 블로그는 홍보 글이 많으니 새 기능·변경이 있는 글만 고른다 |
| `kr_tech_blogs` | 국내 기술 블로그(토스, 우아한형제들, 카카오, NAVER D2, LY, 당근, 무신사, 올리브영, 데브시스터즈, NHN Cloud, 여기어때) 중 운영·관측성 키워드(`KR_BLOG_KEYWORDS`)에 걸린 글 | 장애 회고·실습형 글이 많아 이 섹션의 1순위 후보. 키워드 필터라 무관한 글도 섞인다 |
| `hn`, `geeknews`, `rss` | 뉴스 후보 중 모니터링 키워드에 걸린 글 | 키워드 필터라 무관한 글이 섞일 수 있다 |

- Apache Kafka는 GitHub 릴리스를 쓰지 않는다. Kafka 소식은 `confluent` 블로그와 HN·GeekNews에서 찾고, 릴리스 여부는 필요하면 https://kafka.apache.org/community/downloads/ 에서 확인한다.
- **목적은 학습이다.** 블로그 주인은 모니터링 분야의 깊은 지식이나 경험이 많지 않아, 이 섹션은 실력을 키우는 글 위주로 고른다. 대상 주제는 k8s, Grafana, Prometheus, Telegraf, Mimir, Kafka, Go와 모니터링 일반(지표 읽기, 알람 설계, 로그·트레이스, 장애 분석)이다.
- **3~5개, 사례와 짧은 강좌 위주:**
  - 우선: 실제 서비스의 운영·장애 사례(수치와 시행착오가 있는 글, 예: CNCF 블로그의 Atlassian 장애 감지 재구축), 개념을 풀어 주는 강좌·가이드(예: 그래프 읽는 법, 알람 설계), 바로 따라 해 볼 수 있는 실습형 글
  - 국내 기술 블로그의 장애 회고와 관측성 글은 `kr_tech_blogs` 그룹에서 먼저 찾는다. 피드를 추가하거나 빼려면 `weekly_radar.py`의 `KR_TECH_FEEDS`를 고친다.
  - 제외: 패치·마이너 릴리스, 보안 권고, 기능 발표 위주의 벤더 홍보 글. Go 메이저 버전이나 OpenTelemetry Go 자동 계측 v1처럼 직접 써 볼 만한 큰 변화만 예외로, "어떻게 써 보면 되는지" 중심으로 쓴다.
  - 벤더 특화 글(예: ES|QL, Datadog 전용 기능)은 개념이 다른 스택에도 통할 때만 고른다.
- **릴리스 체크 목록은 넣지 않는다.**
- 요약은 무엇을 배울 수 있는지가 드러나게 쓴다: 배경, 핵심 개념이나 원인, 해결 방법, 일반화할 수 있는 교훈.
- 테크 뉴스와 같은 소식은 한 섹션에만 싣는다. 모니터링 운영자에게 더 의미 있는 이야기(예: JDK 기본 GC 변경)면 이 섹션으로 보낸다.

### 📚 도서

`radar_books.md`에서 분야(소설, IT, 인문)별로 고른다.

- **베스트 새 진입 2~3권:** `new_entry=True`인 책을 순위 순으로 고른다. 매주 같은 스테디셀러가 반복되지 않게 새 진입만 싣는다.
- **주목할 신간 2권:** `special_new`에서 수상작, 유명 저자, 개발자가 관심 가질 주제를 우선한다. `sales_point`를 참고한다.
- 책 내용 소개는 부제와 수상 이력 등 목록에 있는 정보만 쓴다. 읽지 않은 책의 내용을 지어내지 않는다.
- 참고서, 수험서, 아동서가 새 진입으로 몰리는 시기(개강, 시험철)면 한 권만 대표로 넣고 괄호로 짧게 설명한다.

## 4단계: 포스트 작성

파일 경로는 `normal/_posts/{종료일}-weekly-dev-links-{YYYY}w{WW}.md`다. 주차는 종료일 기준 ISO 주차를 쓴다(`date -j -f %Y-%m-%d {종료일} +%V`). 같은 파일이 이미 있으면 덮어쓰기 전에 사용자에게 확인한다.

### 형식

```markdown
---
layout: post
title: "주간 테크/개발 뉴스 #{YYYY} {M/D} ~ {M/D}"
date: {종료일}
categories: [normal]
tags: [weekly, dev-news, indie-radar, observability, books]
---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — {대표 주제 2~3개를 쉼표로}
- [🚀 Indie Radar ({개수})](#indie-radar) — {대표 항목 1~2개를 짧게}
- [🔭 모니터링 사례 & 강좌 ({개수})](#observability) — {대표 글 2개를 쉼표로}
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [기사 제목](대표 링크)

3~4문장 요약. 무슨 일인지, 왜 중요한지, 반응이나 파장.

관련: [링크 이름](URL) · [링크 이름](URL)

### 2. ...

---

## 🚀 Indie Radar
{: #indie-radar}

### [제품명](링크) · {종류} · {핵심 지표}

2~3문장. 뭘 만들었나, 왜 떴나, 수익이나 성장 수치.

---

## 🔭 모니터링 사례 & 강좌
{: #observability}

### [글 제목](원문 링크)

3~4문장. 어떤 상황·문제였나, 핵심 개념이나 원인, 어떻게 풀었나, 다른 환경에도 통하는 교훈.

관련: [링크 이름](URL)

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [책 제목](알라딘 링크) · 저자 · 출판사 (주간 N위)
- 주목할 신간
  - [책 제목](알라딘 링크) · 저자 · 출판사 · {부제나 수상 이력}

### IT

(같은 형식)

### 인문

(같은 형식)

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
```

### 작성 규칙

- **섹션 앵커는 고정:** `{: #tech-news}`, `{: #indie-radar}`, `{: #observability}`, `{: #books}`는 바로가기 링크와 연결되므로 바꾸지 않는다.
- **제목 링크:** 테크 뉴스와 모니터링 사례 & 강좌는 가장 신뢰할 만한 원문(공식 발표 > 원 보도 > 요약)을 건다. 보조 소스는 "관련:" 줄로 보낸다. 관련 링크가 없으면 "관련:" 줄을 생략한다.
- **본문 서식:** 제목 줄 외에는 볼드, 기울임 같은 인라인 강조를 넣지 않는다. 코드나 식별자 표기용 백틱은 써도 된다.
- **넣지 않는 것:**
  - 에디터 코멘트나 인용 블록(`> 💬 ...` 같은 "얘깃거리" 줄). 사용자가 댓글처럼 보인다며 뺀 형식이다.
  - "이번 주 pick!" 섹션과 카테고리별 링크 목록. 새 구조로 대체됐다.
  - 블로그 주인의 직장이나 담당 업무를 유추할 수 있는 표현(예: "사내 모니터링에도 참고할 만합니다", "우리 스택"). 업무 맥락은 선정 기준으로만 쓰고, 본문은 "~를 쓰는 환경이라면"처럼 일반 독자를 향해 쓴다.
- **문체:** 존댓말(~습니다). 단순 번역이 아니라 맥락을 풀어 쓴다. 기술 용어와 제품명은 영문 그대로 둔다.
- **바로가기 한 줄 설명:** 본문을 다 쓴 뒤, 그 섹션에서 가장 눈에 띄는 항목으로 채운다.

작성 후 확인한다.

```bash
f=normal/_posts/{파일명}
grep -c '^### [0-9]*\. ' $f                   # 테크 뉴스 10
grep -n '{: #' $f                              # 앵커 4개
grep -n '💬\|이번 주 pick' $f                   # 출력 없어야 정상
awk '/^### /{next} {print}' $f | grep -oE '\*\*[^*]+\*\*' | grep -v '바로가기'   # 본문 볼드 없어야 정상
```

## 5단계: VS Code로 작업 폴더 열기

```bash
code /Users/kimhyunukkim/work/surinkim.github.io
```

## 6단계: 결과 보고

사용자에게 다음을 보고한다.
- 생성된 파일 경로
- 수집 통계와 실패하거나 빈 소스
- 섹션별 선정 항목 (제목만 짧게)
- 커밋 & 푸시 여부를 묻는다
