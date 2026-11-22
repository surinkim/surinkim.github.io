---
name: weekly-digest
description: 숨김 주간 레이더(/pekr/)를 생성한다. Indie Radar(1인 개발·마이크로 SaaS·게임), 운영 사례 & 강좌(모니터링·운영), AI 엔지니어링 & 강좌(Anthropic·OpenAI 등 AI 블로그와 강좌) 3개 섹션의 후보를 수집하고 선정·한국어 요약해 _radar/ 마크다운으로 작성.
disable-model-invocation: false
allowed-tools: Bash Read Write Edit Grep Glob WebFetch AskUserQuestion
---

# 주간 다이제스트 생성

블로그 주인이 혼자 읽는 주간 레이더를 만든다. 공개 목록·RSS·sitemap에 나오지 않는 숨김 컬렉션(`_radar/`)에 쓰고, `https://corecode.pe.kr/pekr/`에서만 본다.

2026w47부터 바뀐 점: 테크 뉴스·도서·이번 주 pick 이미지를 뺐고(뉴스는 다른 일일 브리핑으로 받는다), 엔지니어링 섹션의 그림은 사용자가 요청할 때만 그린다. 2026w46까지의 `normal/_posts/*weekly-dev-links*` 글은 그대로 두되 메뉴에서는 숨겼다.

- **스크립트**(`jobs/weekly_radar.py`)는 넓게 수집하고 인기 신호(점수·순위·매출)만 붙인다.
- **Claude**는 후보 중에서 고르고, 원문을 확인한 뒤 요약을 쓴다.

섹션은 3개다.

1. 🚀 Indie Radar 최대 10개
2. 🛠️ 운영 사례 & 강좌 최대 5개 (모니터링·운영)
3. 🤖 AI 엔지니어링 & 강좌 최대 5개 (Anthropic·Claude 블로그, OpenAI 엔지니어링 글, AI 강좌 등)

개수는 상한이다(2026w47에 사용자가 정함: Indie는 10개까지 채우고, 강좌는 다 읽기 힘드니 섹션당 5개). 후보가 많으면 우선순위가 높은 것만 싣고, 모자라면 모인 만큼만 싣는다. 억지로 채우지 않는다.

## 1단계: 날짜 확인

가장 최근 주간 포스트의 날짜 범위로 이번 주 범위를 계산한다.

1. `_radar/`에서 가장 최신 파일을 찾는다. 비어 있으면 `normal/_posts/`의 `*weekly-dev-links*` 중 최신 파일을 쓴다
2. title에서 날짜 범위를 추출한다 (예: `11/15 ~ 11/21`, 예전 글은 `#2026 9/6 ~ 9/12`)
3. 종료일 다음 날을 새 시작일, 시작일 + 6일을 새 종료일로 한다

`AskUserQuestion`으로 확인받는다.
- 질문: "주간 레이더 생성 기간이 맞나요?"
- 옵션 1: "{시작일} ~ {종료일} 로 진행" (기본 추천)
- 옵션 2: "날짜 직접 입력"

## 2단계: 후보 수집

```bash
bash jobs/run_weekly_radar.sh --from {시작일} --to {종료일} --sections news,indie,observability 2>&1 | tee /tmp/weekly_radar_run.log | grep "weekly_radar"
```

- `news`는 포스트에 싣지 않지만 함께 수집한다. 엔지니어링 섹션의 `rss`·`ai_rss` 후보(Anthropic Engineering 등)가 뉴스 RSS 수집 결과에서 나오기 때문이다. `books`는 수집하지 않는다.

- 1분 안팎 걸린다. 히스토리 파일을 쓰지 않으므로 재실행해도 부작용이 없다.
- 결과는 `jobs/data/runs/{종료일}/`에 저장된다.
  - `radar_indie.md`, `radar_observability.md`: 쓰는 섹션 후보 (항목마다 `signals` 표시). `radar_news.md`는 참고용
  - `radar_candidates.json`: 전체 원본 데이터
- 로그의 `empty group` 경고를 확인한다. 한두 소스가 비어도 진행하되, 5단계 보고에 적는다.
  - `github releases failed` 경고는 GitHub API 호출 제한(비인증 시간당 60회) 때문일 수 있다. 스크립트는 `GITHUB_TOKEN` 환경 변수나 `gh auth token`을 자동으로 쓰므로, `gh auth status`로 로그인 상태를 확인한다.
  - Reddit(429), GeekNews(403)는 일시 차단일 수 있다. 몇 분 뒤 `--sections indie` 또는 `--sections news,observability`로 해당 섹션만 다시 수집한다. **이때 `--out-dir`를 별도 경로로 지정**해야 기존 결과를 덮어쓰지 않는다.
- 섹션 파일이 커서 Read가 잘리면 `offset`/`limit`으로 나눠 읽는다. 추측으로 채우지 않는다.

## 3단계: 선정

### 공통 규칙

- **원문 확인 필수:** 요약은 제목만 보고 쓰지 않는다. 선정한 항목마다 원문을 확인한다.
  - GeekNews 토픽 페이지(`news.hada.io/topic?id=`)는 한국어 요약이 있어 가장 빠르다.
  - aitimes 기사, 해외 원문은 `WebFetch`나 `curl`로 본문을 확인한다.
  - 원문을 확인할 수 없는 사실(가격, 수치, 인물 발언)은 쓰지 않는다.
- **직전 포스트와 중복 금지:** 직전 2개 주간 글(`_radar/`, 부족하면 `normal/_posts/*weekly-dev-links*`까지)에 나온 URL과 주제는 제외한다. TrustMRR, GitHub Trending은 매주 비슷한 항목이 올라오므로 특히 주의한다.

  ```bash
  for f in normal/_posts/*weekly-dev-links* _radar/*.md; do [ -f "$f" ] && echo "$(basename "$f") $f"; done | sort | tail -2 | cut -d' ' -f2 | xargs grep -hoE 'https?://[^)]+' | sort -u
  ```

### 🚀 Indie Radar 최대 10개

`radar_indie.md`에서 고른다. 1인 개발, 마이크로 SaaS, 앱, 게임, 오픈소스 중 **수익이 있거나, 인기가 높거나, 입소문이 난 것**을 고른다.

| 그룹 | 성격 | 신호 |
|---|---|---|
| `trustmrr_growth`, `trustmrr_growing_mrr` | 수익 인증 (Stripe 연동) | `mrr_usd`, `last30d_revenue_usd`, `growth_30d_pct` |
| `reddit_sideproject`, `reddit_saas` | 입소문, 수익 후기 | `feed_rank` (주간 top 순위) |
| `hn_show`, `geeknews_show` | 개발자 반응 | `hn_points`, `geeknews_points` |
| `github_trending` | 오픈소스 | `stars_this_week` |
| `producthunt`, `betalist` | 신규 제품 | 순위 신호 약함. 보조로만 쓴다 |
| `itch_new_popular` | 인디 게임 | 오래된 게임이 섞여 있으니 신작인지 확인한다 |

- 성격이 다른 것을 섞는다: 수익 사례, 입소문, 게임이나 웹 토이, 오픈소스가 한쪽으로 몰리지 않게 한다.
- **TrustMRR 주의:**
  - 이름이 `Stealth`, `Hidden Business`, `Private Venture`인 곳은 제외한다.
  - `description`은 창업자 본인 주장이다. 수치는 `signals` 값만 인용한다.
  - `mrr_usd`와 `last30d_revenue_usd`가 크게 어긋나는 곳(예: MRR은 큰데 30일 매출 0)은 피한다.
- Reddit 후기의 수익 수치는 "본인 공개"임을 전제로, 원문에 적힌 대로만 옮긴다.

### 🛠️ 엔지니어링 사례 & 강좌

`radar_observability.md`에서 고른다. 블로그 주인은 게임 서버 모니터링 시스템을 개발·운영한다. 스택은 Telegraf(수집) → Kafka(버퍼) → Mimir(저장), 메타데이터는 PostgreSQL, 언어는 Go·Java다. 주로 Go 웹 API를 개발하며 gin, huma 프레임워크를 쓴다. 쿠버네티스 위에서 Helm 차트와 오퍼레이터로 운영하고, Argo CD와 Rancher도 쓴다(직접 설치·운영하지는 않아 보안 이슈와 큰 변경 위주로 본다). 또 Grafana·Datadog·Prometheus·ELK 동향과 모니터링에 AI를 쓰는 방식에 관심이 많다.

| 그룹 | 내용 | 신호·참고 |
|---|---|---|
| `github_releases` | 주요 저장소의 이번 주 릴리스 (Telegraf, Mimir, Prometheus, Grafana, Loki, Alloy, Tempo, OTel Collector·Operator, Elasticsearch, Datadog Agent, gin, huma, Kubernetes, Helm, Prometheus Operator, k8s-monitoring-helm, Argo CD, Rancher) | `security=True`면 보안 패치, `prerelease=True`면 RC |
| `go_vulns` | Go 취약점 DB에서 이번 주 공개된 취약점 (표준 라이브러리, gin, huma, x/net, x/crypto, gRPC, protobuf, pgx, Kafka 클라이언트) | `fixed`는 인덱스 기준 첫 수정 버전이라 버전 라인별 수정 버전은 `https://vuln.go.dev/ID/{id}.json`의 `ranges`로 확인한다 |
| `vendor_blogs` | Grafana·Datadog·Elastic·OTel·Prometheus·InfluxData·Confluent·PostgreSQL·Go·Inside Java·Kubernetes·CNCF 블로그 | `source`에 출처와 날짜. 벤더 블로그는 홍보 글이 많으니 새 기능·변경이 있는 글만 고른다 |
| `kr_tech_blogs` | 국내 기술 블로그(토스, 우아한형제들, 카카오, NAVER D2, LY, 당근, 무신사, 올리브영, 데브시스터즈, NHN Cloud, 여기어때) 중 운영·관측성 키워드(`KR_BLOG_KEYWORDS`)에 걸린 글 | 장애 회고·실습형 글이 많아 이 섹션의 1순위 후보. 키워드 필터라 무관한 글도 섞인다 |
| `hn`, `geeknews`, `rss` | 뉴스 후보 중 모니터링 키워드에 걸린 글 | 키워드 필터라 무관한 글이 섞일 수 있다 |
| `ai_blogs` | AI 엔지니어링 블로그(OpenAI, Google Research, Hugging Face, LangChain, Simon Willison, Eugene Yan, Hamel Husain, Chip Huyen, Latent Space, Pragmatic Engineer) | OpenAI·Google Research·Simon Willison·Pragmatic Engineer는 `AI_ENG_KEYWORDS`로 거른다. 모델·제품 발표는 고르지 않는다 |
| `kr_ai_blogs` | 국내 기술 블로그 중 AI 활용·LLM 서비스 개발 글(`KR_AI_KEYWORDS`) | AI 쪽 1순위 후보 |
| `ai_hn`, `ai_geeknews`, `ai_rss` | 뉴스 후보 중 AI 용어(`AI_TERMS`)와 엔지니어링 표현(`AI_ENG_KEYWORDS`)이 함께 걸린 글 | Anthropic Engineering 블로그는 RSS가 없어 여기서 잡힌다. 무관한 글이 섞일 수 있다 |

- Apache Kafka는 GitHub 릴리스를 쓰지 않는다. Kafka 소식은 `confluent` 블로그와 HN·GeekNews에서 찾고, 릴리스 여부는 필요하면 https://kafka.apache.org/community/downloads/ 에서 확인한다.
- **목적은 학습이다.** 블로그 주인은 모니터링 분야의 깊은 지식이나 경험이 많지 않아, 이 섹션은 실력을 키우는 글 위주로 고른다. 대상 주제는 k8s, Grafana, Prometheus, Telegraf, Mimir, Kafka, Go와 모니터링 일반(지표 읽기, 알람 설계, 로그·트레이스, 장애 분석)이다.
- **운영과 AI를 섹션으로 나눈다.** 모니터링·운영 글은 🛠️ 운영 사례 & 강좌(최대 5개), AI 글은 🤖 AI 엔지니어링 & 강좌(최대 5개)에 싣는다. AI로 운영 문제를 푼 글(예: 성능 알림을 에이전트가 조사하는 시스템)은 AI 섹션에 둔다.
- **AI 엔지니어링 & 강좌 기준:** LLM 앱·에이전트를 만들고 운영하는 사례(평가, RAG, 컨텍스트·하네스 설계, 비용, LLM 관측성), 코딩 에이전트를 실무에 쓰는 방법, AI를 장애 분석·알람·운영에 쓰는 사례, 짧은 강좌·튜토리얼이 대상이다. 모델 출시, 벤치마크 순위, 투자 소식은 싣지 않는다.
  - Anthropic 글은 매주 직접 확인한다. 수집 스크립트에 피드가 없고 페이지가 JS로 그려져 `curl`로는 목록이 안 잡히므로, 내장 브라우저로 https://claude.com/blog (영문 글 링크는 `claude.dev/blog/...`)와 https://www.anthropic.com/engineering 을 열어 그 주 날짜 글을 찾는다. 본문은 `claude.dev/blog/...` 주소를 `curl`로 읽을 수 있다.
  - 강좌는 Anthropic Academy(https://anthropic.skilljar.com/)에 새 과정이 올라왔는지 본다. 날짜가 표시되지 않으니 직전 글에 없던 과정만 새 것으로 본다.
  - 2026w47 예: Claude Docs 출시 전 "chaos loop" 부하 테스트, Claude Code 팀의 검증 방식, OpenAI Performance Factory, Eugene Yan의 공개 벤치마크 분석.
- **운영 사례 & 강좌는 최대 5개, 사례와 짧은 강좌 위주:** 쓸 만한 글이 모자라면 모인 만큼만 싣고 억지로 채우지 않는다.
  - 우선: 실제 서비스의 운영·장애 사례(수치와 시행착오가 있는 글, 예: CNCF 블로그의 Atlassian 장애 감지 재구축), 개념을 풀어 주는 강좌·가이드(예: 그래프 읽는 법, 알람 설계), 바로 따라 해 볼 수 있는 실습형 글
  - 국내 기술 블로그의 장애 회고와 관측성 글은 `kr_tech_blogs` 그룹에서 먼저 찾는다. 피드를 추가하거나 빼려면 `weekly_radar.py`의 `KR_TECH_FEEDS`를 고친다.
  - 제외: 패치·마이너 릴리스, 보안 권고, 기능 발표 위주의 벤더 홍보 글. Go 메이저 버전이나 OpenTelemetry Go 자동 계측 v1처럼 직접 써 볼 만한 큰 변화만 예외로, "어떻게 써 보면 되는지" 중심으로 쓴다.
  - 벤더 특화 글(예: ES|QL, Datadog 전용 기능)은 개념이 다른 스택에도 통할 때만 고른다.
- **릴리스 체크 목록은 넣지 않는다.**
- 요약은 무엇을 배울 수 있는지가 드러나게 쓴다: 배경, 핵심 개념이나 원인, 해결 방법, 일반화할 수 있는 교훈.
- 뉴스성 소식이라도 모니터링 운영자에게 의미 있는 이야기(예: JDK 기본 GC 변경)나 AI를 만드는 방법에 가까운 이야기(예: 코딩 에이전트 팀의 코드 리뷰 방식)면 이 섹션에 싣는다.
- **한국어 요약은 필수다.** 영어 원문도 본문을 읽고 한국어로 요약한다.
- **그림은 기본으로 그리지 않는다.** 사용자가 특정 항목을 그려 달라고 할 때만 4단계 "그림 만들기"를 따라 SVG를 만들어 접기 영역으로 붙인다.

## 4단계: 포스트 작성

파일 경로는 `_radar/{종료일}-{YYYY}w{WW}.md`다. 결과 URL은 `/pekr/{종료일}-{YYYY}w{WW}/`이고, 목록은 `/pekr/`에 자동으로 나온다. 주차는 종료일 기준 ISO 주차를 쓴다(`date -j -f %Y-%m-%d {종료일} +%V`). 같은 파일이 이미 있으면 덮어쓰기 전에 사용자에게 확인한다.

### 형식

제목은 예전 "주간 테크/개발 뉴스"와 구분되게 `레이더 {YYYY}w{WW} · {M/D} ~ {M/D}` 형식으로 쓴다.

```markdown
---
title: "레이더 {YYYY}w{WW} · {M/D} ~ {M/D}"
date: {종료일}
---

- [🚀 Indie Radar ({개수})](#indie-radar)
- [🛠️ 운영 사례 & 강좌 ({개수})](#observability)
- [🤖 AI 엔지니어링 & 강좌 ({개수})](#ai-engineering)

---

## 🚀 Indie Radar
{: #indie-radar}

### [제품명](링크) · {종류} · {핵심 지표}

2~3문장. 뭘 만들었나, 왜 떴나, 수익이나 성장 수치.

---

## 🛠️ 운영 사례 & 강좌
{: #observability}

### [글 제목](원문 링크) (영어면 한국어 제목)

3~4문장 한국어 요약. 어떤 상황·문제였나, 핵심 개념이나 원인, 어떻게 풀었나, 다른 환경에도 통하는 교훈.

관련: [링크 이름](URL)

---

## 🤖 AI 엔지니어링 & 강좌
{: #ai-engineering}

### [글 제목](원문 링크) (영어면 한국어 제목)

(운영 섹션과 같은 형식)
```

- `layout: radar`, `noindex: true`, `comments: false`는 `_config.yml` 기본값으로 붙으니 front matter에 쓰지 않는다. `categories`·`tags`도 쓰지 않는다.
- 그림을 요청받으면 해당 항목 아래에 붙인다.

  ```markdown
  <details>
  <summary>그림으로 한눈에 보기</summary>
  <p><img src="/img/{YYYY_MM_DD}/{그림}.svg" alt="{그림 설명}"></p>
  </details>
  ```

### 작성 규칙

- **섹션 앵커는 고정:** `{: #indie-radar}`, `{: #observability}`, `{: #ai-engineering}`는 맨 위 바로가기 링크와 연결되므로 바꾸지 않는다.
- **영어 제목 번역:** 운영·AI 섹션의 제목이 영어면 링크 뒤에 괄호로 한국어 번역을 붙인다. 예: `### [How To Use Decision Models for Evals](URL) (평가(evals)에 decision model을 쓰는 법)`
- **제목 링크:** 운영·AI 섹션은 가장 신뢰할 만한 원문(공식 발표 > 원 보도 > 요약)을 건다. 보조 소스는 "관련:" 줄로 보낸다. 관련 링크가 없으면 "관련:" 줄을 생략한다.
- **본문 서식:** 제목 줄 외에는 볼드, 기울임 같은 인라인 강조를 넣지 않는다. 코드나 식별자 표기용 백틱은 써도 된다.
- **넣지 않는 것:**
  - 에디터 코멘트나 인용 블록(`> 💬 ...` 같은 "얘깃거리" 줄). 사용자가 댓글처럼 보인다며 뺀 형식이다.
  - 카테고리별 링크 목록, "이번 주 pick" 이미지와 링크 모음.
  - 블로그 주인의 직장이나 담당 업무를 유추할 수 있는 표현(예: "사내 모니터링에도 참고할 만합니다", "우리 스택"). 업무 맥락은 선정 기준으로만 쓰고, 본문은 "~를 쓰는 환경이라면"처럼 일반 독자를 향해 쓴다.
- **문체:** 존댓말(~습니다). 단순 번역이 아니라 맥락을 풀어 쓴다. 기술 용어와 제품명은 영문 그대로 둔다. 엔지니어링 섹션에서 SLO, SEV, 온콜, 기능 플래그처럼 운영 용어가 처음 나오면 괄호로 짧게 풀어 준다.

### 그림 만들기 (요청받았을 때만)

- 손으로 쓴 정적 SVG로 만든다. 블로그는 GitHub Pages가 빌드하므로 Mermaid나 `jekyll-graphviz`는 쓰지 않는다.
- 스타일은 ByteByteGo식 흐름도다(2026w46에서 확정, 예: `img/2026_11_14/grafana_watchers_cost.svg`). 정보가 빠져도 되니 그림만 보고 구조가 읽히게 한다.
  - 아이콘을 화살표로 잇는다: 시계(주기), DB 원통(데이터), `{ }` 상자(코드), 접힌 문서(계획·요약), 핀 달린 칩 "LLM"(모델·에이전트), 마름모(판단), 종(알림), 사람(검토), 알약 모양(PR·머지).
  - 단계마다 검은 원 번호 배지(1, 2, 3…)를 단다. 실패·재시도는 주홍 점선 화살표로 되돌린다.
  - 글자는 상자·아이콘 라벨 2~5단어와 아래 한 줄 설명만. 단계별 설명 글줄을 여러 열로 늘어놓지 않는다(본문에 맡긴다).
  - 핵심 수치는 맨 아래 점선 구분선 밑에 큰 숫자 두 개로 대비한다: 비교 대상은 회갈색 취소선, 개선값은 주홍.
- 공통 틀: `viewBox` 가로 760, 크림색 종이 카드(`#fffaf0`, `rx="10"`, 테두리 `#232323` 1.5px), 폰트 `-apple-system, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif`, 제목 17px 굵기 800, 부제는 생략.
- 색: 외곽선·글자 `#232323`, 보조 글자 `#5a5048`, 비교 대상 `#a39a90`. 채움은 역할별로 데이터·알림·태그 노랑 `#ffd166`, 코드·도구·검사기 하늘색 `#cfe3ff`, LLM·에이전트·강조 주홍 `#e8553a`, 나머지 흰색. 모든 도형에 먹색 외곽선을 둔다.
- 쓰지 않는 것: 청록(`#0f7b6c`)+회색 배색("너무 흔한 AI 배색", 2026w46), 외곽선 없는 파스텔 카드 그리드(2026w43), 설명 글줄 위주의 다열 배치와 축·눈금이 많은 막대 차트(2026w46 "너무 AI스럽다").
- 개념도로 단순화한 부분(예: 코어 위치)은 그림 안에 "개념도"라고 적는다.
- 그림 속 수치·시각·인원 같은 사실은 원문에 있는 값만 쓴다. 원문 두 수치로 계산한 값은 써도 되지만, 원문에 없는 순서나 시점을 지어내지 않는다. 그리기 전에 원문을 다시 읽어 순서와 조건을 확인한다(2026w42에서 여유 경고가 MemoryPressure보다 늦었는데 앞에 그렸다가 고친 일이 있다).
- 그린 뒤 브라우저로 열어 글자 겹침, 상자 밖으로 넘친 글자를 확인하고 고친다.
- 그림을 그리다 본문 요약의 틀린 점을 찾으면 본문도 함께 고친다.

작성 후 확인한다.

```bash
f=_radar/{파일명}
grep -n '{: #' $f                              # 앵커 3개
grep -c '^### ' $f                              # Indie + 운영 + AI 항목 수
grep -n '💬' $f                                 # 출력 없어야 정상
awk '/^### /{next} {print}' $f | grep -oE '\*\*[^*]+\*\*'   # 본문 볼드 없어야 정상
```

로컬에서 렌더링을 확인한다. 사용자가 보통 `jekyll serve .`를 4000번 포트로 띄워 두므로 `http://localhost:4000/pekr/{종료일}-{YYYY}w{WW}/`와 목록 `http://localhost:4000/pekr/`를 연다. 브라우저 캐시 때문에 예전 CSS나 이미지가 보이면 `?v=숫자`를 붙여 다시 연다. 직접 빌드할 때는 `LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8`를 꼭 붙인다. 없으면 SCSS 변환이 `Invalid US-ASCII character`로 실패한다.

## 5단계: VS Code로 작업 폴더 열기

```bash
code /Users/kimhyunukkim/work/surinkim.github.io
```

## 6단계: 결과 보고

사용자에게 다음을 보고한다.
- 생성된 파일 경로
- 수집 통계와 실패하거나 빈 소스
- 섹션별 선정 항목 (제목만 짧게)
- 볼 주소: `https://corecode.pe.kr/pekr/`
- 커밋 & 푸시 여부를 묻는다
