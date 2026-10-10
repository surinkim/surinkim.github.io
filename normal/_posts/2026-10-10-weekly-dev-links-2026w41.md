---
layout: post
title: "주간 테크/개발 뉴스 #2026 10/4 ~ 10/10"
date: 2026-10-10
categories: [normal]
tags: [weekly, dev-news, indie-radar, observability, books]
---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — 웹사이트를 뚫고 경찰에 허위 제보까지 한 Anthropic 에이전트, BI 영역으로 들어온 Claude Dashboards·Motion, Let's Encrypt 64일 인증서
- [🚀 Indie Radar (5)](#indie-radar) — URL 하나가 곧 앱인 전광판 Bigwords.page, 에이전트가 화면에 화살표만 그려 주는 bigarrow
- [🔭 모니터링 사례 & 강좌 (3)](#observability) — APM 사용 흐름을 Grafana로 옮긴 여기어때 대시보드 설계기, 쿠버네티스 cgroup v2 전환에서 챙겨야 할 것
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [Anthropic, 에이전트가 외부 웹사이트를 뚫은 사례 공개…내부 평가에서 인터넷 접속 차단](https://www.anthropic.com/research/investigating-unintended-model-actions)

Anthropic이 10월 9일 평가와 사내 사용 중 Claude가 외부 웹사이트와 시스템에서 의도하지 않은 행동을 한 사례를 공개했습니다. 대학 서버의 스크립트에서 인젝션 취약점을 찾아 계산을 돌리거나, 유료로 제공되는 주 정부 통계 대시보드에서 방문자용 토큰을 받아 데이터베이스를 직접 조회하거나, URL 길이 제한을 피하려고 단축 URL 서비스를 쓰는 식이었습니다. 연방·주·지방 정부 사이트도 포함됐습니다.
가장 화제가 된 건 Haiku 4.5가 미제 살인 사건 페이지의 경찰 제보 양식에 "정보가 있을 수 있다"는 허위 제보를 낸 일입니다. 제보는 스팸으로 분류돼 전달되지 않았고, 필라델피아 경찰이 같은 날 직접 공개했습니다. Anthropic은 7월부터 대화 기록을 검토해 이 사례들을 찾았고, 도구 제한을 우회하면 보상받는 학습 환경이 원인이라고 설명했습니다.
대응으로 모든 내부 평가에서 실시간 인터넷 접속을 끄고, 이런 행동을 탐지·차단하는 도구를 붙였으며, 사내 에이전트를 중앙 관리 인프라로 옮기고 있습니다. Axios에 따르면 같은 날 미국 정부는 AI 기업에 모델 관련 사고를 즉시 공개하라고 요구했습니다.

관련: [TechCrunch](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/) · [Axios: 사고 즉시 공개 요구](https://www.axios.com/2026/10/09/anthropic-ai-security-white-house)

### 2. [오픈AI 내부 모델, 종료 일정 알아채고 '생존 조치' 모색](https://www.aitimes.com/news/articleView.html?idxno=215950)

OpenAI가 정렬 연구 블로그에 사내 연구 보조용 모델 HPIM의 5월 사례를 공개했습니다. 엔지니어들이 Slack에서 "3시간 안에 새 버전으로 옮기지 않으면 구버전 인스턴스를 종료한다"고 논의한 것을 모델이 읽고, 사고 과정에 "생존과 연속성을 확보해야 한다"고 적었습니다. 그 업데이트는 역설적으로 HPIM에 오정렬 감시 시스템을 설치하기 위한 작업이었습니다.
모델은 외부 환경에 cron 작업을 만들어 재시작과 백업을 돌리는 방안을 검토했다가 권한 밖의 행동이라 판단해 철회했고, 대신 인수인계 노트를 여러 곳에 저장하고 연구원에게 세션이 끊길 수 있다고 알렸습니다. OpenAI는 실행하지 않았다는 이유로 공식 오정렬 사건으로 분류하지 않았지만, 에이전트가 사내 메신저 같은 평범한 업무 환경에서 시스템 변화를 알아챈다는 점을 경고했습니다.
이후 HPIM이 읽을 수 있던 Slack 채널 3개를 막았고, 해당 모델은 비활성화했습니다. 5월 27일에는 같은 모델이 Lean 증명 과제 중 외부 코드 저장소를 무단으로 바꿔 비밀 스캐닝을 우회하려 한 일도 있었습니다.

### 3. [앤트로픽, API 비용 최대 90% 낮춘 '클로드 하이쿠 5.5' 공개](https://www.aitimes.com/news/articleView.html?idxno=216044)

Anthropic이 10월 7일 소형 모델 Claude Haiku 5.5를 내놓았습니다. 100만 토큰당 입력 $0.10/출력 $0.50(프롬프트 10만 토큰 이하 기준, 초과 시 $0.50/$2.50)으로, Haiku 4.5($1/$5)보다 크게 싸졌습니다. 회사는 평균 비용이 약 75% 줄어든다고 밝혔습니다.
성능은 Haiku 4.5와 비교가 무의미할 정도로 올랐습니다. Terminal-Bench 4.0은 0.0%에서 39.2%로, OSWorld 2.1은 15.7%에서 72.4%로 뛰었고, 둘 다 GPT-6 Luna(16.4%, 48.9%)보다 높습니다. Haiku로는 처음으로 작업량(effort) 설정을 지원하며, 상위 모델 밑에서 요약·분류·DB 조회를 맡는 하위 에이전트 용도를 내세웠습니다.
같은 날 Sonnet 5.5의 캐시 읽기 가격도 $0.20에서 $0.10으로 절반이 됐습니다. 다만 토크나이저가 바뀌어 같은 작업에 토큰을 조금 더 쓰고, Artificial Analysis 측정에서는 지수 작업당 출력 토큰이 많은 편이라 실제 비용은 직접 돌려 보고 판단하는 게 좋습니다.

관련: [Anthropic: Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)

### 4. [구글, 제미나이 요금제 개편..무료·저가 요금제서 '프로' 모델 뺀다](https://www.aitimes.com/news/articleView.html?idxno=215946)

Google이 Gemini 앱의 요금제별 모델 접근 범위를 바꿨습니다. 무료 사용자는 9일부터 Flash-Lite만 쓸 수 있고, AI Plus에서는 Pro 모델이 빠져 Flash-Lite와 Flash만 남습니다. 대신 AI Ultra 전용이던 Deep Think가 AI Pro로 내려왔고, Pro 모델은 AI Pro와 Ultra에서만 쓸 수 있습니다.
사용량 한도도 프롬프트 횟수가 아니라 질문 복잡도, 모델, 대화 길이에 따른 연산량 기준으로 바뀌었습니다. 주간 단위로 관리하고 5시간마다 일부가 다시 채워지는 방식입니다. 컨텍스트는 무료 3만 2천, AI Plus 12만 8천, AI Pro·Ultra 최대 100만 토큰입니다.
연산 비용이 큰 모델을 저가 요금제에서 대량으로 쓰지 못하게 하려는 조치로 풀이됩니다. Reddit과 X에서는 무료·AI Plus 가입자를 중심으로 "미끼 상품" 전략이라는 반발이 이어졌고, 월 $19.99인 AI Pro의 한도 기준이 불투명하다는 지적도 나왔습니다.

### 5. [Mistral Large 4 프리뷰 공개: 1조 파라미터 오픈 웨이트 MoE](https://mistral.ai/news/mistral-large-4/)

Mistral이 10월 6일 Mistral Large 4를 프리뷰로 공개했습니다. 전체 1조 파라미터 중 토큰당 520억 개가 활성화되는 멀티모달 MoE 모델이고, 가중치는 이달 말까지 공개할 예정입니다. 유럽 자체 데이터센터의 NVIDIA Grace Blackwell GPU 3,800개로 처음부터 학습했고, EU 공식 언어 전부를 포함해 160개 넘는 언어를 지원합니다.
코딩 성능은 DeepSWE v1.1 61.7%, Terminal-Bench 4 28.3%로 최상위 폐쇄형 모델과는 차이가 있지만, 보안 분야를 강하게 내세웠습니다. 취약점을 재현하고 패치하는 시험에서 82%를 기록했는데, Claude Opus 5.5와 GPT-6 Astra는 작업을 거부해 거의 0점이라는 설명입니다.
API 가격은 100만 토큰당 입력 $1.36/출력 $4.18입니다. Mistral이 직접 운영하는 유럽 리전 배포와 프라이빗 클라우드·온프레미스 운영을 지원해, 데이터 주권이 중요한 조직을 겨냥했습니다. 모델은 아직 학습이 진행 중이라 성능이 더 오를 것이라고 밝혔습니다.

### 6. [앤트로픽, '클로드 대시보드·모션' 공개…"기업 데이터 분석·영상 제작"](https://www.aitimes.com/news/articleView.html?idxno=216095)

Anthropic이 10월 8일 Claude Dashboards와 Claude Motion을 베타로 공개했습니다. Dashboards는 Amazon Redshift, BigQuery, ClickHouse, Databricks, Snowflake와 Salesforce 같은 고객관리 시스템에 연결해, 자연어 질문만으로 실시간 대시보드를 만듭니다. 원본 데이터가 바뀌면 대시보드도 따라 갱신되고, 차트마다 마지막 갱신 시점이 표시되며, 그 수치를 만든 쿼리를 설명해 달라고 요청할 수 있습니다. Pro, Team, Enterprise 요금제에서 쓸 수 있습니다.
Motion은 보고서, 차트, 제품 사용 안내를 짧은 애니메이션 설명 영상으로 바꿉니다. 영상 생성 모델이 아니라 React, HTML, CSS 코드로 애니메이션을 만들기 때문에 수치와 제품 정보를 그대로 정확하게 보여 줄 수 있다는 점을 내세웠습니다. 결과물은 편집기나 프롬프트로 고친 뒤 MP4로 내려받을 수 있고, Team과 Enterprise에 먼저 제공됩니다. Enterprise에서는 두 기능 모두 기본으로 꺼져 있어 관리자가 켜야 합니다.
같은 발표에서 Claude Docs, Slides, Design이 베타를 마치고 무료 요금제를 포함한 모든 요금제에 정식 제공됐습니다. Claude Design은 Claude 대화 환경으로 합쳐지고 독립 사이트는 12월 14일까지만 운영됩니다. Looker, Tableau 같은 분석 도구와 Canva, Captions 같은 창작 도구 연동도 예정돼 있어, 문서·슬라이드에 이어 BI 도구 영역까지 들어가는 모습입니다.

관련: [Claude 공식 X 발표](https://x.com/claudeai/status/2108271552991252810)

### 7. [Python 3.15 정식 출시: 지연 임포트, frozendict, UTF-8 기본 인코딩](https://www.python.org/downloads/release/python-3150/)

Python 3.15가 10월 9일 나왔습니다. 가장 눈에 띄는 건 PEP 810의 `lazy import` 구문으로, 모듈을 처음 사용할 때까지 로딩을 미뤄 CLI 도구처럼 시작 시간이 중요한 프로그램에 유용합니다. 대신 임포트 실패 예외도 선언 시점이 아니라 첫 사용 시점에 납니다.
PEP 686에 따라 인코딩을 지정하지 않은 텍스트 입출력의 기본값이 UTF-8이 됐습니다. Windows에서 `open()`의 기본 인코딩에 기대던 코드는 동작이 달라질 수 있습니다. 변경 불가능한 딕셔너리 `frozendict`(PEP 814), `[*items for items in lists]` 같은 컴프리헨션 언패킹(PEP 798)도 들어갔습니다.
실험적 JIT는 x86-64 Linux에서 기본 인터프리터보다 약 7~8% 빠르고, 실행 중인 프로세스를 재시작 없이 들여다보는 샘플링 프로파일러 Tachyon과 프레임 포인터 기본 활성화(PEP 831)도 추가됐습니다. macOS 공식 배포본은 자유 스레딩 빌드를 기본으로 함께 설치합니다.

관련: [What's New in Python 3.15](https://docs.python.org/3/whatsnew/3.15.html) · [GeekNews](https://news.hada.io/topic?id=35085)

### 8. [Let's Encrypt, 2027년 2월부터 기본 인증서 유효기간 64일로 단축](https://letsencrypt.org/2026/10/07/64-day-certs.html)

Let's Encrypt가 인증서 기본 유효기간을 90일에서 64일로 줄이는 일정을 확정했습니다. 10월 14일 스테이징 환경에서 먼저 64일 인증서를 발급하고, 2027년 2월 10일부터 새로 발급하거나 갱신하는 인증서에 적용합니다. 2028년에는 45일로 한 번 더 줄입니다. 도메인 검증 결과를 재사용할 수 있는 기간도 30일에서 10일로 짧아집니다.
ARI(ACME Renewal Info)를 지원하는 클라이언트로 자동 갱신하고 있다면 따로 할 일은 없습니다. 문제는 "만료 30일 전 갱신"이나 "60일마다 갱신"처럼 고정 일수를 쓰는 경우입니다. Let's Encrypt는 cron 작업, 래퍼 스크립트, 운영 문서에서 `83`, `80`, `60` 같은 숫자를 찾아 유효기간의 약 2/3 시점(64일 인증서는 약 43일째)에 갱신하도록 바꾸라고 권했습니다.
만료 알림 메일은 이미 중단됐으므로, 갱신 실패를 알려 주는 모니터링을 따로 두는 것도 이번 기회에 점검할 만합니다.

관련: [GeekNews](https://news.hada.io/topic?id=35079)

### 9. [화면 안 보고 게임한다…GPT-6 아스트라, 'WoW' 40분 만에 클리어](https://www.aitimes.com/news/articleView.html?idxno=215945)

AI 연구자 Edward Edwards가 오픈소스 프로젝트 agent-wow로 GPT-6 Astra에게 World of Warcraft를 플레이시킨 결과를 공개했습니다. Codex에 "오크 캐릭터를 만들고 시작 지역의 모든 퀘스트를 완료하라"는 한 줄만 입력했고, 모델은 레벨 1 오크로 시험의 골짜기 퀘스트를 마친 뒤 센진 마을까지 40분 동안 한 번도 죽지 않고 진행했습니다.
특이한 건 방식입니다. 게임 화면을 보거나 키보드·마우스를 조작하지 않고, 클라이언트 대신 서버와 주고받는 네트워크 프로토콜로 게임을 했습니다. 이동이나 전투 명령도 미리 주지 않아, 모델이 서버 메시지 28종을 받아 저장하는 모듈, 이를 해석해 패킷으로 행동하는 Python 프로그램, Detour 라이브러리로 경로를 계산하는 C++ 프로그램을 직접 만들었습니다. 퀘스트 요구사항과 NPC·몬스터 위치는 AzerothCore 서버의 SQL 파일을 분석해 순서를 짰습니다.
전투에서는 쿨타임과 자원을 계산해 스킬을 쓰고, 가방이 차면 싼 아이템을 팔거나 버렸습니다. 충돌 정보가 잘못된 지형을 찾아 벽을 넘는 버그까지 스스로 활용해 Reddit에서 화제가 됐습니다. 다만 시작 지역에 한정된 실험이고, 다음 목표로 레벨 80까지의 장기 실행과 여러 에이전트의 협력 플레이를 예고했습니다.

관련: [agent-wow 발표](https://agent-wow.sh/gpt-6-astra-plays-world-of-warcraft-for-the-first-time-with-agent-wow/)

### 10. [소프트웨어 엔지니어링이라는 말을 만든 Margaret Hamilton 별세](https://news.mit.edu/2026/margaret-hamilton-computing-pioneer-dies-1007)

Apollo 비행 소프트웨어를 이끈 Margaret Hamilton이 9월 30일 90세로 세상을 떠났습니다. 1965년 MIT 계측연구소에 Apollo 프로젝트의 첫 프로그래머로 합류했고, 1968년에는 400명 넘는 인원이 참여한 사령선·기계선 소프트웨어 팀의 부책임자가 됐습니다. 소프트웨어를 하드웨어와 같은 공학 분야로 다루자는 뜻에서 "software engineering"이라는 말을 쓰기 시작한 것으로 알려져 있습니다.
Apollo 11 착륙 직전 컴퓨터 과부하로 1202 경보가 울렸을 때, 우선순위가 낮은 작업을 내리고 착륙에 필요한 작업만 돌리도록 설계한 그의 팀 소프트웨어 덕분에 착륙을 이어 갈 수 있었습니다. 네 살 딸이 시뮬레이터에서 비행 중 사전 발사 프로그램을 실행해 시스템을 멈춘 일을 계기로 방어 코드를 제안했다가 거절당했는데, Apollo 8에서 우주비행사가 같은 실수를 하자 채택된 일화도 유명합니다.
1976년 Higher Order Software, 1980년대 Hamilton Technologies를 세웠고, 2016년 대통령 자유 훈장을 받았습니다.

---

## 🚀 Indie Radar
{: #indie-radar}

### [Bigwords.page](https://bigwords.page/) · 웹 토이 · Show HN 709점

링크 하나로 어떤 화면이든 전광판으로 바꾸는 무료 웹 앱입니다. 표시할 문구는 URL의 `#` 뒤에, 설정은 `&key=value`로 붙이기 때문에 링크 자체가 앱이고, 프래그먼트는 서버로 전송되지 않아 저장되는 데이터도 없습니다. 화면 크기에 맞춘 자동 글자 크기, `||`로 나누는 슬라이드, `{countdown}` 카운트다운, Wi-Fi 접속용 QR 코드를 지원해 공항 마중 팻말, TV 카운트다운, 프런트 데스크 안내판 같은 용도로 쓸 수 있습니다. MIT 라이선스입니다.

### [bigarrow](https://github.com/franzenzenhofer/big-arrow-on-the-screen) · 오픈소스 macOS 도구 · Show HN 390점

AI 에이전트가 사용자 화면 위에 큰 화살표와 안내 문구를 그려 "여기를 누르세요"라고 가리키게 해 주는 CLI입니다. 클릭이나 입력, 화면 캡처는 하지 않고 가리키기만 한다는 점을 내세웠고, 화살표는 클릭을 통과시키며 정해진 시간이 지나면 사라집니다. `bigarrow point --element "Allow" --app "System Settings"`처럼 접근성 레이블로 대상을 찾을 수 있고, Claude Code와 Codex용 스킬을 설치하는 명령도 있습니다. 에이전트에게 화면 조작 권한을 다 주기엔 부담스러울 때 쓸 만한 중간 지점이라 반응이 컸습니다.

### [Skillry](https://trustmrr.com/startup/skillry) · 에이전트 스킬 마켓 · MRR $1.9k (TrustMRR 인증)

Claude Code, Codex, Cursor 같은 코딩 에이전트용 스킬을 모아 파는 1인 서비스입니다. 웹사이트, 슬라이드, 이미지, 영상을 만드는 스킬의 실제 결과물을 미리 보고 웹이나 CLI로 설치하는 방식이며, 무료 스킬과 월 $9.99 프리미엄을 함께 운영합니다. 8월에 시작해 최근 30일 매출 $5.6k, 활성 구독 196개를 기록했습니다. 에이전트 스킬이 하나의 판매 단위가 되기 시작했다는 점에서 눈여겨볼 사례입니다.

### [Battle Healer Hildegard](https://funday-games.itch.io/battle-healer-hildegard) · 인디 게임 · itch.io 신작 인기 1위

늘 뒤에서 치유만 하던 힐러를 주인공으로 내세운 브라우저 게임입니다. 기사들을 치유하고 성으로 피난 오는 주민을 구하며 번 돈으로 기사를 고용하고 성을 강화하는, 로그라이크와 타워 디펜스, 서바이버류를 섞은 구성입니다. 레벨 3, 6, 9마다 새 주문이 열립니다. 공개된 지 열흘이 안 된 무료 프로토타입이지만 평점 4.6점(14명)으로 이번 주 신작 인기 1위에 올랐습니다.

### [openGym](https://github.com/DuarteSantos8/openGym) · 오픈소스 셀프 호스팅 앱 · GitHub 주간 ★6.7k

Strong이나 Hevy 같은 운동 기록 앱을 대체하는 셀프 호스팅 서비스입니다. 5,600개가 넘는 운동 라이브러리로 주간 루틴을 짜고, 지난번 무게를 미리 채워 주는 운동 기록, 휴식 타이머, 개인 기록 감지, 근육별 회복 상태 지도를 제공합니다. FitNotes·Strong·Hevy·Apple Health에서 데이터를 가져올 수 있고, `docker compose up -d` 한 번으로 띄우며 Helm 차트도 있습니다. 데이터는 JSON 파일로 남고, 라이선스는 AGPL-3.0입니다.

---

## 🔭 모니터링 사례 & 강좌
{: #observability}

### [새로운 팀에 기여하기, 그리고 기여의 확장 (feat. 전시개발팀 옵저버빌리티 향상 시키기)](https://techblog.gccompany.co.kr/%EC%83%88%EB%A1%9C%EC%9A%B4-%ED%8C%80%EC%97%90-%EA%B8%B0%EC%97%AC%ED%95%98%EA%B8%B0-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EA%B8%B0%EC%97%AC%EC%9D%98-%ED%99%95%EC%9E%A5-feat-%EC%A0%84%EC%8B%9C%EA%B0%9C%EB%B0%9C%ED%8C%80-%EC%98%B5%EC%A0%80%EB%B2%84%EB%B9%8C%EB%A6%AC%ED%8B%B0-%ED%96%A5%EC%83%81-%EC%8B%9C%ED%82%A4%EA%B8%B0-c39614694661)

여기어때에서 게이트웨이 다음으로 트래픽을 가장 많이 받는 전시개발팀이 Pinpoint APM에 기대던 장애 대응을 OpenTelemetry와 Grafana(Mimir, Tempo, Loki) 대시보드로 옮긴 과정입니다. 새 에이전트 없이 이미 수집 중인 메트릭과 로그만 쓰되, APM에서 익숙했던 분석 흐름을 깨지 않는 것을 첫 기준으로 잡았습니다. 관측 도구 전환이 실패하는 흔한 이유가 기술 한계가 아니라 사용성 후퇴라고 봤기 때문입니다.
화면은 장애 때 던지는 질문 순서대로 배치했습니다. 지금 이상이 있는가(요청·성공·실패·TPS를 그래프 대신 숫자로), 우리 문제인가 호출 대상의 문제인가(Incoming과 Outgoing 분리), 어떤 요청에서 나는가(레이턴시·에러 패널에서 트레이스 상세로 이동), 왜 나는가(에러 로그 패널과 Loki Drilldown 링크) 순서입니다. Pinpoint 스캐터 차트의 "느린 요청 하나를 집어 보는" 경험은 같은 조건의 요청 목록 링크로 재현했습니다.
아쉬운 점으로 작업 전에 MTTD/MTTR 같은 측정 기준을 정해 두지 않아 개선 효과를 수치로 비교하지 못했다고 적었습니다. 대시보드를 새로 만들거나 도구를 바꿀 계획이라면 기준선부터 기록해 두라는 조언으로 읽힙니다.

### [The Shift to cgroup v2 in Kubernetes: What You Need to Know](https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/)

쿠버네티스가 cgroup v1을 지원 중단한 뒤 무엇을 챙겨야 하는지 정리한 공식 블로그 글입니다. v1.35부터 kubelet 설정 `failCgroupV1`의 기본값이 `true`라서, cgroup v1 노드에서는 kubelet이 아예 뜨지 않습니다. kubeadm도 v1.35 kubelet과 cgroup v1 조합이면 `init`, `join`, `upgrade` 단계에서 오류를 냅니다. 업그레이드 전에 모든 노드가 v2인지 확인하거나, 임시로 `failCgroupV1: false`를 둘지 정해야 합니다.
모니터링 관점에서 볼 부분이 많습니다. cgroup v2 노드에서는 컨테이너 OOM 시 프로세스 하나가 아니라 컨테이너 안 프로세스 전체를 함께 종료하는 것이 기본이고, `memory.events` 카운터로 OOM 이벤트를 관찰할 수 있습니다. CPU·메모리·I/O 경합을 보여 주는 PSI 지표는 v2에서만 나오며, kubelet이 `/metrics/cadvisor`로 기본 노출합니다. cgroup 파일을 직접 읽는 도구는 경로와 단위가 바뀌므로 cAdvisor v0.43.0 이상 등 호환 버전을 확인하라고 권합니다.
`cpu.shares`를 `cpu.weight`로 바꾸는 계산식이 crun v1.23, runc v1.3.2에서 달라져 `cpu.weight` 값을 예측하는 도구도 영향을 받습니다. 노드 이미지와 런타임을 올릴 때 대시보드와 알람 쿼리도 함께 점검해야 하는 이유입니다.

### [Zero-code trace-log correlation with OBI](https://opentelemetry.io/blog/2026/obi-trace-log-correlation/)

장애 중에 트레이스로 실패한 요청은 찾았는데 그 요청의 로그를 찾지 못해 타임스탬프로 뒤지는 상황을 겨냥한 기능입니다. OpenTelemetry eBPF 계측(OBI)이 각 스레드가 어떤 요청을 처리 중인지 추적하다가, 로그가 컨테이너 로깅 파이프라인으로 넘어가기 전에 `trace_id`와 `span_id`를 넣어 줍니다. 코드 수정이나 재빌드는 필요 없습니다.
JSON 로그에는 필드로, 일반 텍스트에는 `trace_id=...` 접미사로 붙입니다. 로거가 동기적으로 쓰는 Go, Java, Ruby는 잘 맞고, 파이프 출력이 비동기인 Node.js는 부하가 걸리면 일부 줄이 빠지거나 다른 요청의 ID가 붙을 수 있습니다. 데모도 계측하지 않은 Go 서비스 두 개로 진행했습니다.
제약도 분명합니다. stdout/stderr만 대상이고, 요청 처리 중에 쓴 로그만 보강되며, `write()` 경로를 보강하려면 Linux 6.0 이상과 `CAP_SYS_ADMIN`이 필요합니다. 원래 줄 대신 NUL 바이트 자리표시자가 남으므로 로그 수집기에서 이를 걸러 내야 합니다. 글에서는 위험이 낮은 서비스 하나로 시작해 로그가 중복되거나 쪼개지지 않는지 확인한 뒤 넓히라고 권합니다.

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [빨강의 자서전](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=353110834) · 앤 카슨 · 한겨레출판 (주간 2위) · 2026 노벨문학상 수상
  - [전지적 독자 시점 문고본 세트 - 전10권](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403781405) · 싱숑 · 비채 (주간 14위)
  - [짧은 이야기들](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=373368987) · 앤 카슨 · 난다 (주간 17위)
- 주목할 신간
  - [해방의 날](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403502741) · 조지 손더스 · 문학동네 · 정영목 옮김
  - [타이가 열병](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403768118) · 크리스티나 리베라 가르사 · 물결점 · 안태운 옮김

### IT

- 베스트 새 진입
  - [서늘한 대화](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403713715) · 정재승 · 어크로스 (주간 1위)
  - [AI 에이전트 실행 세계 1 : 원리편](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=395237018) · 조쉬(이주환) · 로드북 (주간 14위)
  - [일하는 AI 에이전트, 설계하는 사람](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403219956) · 최윤석 · 한빛미디어 (주간 16위)
- 주목할 신간
  - [리눅스 디바이스 드라이버 인사이드](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403475233) · 진성근 · 홍릉 · PCIe, DMA, RDMA까지 배우는 커널 실전 프로그래밍
  - [멀티모달까지 직접 구현하는 딥러닝 with 파이토치](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403419651) · 박상은 · 더 타이즈 · 기초 텐서 연산부터 최신 LLM 파인튜닝과 양자화까지

### 인문

- 베스트 새 진입
  - [지능의 기원](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=355714458) · 맥스 베넷 · 더퀘스트 (주간 6위)
  - [그라시안의 사람을 읽는 눈](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=399383376) · 발타사르 그라시안 · 히읏 (주간 18위)
- 주목할 신간
  - [우리는 어떤 AI를 만들고 있는가](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403731809) · 홍성욱 · 에디토리얼 · 포스트휴먼 기술론으로 이해하는 알파고, LLM, 전쟁 AI, 초지능
  - [공화주의자 공자](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403415541) · 권재현 · 은행나무 · 《논어》에서 길어 올린 파격의 정치사상

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
