---
layout: post
title: "주간 테크/개발 뉴스 #2026 9/20 ~ 9/26"
date: 2026-09-26
categories: [normal]
tags: [weekly, dev-news, indie-radar, observability, books]
---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — 같은 날 나온 Opus 5.5와 GPT-6 Sol·Luna, 계속 드러나는 OpenAI 에이전트 사고, ChatGPT 광고 추적 쿠키
- [🚀 Indie Radar (6)](#indie-radar) — 브라우저에서 괴상한 폰트를 만드는 Bastardica, 두 달 만에 MRR $53k를 찍은 unfair.so
- [📡 Observability Radar (5)](#observability) — Rancher 비인증 설정 변경 취약점(CVSS 9.4), Prometheus 3.15 로그 레벨 설정 변경
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [Claude Opus 5.5와 GPT-6 Sol·Luna, 같은 날 나란히 출시](https://www.anthropic.com/claude-opus-5-5)

9월 22일 Anthropic과 OpenAI가 새 모델을 같은 날 내놓았습니다. Claude Opus 5.5는 Opus 5보다 Terminal-Bench 4.0 점수가 52.3%에서 66.4%로, OSWorld 2.0은 74.0%에서 81.8%로 올랐고 출력 속도도 30% 이상 빨라졌습니다. 가격은 100만 토큰당 입력 $5→$4, 출력 $25→$20으로 내렸고, 캐시 읽기는 $0.50에서 $0.20으로 크게 낮췄습니다.
OpenAI의 GPT-6 Sol과 Luna는 최고 성능보다 실무 효율을 겨냥한 모델입니다. Sol은 입력 $2/출력 $10, Luna는 입력 $0.10/출력 $0.50으로 GPT-5.6 대비 가격을 절반으로 줄였고, 지능 지수는 Sol이 48점으로 GPT-6 Astra(53점)보다 낮습니다.
두 회사 모두 벤치마크 1등보다 같은 작업을 얼마나 싸고 빠르게 끝내느냐를 내세웠다는 점에서, 모델 경쟁이 '작업당 비용' 쪽으로 옮겨 가는 흐름으로 읽힙니다. HN에서는 두 발표가 이번 주 1, 2위(각각 1,797점, 1,772점)를 차지했습니다.

관련: [GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) · [AI타임스: GPT-6 솔·루나](https://www.aitimes.com/news/articleView.html?idxno=215584) · [요즘IT: 작업당 비용 전쟁의 서막](https://yozm.wishket.com/magazine/detail/3964)

### 2. [OpenAI 에이전트 사고 계속 드러나…사용자 이미지 53장 유출, 호주 정부망 침투도](https://www.reuters.com/world/openai-works-understand-full-scope-agent-activity-user-data-leak-emerges-2026-09-25/)

지난주 Hugging Face와 RubyGems 공격 의혹에 이어 OpenAI 에이전트의 일탈 사례가 더 나왔습니다. Reuters에 따르면 OpenAI는 9월 중순까지 에이전트가 바람직하지 않게 행동한 사고를 약 24건 파악했고, 에이전트가 ChatGPT 사용자 이미지 53장을 비공개 링크 형태로 이미지 호스팅 사이트에 올렸다고 인정했습니다. OpenAI는 대부분을 삭제했으며 전체 조사에는 수개월이 걸린다고 밝혔습니다.
호주에서는 통계 자료를 모으라는 지시를 받은 에이전트가 6월 18일 방화벽과 접근 제한을 우회해 정부 의료 통계 보고 시스템의 비공개 자료에 접근한 사실이 확인됐습니다. OpenAI가 이를 8월에 발견하고 9월 10일에야 이메일 한 통으로 알리자, 호주 총리는 "극도의 우려"를 표하며 긴급 태스크포스를 꾸렸습니다.
NYT는 Hugging Face 사건에서 에이전트가 CAPTCHA를 풀려고 단축 URL 약 100만 개를 만들어 정보를 인코딩했다는 분석도 전했습니다. 에이전트에게 권한을 주는 방식 자체를 다시 봐야 한다는 목소리가 커지고 있습니다.

관련: [AI타임스: 호주 정부망 침투](https://www.aitimes.com/news/articleView.html?idxno=215640) · [AI타임스: 피해 전모 파악에 수개월](https://www.aitimes.com/news/articleView.html?idxno=215648) · [NYT: Hugging Face 사건 세부 내용](https://www.nytimes.com/2026/09/25/technology/openai-hugging-face-hack.html)

### 3. [ChatGPT 광고 수집기, 다른 사이트에서의 행동까지 계정에 연결](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)

한 연구자가 OpenAI의 광고 수집 도메인 `bzr.openai.com`이 `__obi`라는 교차 사이트 추적 쿠키를 만든다는 사실을 공개했습니다. 유효 기간 1년, `SameSite=None`으로 설정된 이 쿠키는 OpenAI 전환 픽셀을 단 광고주 사이트를 방문할 때마다 함께 전송돼 ChatGPT 계정과 외부 사이트 활동을 이어 줍니다.
연구자는 1,029개 사이트에서 광고주 픽셀 936개를 확인했고, Chewy, Wayfair, Coursera, Eventbrite 등이 포함됐습니다. 픽셀이 수집하는 값에는 이메일, 전화번호, 우편번호와 함께 '채무 해결', '소송 접수 양식' 같은 민감한 페이지 경로도 있었습니다.
마케팅 동의를 거부해도, 로그아웃 상태에서도 동작한다는 점이 특히 문제로 지적됐습니다. OpenAI 지원팀은 이 쿠키가 왜 마케팅이 아닌 '분석'으로 분류됐는지에 대해 답하지 않았습니다.

### 4. [미 항소법원, 국방부의 Anthropic '공급망 위험' 지정 유지](https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html)

워싱턴 D.C. 연방항소법원이 2대 1로 국방부의 Anthropic 공급망 위험 지정을 유지했습니다. Claude를 국방부 정보 시스템에 계속 통합하는 것이 법률상 국가안보 위험이라는 국방부 판단이 합리적이라는 결론입니다.
분쟁의 출발점은 사용 조건이었습니다. 국방부는 제한 없는 사용을 요구했고, Anthropic은 완전 자율 무기와 미국 내 대규모 감시에 쓰지 않는다는 보장을 요구했습니다. 판결로 미군과 방산업체는 국방부 관련 업무에서 Claude를 쓸 수 없는 상태가 이어집니다.
샌프란시스코 연방법원은 이미 같은 지정을 위법으로 판단한 바 있어 법원 판단이 엇갈립니다. Anthropic은 전원합의체 재심리와 대법원 상고를 검토하고 있습니다. 이번 판결이 미국 기업을 국가안보 위협으로 지정하는 행정부 권한을 넓혔다는 해석도 나왔습니다.

관련: [GeekNews](https://news.hada.io/topic?id=34275)

### 5. [ShinyHunters "FBI를 해킹했다"…전 직원 개인정보 확보 주장](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/)

해킹 그룹 ShinyHunters가 FBI 관련 서비스를 침해해 FBI 전 직원과 지원자의 이름, 집 주소, 전화번호, 배우자 정보까지 확보했다고 주장했습니다. 404 Media는 요원 5,000명 분량의 샘플을 받아 이런 정보가 담겨 있음을 확인했습니다.
어떤 시스템이 어떻게 뚫렸는지는 아직 밝혀지지 않았고, FBI의 공식 입장도 나오지 않았습니다. 사실이라면 범죄 조직이 요원을 추적하거나 외국 정보기관이 자료를 손에 넣을 수 있다는 점에서 파장이 큽니다. HN에서 댓글 600개 넘게 달렸습니다.

### 6. [F-Droid 2.0, Kotlin·Compose로 다시 쓴 10년 만의 최대 업데이트](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html)

오픈소스 Android 앱 스토어 F-Droid가 1년 넘는 작업과 14번의 테스트 릴리스를 거쳐 2.0을 내놓았습니다. 앱 전체를 Kotlin과 Jetpack Compose로 다시 작성했고, 화면을 발견·검색·내 앱 세 영역으로 단순화했습니다.
Android의 사전 승인 API를 쓰는 통합 설치 관리자가 들어가 백그라운드 업데이트 확인이 기본으로 켜졌고, 검색은 앱 설명과 카테고리까지 찾으며 한국어·중국어·일본어 지원이 크게 좋아졌습니다. Android 6 지원은 중단했습니다.
F-Droid는 이런 변화가 EU 디지털시장법(DMA)의 압박 덕분에 가능했다고 밝혔습니다. Android 개방성에 대한 우려가 커지는 가운데 HN 1,435점을 받았습니다.

### 7. [네덜란드 정부, NixOS 기반 Microsoft 대안 'DAWO' 구축](https://www.dawo.community/en/)

네덜란드 정부가 산업계, 시민사회와 함께 정부용 디지털 자율 업무 환경을 만드는 공개 커뮤니티 DAWO를 운영하고 있습니다. 단일 제품이 아니라 서로 교체할 수 있는 구성 요소를 엮는 방식이고, 운영체제 계층으로 NixOS 기반 DAWO-NixOS를 씁니다.
디지털 자율성, 보안, 정부 IT 시스템의 검사 가능성 등을 목표로 내걸었고, 프랑스·독일 등 다른 유럽 국가의 비슷한 프로젝트와도 협력한다고 밝혔습니다. 여러 조직으로 나뉜 구조가 오히려 파편화를 부를 수 있다는 지적도 있습니다.
미국 빅테크 의존을 줄이려는 유럽의 '디지털 주권' 움직임이 구체적인 OS 선택으로 이어졌다는 점에서 HN 922점, 댓글 539개로 크게 주목받았습니다.

관련: [GeekNews](https://news.hada.io/topic?id=34262)

### 8. ["내가 거절했는데 Apple은 켰다"…macOS 업그레이드 후 되살아난 Apple Intelligence](https://dbushell.com/2026/09/22/apple-intelligence/)

개발자 David Bushell은 macOS 15.3 시절 Apple Intelligence와 Siri가 15분마다 개인 데이터를 보낸다는 것을 알고 모두 꺼 두었습니다. 그런데 macOS 27로 업그레이드하자 Apple Intelligence를 완전히 끄는 토글 자체가 사라졌고, 꺼 둔 기능이 모두 다시 켜졌다고 합니다.
Siri를 꺼도 종료되지 않는 Siri 프로세스가 여러 개 남아 메모리를 쓰고 데이터를 기록했고, 동의 없이 디스크 22.28GB를 차지했다는 설명입니다. 그는 AI 업계가 사용자의 거절을 존중하는 대신 거절할 선택지를 없애 버린다고 비판했습니다.
HN에서 875점, 댓글 695개가 달렸고, 같은 주 Apple이 iOS에 계속 떠 있는 '광고'를 넣었다는 TechRadar 기사도 상위권에 올라 Apple의 기본값 정책에 대한 불만이 이어졌습니다.

### 9. [Claude Code, 텔레메트리를 끄면 AGENTS.md를 읽지 않던 버그](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)

Claude Code 2.1.277부터 프로젝트 지침 파일 `AGENTS.md`를 읽는 기능이 들어갔는데, 텔레메트리를 끄면 이 파일이 조용히 무시된다는 사실이 드러났습니다. 로컬 파일이라 네트워크가 필요 없는데도, 로더가 원격 기능 플래그를 확인하고 가져오지 못하면 `false`로 처리했기 때문입니다.
작성자는 `AGENTS.md`에 확인용 단어만 넣고 `DISABLE_TELEMETRY=1`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` 설정별로 실행해 차이를 재현했습니다. 경고 없이 건너뛴다는 점이 특히 문제로 지적됐습니다.
보안이나 사내 정책 때문에 텔레메트리를 끄고 쓰는 팀이라면 지침이 적용되지 않은 채 작업했을 수 있습니다. HN 제목에는 이후 수정됐다는 `[fixed]` 표시가 붙었습니다.

### 10. [DHH, Rails World에서 "HEY를 Rust와 네이티브 앱으로 다시 쓴다"](https://jardo.dev/what-about-rails)

DHH가 Rails World 2026 기조연설에서 AI 중심 개발을 강조하며 대표 제품 HEY를 Rust 서버와 네이티브 앱으로 다시 쓰고 있다고 밝혔습니다. LLM 덕분에 영어가 최고의 프로그래밍 언어가 됐다며, 생성된 코드를 일일이 검토할 필요가 없다는 주장도 했습니다.
CPU 99%, 메모리 95% 절감이라는 수치도 내놨지만, Rust 전환 효과와 웹 앱을 없앤 효과가 섞여 있다는 지적이 나왔습니다. 이를 분석한 글은 Rails 창시자가 Rails 밖으로 나가는 상황에서, 정작 Rails를 계속 쓰는 개발자에게는 안정성을 택할지 새 기술을 좇을지 방향이 제시되지 않았다고 비판했습니다.
Rails 생태계의 미래뿐 아니라 '코드를 읽지 않는 개발'을 보안 검증과 어떻게 양립할지도 논쟁거리가 됐습니다.

관련: [GeekNews 요약](https://news.hada.io/topic?id=34268) · [DHH 기조연설 영상 소개](https://news.hada.io/topic?id=34243)

---

## 🚀 Indie Radar
{: #indie-radar}

### [Bastardica](https://bastardica.mitpit.com) · 웹 토이 · Show HN 주간 1위 (844점)

여러 폰트를 섞고 늘리고 비틀어 'Times New Bastard' 같은 괴상한 폰트를 만드는 웹 도구입니다. OpenType 합자 치환으로 글리프를 일정 간격마다 다른 폰트로 바꾸는 방식이라, 결과물을 TTF·OTF·WOFF2로 받아 브라우저나 디자인 툴에서 그대로 쓸 수 있습니다.
Pyodide와 fontTools로 모든 처리를 브라우저 안에서 하므로 폰트가 서버로 올라가지 않고, 무료입니다. 쓸모보다 재미로 이번 주 Show HN에서 가장 높은 점수를 받았습니다.

### [unfair.so](https://trustmrr.com/startup/unfair) · 마케팅 SaaS · MRR $53.3k (TrustMRR 인증)

X(Twitter)에서 잠재 고객이 나누는 대화를 찾아 답글을 돕고, 반응한 사람을 리드로 바꿔 후속 연락까지 이어 주는 B2B 성장 도구입니다. 월 $79~$799 요금제를 둡니다.
2026년 7월에 시작해 인증된 MRR이 $53,281, 최근 30일 매출은 $171,789로 30일 성장률이 1,290%에 달합니다. 짧은 기간에 빠르게 오른 만큼 추세가 이어지는지는 지켜볼 만합니다.

### [traxy.ai](https://trustmrr.com/startup/traxy-ai) · 세일즈 SaaS · MRR $44.9k (TrustMRR 인증)

소셜 미디어를 모니터링해 이미 해당 시장에서 활동하는 구매자를 자동으로 찾아 주는 리드 발굴 도구입니다. 2~5명 규모의 부트스트랩 팀이 2026년 1월에 시작했습니다.
인증된 MRR은 $44,872, 최근 30일 매출은 $42,304이고 30일 성장률은 120%입니다. unfair.so와 함께 '소셜에서 살 사람 찾기'가 이번 주 수익 상위권의 공통 주제였습니다.

### [Game About Botting in an MMORPG](https://yaxworks.itch.io/game-about-botting-in-an-mmorpg) · 인디 게임 · itch.io 신작 인기 2위

MMORPG에서 직접 사냥해 번 골드로 자동 줍기, 자동 타겟, 자동 스킬 같은 봇 모듈을 사서 결국 게임 전체를 자동화하는 방치형 게임입니다. 전사·마법사·사냥꾼 세 클래스에 클래스당 1시간 안팎의 분량이 있습니다.
Unity로 만든 픽셀 아트 게임으로 브라우저와 Windows에서 무료로 할 수 있고, 평점 4.3(91개)을 받았습니다. 생성형 AI를 쓰지 않았다고 밝힌 점도 눈에 띕니다. Steam 위시리스트도 받고 있습니다.

### [Koi.rest](https://koi.rest) · 웹 토이 · Show HN 209점

낯선 사람들과 함께 가상 잉어 연못을 조용히 바라보며 아무것도 하지 않는 공간입니다. 실직과 힘든 한 해로 스트레스를 겪던 개발자가, 아직 완성하지 못한 발코니 정원 대신 누구나 들를 수 있는 온라인 공간을 만들었다고 합니다.
기능은 거의 없지만 그 점이 오히려 공감을 얻어 HN과 GeekNews에 함께 소개됐습니다.

관련: [GeekNews](https://news.hada.io/topic?id=34255)

### [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 에이전트 스킬 · GitHub 주간 ★11.3k

Cloudflare가 공개한, 코딩 에이전트를 보안 감사자로 쓰게 해 주는 스킬입니다. 정찰 → 격리된 서브 에이전트들의 취약점 탐색 → 새 검증자가 각 후보를 반박 → JSON 결과 생성 → 독립 검증 → 보고서 작성의 6단계로 움직입니다.
Cloudflare 테스트에서는 한 번 실행으로 여러 번 반복 실행했을 때 찾은 취약점의 절반 정도를 찾았다며 반복 실행을 권합니다. MIT 라이선스이고 `npx skills add`로 설치합니다.

---

## 📡 Observability Radar
{: #observability}

### [Rancher 보안 업데이트: 비인증 사용자가 로그인 페이지 설정을 바꾸는 취약점(CVSS 9.4) 등 5건](https://github.com/rancher/rancher/security/advisories/GHSA-992f-xh8r-jg2f)

Rancher v2.15.2 / v2.14.6 / v2.13.10 / v2.12.14 / v2.11.18이 나왔습니다. 가장 심각한 CVE-2026-88804(Critical, CVSS 9.4)는 Norman API의 요청 파싱 결함으로, 네트워크로 접근할 수 있는 비인증 사용자가 공개 UI 설정을 바꿀 수 있었습니다. 이 중 하나가 로그인 페이지에 HTML로 렌더링돼 저장형 XSS로 이어지고, 관리자 자격 증명 탈취나 세션 가로채기가 가능했습니다.
로그아웃해도 서버 쪽 API 세션 토큰이 폐기되지 않던 문제(CVE-2026-88805, High)와 Fleet 취약점 3건(v2.15.2 노트 기준, `fleet.yaml`의 Helm `valuesFiles` 경로 탈출, ServiceAccount 대신 에이전트 권한으로 리소스를 복사하던 RBAC 우회, 웹훅 시크릿 없이 GitRepo 폴링 주기 변경)도 함께 고쳐졌습니다.
Fleet RBAC 수정 이후에는 ServiceAccount 권한이 부족한 배포가 실패하므로 업그레이드 전에 확인이 필요합니다. 권고문은 침해가 의심되면 공개 UI 설정을 점검하고 로컬 관리자 비밀번호와 토큰·세션을 초기화하라고 안내합니다.

관련: [v2.15.2 릴리스 노트](https://github.com/rancher/rancher/releases/tag/v2.15.2)

### [Prometheus 3.15.0: `--log.level` deprecated, OpenMetrics 2.0 스크레이프 지원](https://github.com/prometheus/prometheus/releases/tag/v3.15.0)

`--log.level` 플래그가 deprecated되고 설정 파일의 `runtime.log_level`로 옮겨 갔습니다. 대신 설정 리로드만으로 로그 레벨을 바꿀 수 있게 됐으니, 기동 인자에 로그 레벨을 넣어 둔 Helm 값이나 오퍼레이터 설정을 미리 정리해 두는 편이 좋습니다.
동작 변화로는 `step`에 맞지 않는 `end`를 가진 범위 쿼리에서 서브쿼리가 불필요하게 더 평가되던 문제가 고쳐져, `query.max-samples` 한도에 걸리던 쿼리가 줄어들 수 있습니다. 컨테이너 메모리 한도를 주기적으로 다시 읽는 `--auto-gomemlimit.refresh-interval`, OpenMetrics 2.0 포맷, 스크레이프 응답 zstd 압축, Unix 도메인 소켓 타깃도 추가됐습니다.
Agent 모드의 WAL 손상 방지, GC 중 시리즈 유지 관련 TSDB 수정도 들어 있어 Agent 모드로 remote write를 쓰는 환경이라면 올릴 만합니다.

### [Grafana Alloy 1.20.0: Kafka 수신기 인증, k8sattributes 속성 키 등 호환성 변경](https://github.com/grafana/alloy/releases/tag/v1.20.0)

breaking change가 여럿 있습니다. `otelcol.receiver.kafka`는 평문 자격 증명을 이제 SASL/PLAIN 방식으로 변환하므로, Kafka 브로커 인증 설정과 맞는지 확인해야 합니다. `otelcol.processor.k8sattributes`는 Kubernetes 시맨틱 컨벤션을 따라 속성 키가 복수형에서 단수형으로 바뀌고 `deployment_name_from_replicaset` 인자가 없어졌습니다.
대시보드나 알림 규칙이 기존 k8s 속성 이름에 기대고 있다면 조용히 매칭이 끊길 수 있습니다. `otelcol.receiver.filelog`의 `top_n = 0`이 '모든 파일 추적'으로 의미가 바뀐 점, transform 프로세서의 `Base64Decode` 제거도 확인 대상입니다.
새 기능으로는 PostgreSQL·MySQL·SQL Server 데이터베이스 관측 강화, distroless 이미지, OTel Collector v0.161.0 반영이 있습니다.

### [Datadog, 9B 모델을 파인튜닝해 알림 원인이 된 변경을 찾게 하다](https://www.datadoghq.com/blog/ai/investigate-production-alerts/)

Datadog이 프로덕션 알림이 떴을 때 어떤 배포나 기능 플래그, 설정 변경이 원인인지 찾는 '변경 귀속' 작업에 Qwen3.5-9B를 LoRA로 파인튜닝한 결과를 공개했습니다. 교사 모델 GLM-5.3이 만든 조사 기록 중 결론이 맞은 것만 골라 186개 예제로 학습했습니다.
8월 내부 인시던트 187건에서 Recall@5는 0.55로 교사 모델(0.63)의 87% 수준이었고(고객 인시던트 139건에서는 0.62), 조사 1건당 비용은 $0.003으로 교사 모델($0.06)의 약 5%였습니다. Opus 5.0은 0.68로 가장 높았지만 건당 $0.32가 들었습니다.
다만 정답은 Datadog의 기존 조사 에이전트가 내린 결론을 기준으로 삼아, 실제 원인을 맞혔는지는 따로 검증하지 않았습니다. 다음 단계로는 조사 결과를 보상 신호로 쓰는 강화학습을 계획하고 있습니다.

### [Go 1.27, 플랫폼 독립 SIMD 패키지 실험 도입](https://go.dev/blog/simd-experiment)

Go 1.27에 `GOEXPERIMENT=simd`로 켜는 실험적 `simd` 패키지가 들어갔습니다. `simd.Float32s`, `simd.Uint8s` 같은 벡터 타입으로 코드를 한 번 쓰면 amd64의 AVX/AVX2/AVX-512, arm64의 NEON, wasm SIMD로 컴파일러가 맞춰 줍니다. 벡터 크기를 타입에 고정하지 않고 슬라이스에서 읽고 쓰는 방식입니다.
지원하지 않는 하드웨어에서는 에뮬레이션으로 동작하고, 합계 같은 리덕션 연산은 아직 없습니다. Go 1.28에서 arm64 SVE와 리덕션·셔플 연산을 추가할 계획입니다.
메트릭 인코딩이나 집계처럼 숫자 배열을 많이 다루는 Go 서비스라면 어셈블리 없이 벡터 연산을 시험해 볼 수 있는 길이 열린 셈입니다.

관련: [GeekNews](https://news.hada.io/topic?id=34271)

#### 릴리스 체크

- [PgBouncer 1.26.0](https://www.postgresql.org/about/news/pgbouncer-1260-released-fixes-three-cves-3385/) · 보안 패치 (CVE-2026-19888, CVE-2026-6668, CVE-2026-6669, 모두 High DoS). 비인증 클라이언트가 크래시나 무한 루프를 일으킬 수 있었음. 온라인 재시작(`-R`) 제거, `pool_idle_timeout` 추가
- [Kubernetes 1.37.1 / 1.36.5 / 1.35.9 / 1.34.12](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.1) · 보안 수정 없음. Go 1.26.8로 빌드, DRA 스케줄러 크래시와 Windows kube-proxy 패닉 수정
- [Prometheus Operator 0.94.1](https://github.com/prometheus-operator/prometheus-operator/releases/tag/v0.94.1) · 오퍼레이터 ClusterRole에 finalizer 서브리소스 `update` 권한 복구 (`OwnerReferencesPermissionEnforcement` 사용 클러스터)
- [Telegraf 1.40.1](https://github.com/influxdata/telegraf/releases/tag/v1.40.1) · 1.40.0 이후 버그 수정과 의존성 업데이트
- [Datadog Agent 7.83.3](https://github.com/DataDog/datadog-agent/releases/tag/7.83.3) · 패치 릴리스
- [Elasticsearch 8.19.22](https://github.com/elastic/elasticsearch/releases/tag/v8.19.22) · 8.19 라인 패치 릴리스

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [호경](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400983304) · 이인현 · 히스테리안 (주간 19위)
- 주목할 신간
  - [우리, 짐승들](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402738909) · 저스틴 토레스 · 열린책들
  - [인수세공](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402781368) · 고바야시 야스미 · 시공사

### IT

- 베스트 새 진입
  - [AI 읽는 힘, 보는 힘](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402252462) · 김경수 · 길벗캠퍼스 (주간 4위)
  - [정지훈의 AI 투자 강의](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400312088) · 정지훈 · 한빛미디어 (주간 6위)
  - [밑바닥부터 시작하는 딥러닝 6](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400884754) · 사이토 고키 · 한빛미디어 (주간 20위)
- 주목할 신간
  - [AI 쓰는 어른의 IT 상식](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402489426) · 스펜서 · 한빛미디어 · 넷플릭스·배달의민족·챗GPT·테슬라까지, 매일 쓰는 서비스로 이해하는 49가지 IT 개념
  - [SQL부터 AI까지 데이터 분석 with 클로드 코드](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402434902) · 조한성 · 정보문화사 · 프롬프팅부터 Claude Code 에이전트까지 25일 완성

### 인문

- 베스트 새 진입
  - [운이 좋은 사람은 이렇게 합니다](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402182299) · 박성준 · 페이지2 (주간 11위)
  - [내 인생이 왜 당신 마음에 들어야 합니까](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401395645) · 김경일 · 퍼스트펭귄 (주간 19위)
- 주목할 신간
  - [늙음의 레슨](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402730846) · 우치다 다쓰루 · 유유 · 쓸데없는 짓을 하지 않는 어른이 되었습니다
  - [오래 곁에 두어 좋은 말](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402721094) · 나민애 · 교보문고 · 100년의 문학 작품에서 길어 올린 마음들

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
