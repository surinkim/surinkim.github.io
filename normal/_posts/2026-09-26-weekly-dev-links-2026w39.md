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

### 6. ["내가 거절했는데 Apple은 켰다"…macOS 업그레이드 후 되살아난 Apple Intelligence](https://dbushell.com/2026/09/22/apple-intelligence/)

개발자 David Bushell은 macOS 15.3 시절 Apple Intelligence와 Siri가 15분마다 개인 데이터를 보낸다는 것을 알고 모두 꺼 두었습니다. 그런데 macOS 27로 업그레이드하자 Apple Intelligence를 완전히 끄는 토글 자체가 사라졌고, 꺼 둔 기능이 모두 다시 켜졌다고 합니다.
Siri를 꺼도 종료되지 않는 Siri 프로세스가 여러 개 남아 메모리를 쓰고 데이터를 기록했고, 동의 없이 디스크 22.28GB를 차지했다는 설명입니다. 그는 AI 업계가 사용자의 거절을 존중하는 대신 거절할 선택지를 없애 버린다고 비판했습니다.
HN에서 875점, 댓글 695개가 달렸고, 같은 주 Apple이 iOS에 계속 떠 있는 '광고'를 넣었다는 TechRadar 기사도 상위권에 올라 Apple의 기본값 정책에 대한 불만이 이어졌습니다.

### 7. ["문장 생성 버렸다"…판단 전용 AI Jev에 개발자 반응 폭발](https://www.aitimes.com/news/articleView.html?idxno=215506)

지난주 소개한 TypeSafe AI의 Jev가 공개 일주일 만에 개발자 커뮤니티에서 가장 뜨거운 주제가 됐습니다. 단어를 하나씩 생성하는 디코더 없이 한 번의 패스로 선택지, 확률 분포, 신뢰도 점수만 돌려주는 의사결정 전용 모델로, 응답 속도는 70~500ms, 입력 100만 토큰당 $0.042에 출력은 무료입니다.
공개 48시간 만에 GitHub와 X에 오픈소스 클론이 6개 넘게 나왔고, Diogo Almeida 대표의 X 게시물은 3,700만 회 넘게 조회됐습니다. 한 개발자는 StarCraft 유닛 제어에 붙여 초당 10번씩 움직임을 결정하게 했습니다. 이번 주에도 Qwen3.5 기반의 Jev 방식 모델 Kev, 이런 모델을 로컬에서 돌리는 Ollaya, 파이썬 25줄로 흉내 낸 구현 등이 HN과 GeekNews 상위권을 채웠습니다.
다만 출력 형식이 절대 깨지지 않는다는 것과 판단이 정확하다는 것은 별개라는 지적도 나왔습니다. 신뢰도 점수에 임계값을 두는 식으로 시스템을 설계해야 한다는 것입니다. 빠른 판단은 Jev 같은 경량 모델이, 깊은 추론은 대형 LLM이 나눠 맡는 'System 1 / System 2' 구조가 자리 잡을 것이라는 전망이 많습니다.

관련: [Kev](https://github.com/jaredpalmer/kev/tree/main) · [Ollaya (GeekNews)](https://news.hada.io/topic?id=34288) · [Jev in 25 Lines of Python](https://www.nobodywho.ai/posts/jev-in-25-lines/)

### 8. [구글 '제미나이 4 프로' 테스트 포착…"UI·웹 디자인 성능 도약"](https://www.aitimes.com/news/articleView.html?idxno=215631)

구글이 코드네임 'Argon'으로 Gemini 4 Pro를 내부 테스트 중인 것이 포착됐습니다. X의 유출 계정 Lentils80이 처음 알렸고, 벤치마크 플랫폼에는 'Gemini 3.8 Flash'라는 이름으로 위장해 올라와 있었다고 합니다.
눈에 띄는 건 프론트엔드 코드 생성입니다. 한 개발자는 모노그래픽 웹사이트를 14분 만에 깔끔하게 만들어 냈다고 했고, Xbox·PS5 컨트롤러를 곡선과 음영까지 살린 SVG로 그려 낸 사례도 공유됐습니다. 출력 토큰 한도는 64,000에서 256,000으로 늘어난 것으로 알려졌고, 구글은 3.5 Pro를 건너뛰고 4에 집중했다고 합니다.
출시 시점도 앞당겨질 전망입니다. 구글 딥마인드의 Koray Kavukcuoglu 수석 부사장은 첫 공식 인터뷰에서 Gemini 4를 연말보다 "훨씬 더 일찍" 내놓고 싶다며, 현재 사후 학습 초기 단계라고 밝혔습니다. 업계는 10월 출시를 점치고 있어, Opus 5.5와 GPT-6에 이은 모델 경쟁이 한 차례 더 이어질 것으로 보입니다.

관련: [AI타임스: 딥마인드 수장 "제미나이 4 조기 출시"](https://www.aitimes.com/news/articleView.html?idxno=215646)

### 9. [GPT-6 Astra, '통설' 뒤집고 108년 된 독일군 암호 해독](https://www.aitimes.com/news/articleView.html?idxno=215511)

독립 개발자 Prinz가 OpenAI의 GPT-6 Astra로 1918년 11월 29일 독일군이 보낸 ADFGVX 암호문을 풀었습니다. 세계 50대 미해결 암호 목록에 올라 있던 문제입니다.
그동안 연구자들은 암호 키 'TRUPPENVERSCHIEBUNG(부대 이동)'이 12월 9일부터 쓰였다고 보고, 그 전인 11월 29일 암호문에는 이 키가 쓰이지 않았다고 단정해 왔습니다. Astra는 이 전제를 의심해 더 이른 시점에도 같은 키가 쓰였을 가능성을 열어 두고 대입했고, 해독에 성공했습니다. 풀린 내용은 영국 순양함 HMS Canterbury의 세바스토폴 도착(11월 24일)과 연합군 함대 추적(11월 26일)에 관한 정보로, 역사 기록과 정확히 맞았습니다.
같은 주에는 2005년부터 풀리지 않던 1941년 독일군 Enigma 메시지 MVUEH도 Astra가 약 이틀 만에 스스로 시뮬레이터를 짜서 풀어냈습니다. 지난주 Claude Fable 5.1의 17세기 암호 해독에 이어, AI가 오래된 미해결 문제의 전제 자체를 다시 검토하는 사례가 이어지고 있습니다.

관련: [MVUEH Enigma 해독 (HN 734점)](https://www.cryptocellar.org/bgac/the-mvueh-break.html)

### 10. [메타 에이전트 '뮤즈', 출시 초기 ChatGPT 기록 넘어섰다](https://www.aitimes.com/news/articleView.html?idxno=215566)

메타가 9월 8일 미국·캐나다에 내놓은 개인형 AI 에이전트 앱 Muse가 빠르게 퍼지고 있습니다. 웹 검색, 이메일 정리, 일정 관리, 온라인 양식 작성, 상품 검색과 구매까지 대신 해 주고, Facebook, Instagram, Gmail, Apple·Google 캘린더와 연결됩니다.
Apptopia 조사에서 Muse는 출시 13일 동안 iOS 다운로드 180만 건, 일일 활성 사용자(DAU) 64만 2천 명을 기록했습니다. ChatGPT 앱의 같은 기간 기록(130만 건, DAU 23만 1천 명)을 넘어선 수치이고, 센서타워는 다운로드를 250만 건 이상으로 추정했습니다. 메타 주가는 21일 하루에 11% 올랐습니다.
반면 Amazon은 제3자 AI 에이전트는 사업자 동의가 필요하다며 Muse의 자동 쇼핑을 막았습니다. 에이전트가 사람 대신 사이트를 쓰기 시작하면서, 서비스 업체와 에이전트 운영사 사이의 이용 규칙이 새로운 쟁점으로 떠오르고 있습니다.

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
