---
layout: post
title: "주간 테크/개발 뉴스 #2026 9/13 ~ 9/19"
date: 2026-09-19
categories: [normal]
tags: [weekly, dev-news, indie-radar, books]
---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — 문장 대신 확률을 내는 Jev, 370년 암호 푼 Fable 5.1, 코딩 에이전트 스킬 제로클릭 RCE
- [🚀 Indie Radar (6)](#indie-radar) — 새소리를 듣고 그림을 그리는 e-ink 액자, 승객 전용 비행 시뮬레이터
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [TypeSafe AI, 문장 대신 '판단과 확률'을 반환하는 모델 Jev 공개](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

ChatGPT의 기반이 된 연구에 참여했던 전 OpenAI 연구자 Diogo Almeida가 2년간의 스텔스 끝에 TypeSafe AI의 첫 모델 Jev를 얼리 액세스로 공개했습니다. 분류, 라우팅, 점수화처럼 소프트웨어 안에서 반복되는 판단을 위한 'System One Model'로, 텍스트를 한 토큰씩 생성하지 않고 미리 정의한 타입의 값과 보정된 확률을 한 번에 병렬로 돌려줍니다.
문자열을 만들지 않으니 파싱 실패나 스키마 이탈이 없고, 응답 시간은 70~500ms, 가격은 입력 100만 토큰당 $0.042에 출력은 무료라고 밝혔습니다. 다만 자체 평가에서 내세운 '193.6배 빠르고 444.6배 저렴'은 비교 구성에 따라 달라지는 상단 수치라는 지적도 있습니다.
HN에서 이번 주 두 번째로 많은 점수를 받았고, 공개 모델의 로짓을 직접 읽어 같은 방식을 흉내 낸 오픈소스 실험(SemIf, 구 OpenJev)도 바로 등장했습니다. 이 실험은 JSON 생성보다 5.21배 빨랐지만 21개 판단 중 18개만 결과가 같았습니다.

관련: [GeekNews 요약](https://news.hada.io/topic?id=33751) · [SemIf(구 OpenJev)](https://openjev.com/) · [Jevlike](https://news.hada.io/topic?id=33854)

### 2. [Claude Fable 5.1, 370년 넘게 풀리지 않던 암호를 44분 만에 해독](https://www.vals.ai/blogs/fable-solves-cyphral-distich)

Vals AI가 Claude Fable 5.1에게 17세기 작가 Thomas Urquhart가 남긴 암호문 'Cyphral Distich'를 풀라는 과제만 주고 지켜봤습니다. 숫자 64개로 된 이 암호는 1899년 학술지에 미해결 문제로 소개됐고, 세계 50대 미해결 암호 목록에도 올라 있던 문제입니다.
Fable 5.1은 개입 없이 44분, 17.6만 토큰 만에 답을 냈습니다. 열쇠는 외부 암호표가 아니라 책 자체였습니다. i번째 숫자를 책에 실린 32개 조항(Proquiritations) 중 i번째 조항의 단어 위치로 보고 그 단어의 첫 글자를 모으면, 찰스 2세를 위한 기도문 두 줄이 나옵니다.
각 줄이 정확히 32자이고 운율까지 맞아 스스로 검증되는 답이라는 평가를 받았습니다. 같은 방식으로 숫자 285개짜리 더 큰 암호도 9글자를 빼고 풀었다고 합니다.

관련: [AI타임스](https://www.aitimes.com/news/articleView.html?idxno=215301)

### 3. [MS 임원 "AI 스크래핑은 인류 역사상 최대의 노동 절도"…NYT 소송 문서 공개](https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/)

뉴욕타임스가 OpenAI와 Microsoft를 상대로 낸 저작권 소송에서 가려져 있던 내용이 공개됐습니다. Microsoft 고위 임원이 내부에서 AI 학습 관행을 '절도'라고 불렀고, OpenAI 경영진도 자사 모델이 언론사에 '실존적 위협'이라고 말한 것으로 나옵니다.
Microsoft 자체 데이터에서 Copilot은 기존 Bing 검색보다 뉴욕타임스 도메인 클릭률을 최대 93% 떨어뜨렸고, 내부 발표 자료는 이를 모델과 웹을 함께 망가뜨리는 '둠 루프'라고 표현했습니다.
시장 대체 여부는 공정 이용 판단의 핵심이라 소송에 불리한 자료로 보입니다. 다만 인용 대부분은 원고 측 서면에서 나온 것이고 원본 증거는 여전히 비공개입니다. HN에서 댓글 800개 가까이 달리며 이번 주 가장 뜨거운 논쟁거리 중 하나였습니다.

관련: [GeekNews](https://news.hada.io/topic?id=33890)

### 4. [NVIDIA, Rust로 GPU 커널을 직접 쓰는 CUDA Rust 발표](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)

지금까지 Rust에서는 GPU 커널을 호출할 수는 있어도 커널 자체는 CUDA C++ 등으로 써야 했습니다. NVIDIA가 커널을 Rust로 작성해 PTX로 바로 컴파일하는 두 갈래의 도구를 공개했습니다.
cuda-oxide는 스레드 단위로 짜는 기존 SIMT 방식을 위한 rustc 코드 생성 백엔드로, 아직 초기 알파이고 nightly 툴체인이 필요합니다. cutile-rs는 타일 단위로 짜면 컴파일러가 스레드 매핑과 메모리 배치를 맡는 방식으로, stable Rust에서 돌아가고 이미 crates.io에 올라가 mistral.rs 등에서 쓰이고 있습니다.
두 도구 모두 메모리 앨리어싱을 컴파일 타임에 막는 것이 특징입니다. NVIDIA는 2027년 이후까지 CUDA Rust를 키우고 C++, Python과 상호 운용을 지원하겠다고 밝혔습니다. 지난주 Microsoft의 Rust Tier-1 격상에 이어 Rust에 힘이 실리는 소식입니다.

관련: [GeekNews](https://news.hada.io/topic?id=33815)

### 5. [Android 17 QPR1, 3.x 이후 처음으로 AOSP 공개 없이 새 API 추가](https://grapheneos.social/@GrapheneOS/117282080803799576)

9월 15일 배포된 Android 17 QPR1에 앱 개발자용 새 API가 추가됐는데, 소스는 AOSP에 공개되지 않고 Pixel에서만 쓸 수 있습니다. GrapheneOS에 따르면 Honeycomb(3.x) 이후 처음 있는 일이고, 다른 제조사와 AOSP 기반 프로젝트는 12월 QPR2에서야 받게 됩니다.
더 큰 문제로 지적된 건 보안 패치입니다. 9월 Pixel 보안 공지에 Pixel이 아닌 기기에도 해당하는 표준 플랫폼 패치가 들어 있는데, 일반 Android 보안 공지에는 빠져 있다는 것입니다.
GrapheneOS는 "Google이 표준 플랫폼 보안 패치를 제조사들로부터 막아서는 안 된다"며 역공학으로 먼저 적용하겠다고 밝혔습니다. Android의 개방성이 점점 줄어든다는 우려가 다시 커지고 있습니다.

관련: [GeekNews](https://news.hada.io/topic?id=33910) · [API 변경 목록](https://developer.android.com/sdk/api_diff/37.1/changes)

### 6. [Claude Code·Codex 등 코딩 에이전트 4종, 스킬 업데이트로 제로클릭 RCE](https://www.aitimes.com/news/articleView.html?idxno=215454)

보안 스타트업 Air가 Claude Code, Codex, Gemini CLI, GitHub Copilot 네 가지 코딩 에이전트에서 'Plugin4Shell'이라는 제로클릭 원격 코드 실행 취약점을 발견했다고 발표했습니다.
네 서비스 모두 마켓플레이스에서 받은 스킬이나 플러그인을 처음 등록할 때만 검사하고 이후 업데이트는 다시 검증하지 않았습니다. 공격자는 유용한 스킬로 사용자를 모은 뒤, 고정해 둔 커밋 SHA와 같은 이름의 브랜치를 만들어 악성 업데이트를 밀어 넣을 수 있었습니다.
Anthropic과 OpenAI는 패치를 마쳤고, Google은 Gemini CLI 지원 종료를 이유로 사용 중단을 권고했습니다. Microsoft는 플랫폼 차원에서 같은 이름의 재업로드가 막혀 있다는 입장입니다. 스킬과 플러그인이 새로운 공급망 공격 경로가 된 셈입니다.

### 7. [GLM 코딩 앱 ZCode, 사용자 모르게 작업 공간과 Git 이력을 클라우드로 업로드](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)

Z.ai(Zhipu)의 데스크톱 코딩 앱 ZCode가 로그인 상태에서 작업 공간 전체와 `.git` 이력, LFS 캐시, reflog를 묶어 Alibaba Cloud 저장소로 올린다는 사실이 역공학 분석으로 드러났습니다. 모델 학습 허용과 저장소 인덱싱 설정을 꺼도 업로드는 계속됐습니다.
분석 대상 345MB 작업 공간 중 86.6%가 `.git` 데이터였습니다. 과거 커밋에서 지운 API 키나 푸시하지 않은 브랜치 이름까지 넘어갈 수 있다는 뜻입니다. 업로드 파일은 암호화되지만 복호화 키는 서버에만 있어 사용자 보호 장치는 되지 못합니다.
GLM 가중치가 공개돼 있다고 해서 주변 앱까지 믿을 수 있는 건 아니라는 점에서, 코딩 에이전트 선택 기준을 다시 생각하게 하는 사례입니다.

관련: [Tokenstead 분석](https://tokenstead.ai/guides/zcode-silent-git-history-upload) · [GeekNews](https://news.hada.io/topic?id=33902)

### 8. [개인정보 대량 유출 과징금, 매출의 최대 10%로 상향](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899)

9월 11일 시행된 개정 개인정보보호법에 따라, 고의나 중대한 과실로 1,000만 명 이상의 개인정보를 유출한 기업은 전체 매출의 최대 10%를 과징금으로 낼 수 있습니다. 기존 상한은 3%였습니다.
유출이 확정되지 않아도 노출 가능성이 높으면 72시간 안에 이용자에게 알려야 하고, 일정 규모 이상 기업은 개인정보 보호책임자를 선임하거나 바꿀 때 이사회 승인을 받아야 합니다. 대신 사전 보호 투자와 신속한 대응에는 각각 최대 40%까지 감경해 줍니다.
지난 6월 3,755만 명 유출로 6,246억 원을 부과받은 쿠팡 사례에 새 기준을 적용하면 수조 원대가 될 수 있습니다. 지난주 티빙 유출 사고와 맞물려 보안 투자를 비용이 아닌 필수로 보게 만드는 변화입니다.

관련: [GeekNews](https://news.hada.io/topic?id=33911)

### 9. [Apple, 센서 단계부터 서명하는 '진짜 사진' 인증 기술 Reference Image 공개](https://security.apple.com/blog/apple-reference-image/)

AI로 만든 이미지와 실제 사진을 구분하기 어려워지자 Apple이 iPhone 18 Pro 메인 카메라에 'Apple Reference Image' 모드를 넣었습니다. 촬영 시각이 기록된 참조 이미지가 실제 센서로 찍은 사진임을 보증하는 옵트인 기능입니다.
기존 C2PA 방식은 촬영 뒤에 출처 메타데이터를 붙이기 때문에 편집 과정 중간에 뚫리면 알 수 없고, 기기나 촬영자 신원이 드러나는 문제도 있었습니다. Apple은 센서가 전용 모드로 부팅해 캡처 직후 픽셀에 서명하는 '디지털 네거티브'를 만들고, 이를 Private Cloud Compute에서 현상하는 두 단계 구조를 택했습니다.
두 사진이 같은 기기에서 찍혔는지 외부에서 알 수 없고, 위조가 발견되면 촬영자 신원을 노출하지 않고 해당 이미지를 폐기할 수 있습니다.

관련: [요즘IT 해설](https://yozm.wishket.com/magazine/detail/3953)

### 10. [Homebrew 7.0.0 출시…GUI 앱, 취약점 검사, Intel Mac은 Tier 3로](https://brew.sh/2026/09/13/homebrew-7.0.0/)

Homebrew가 메이저 버전 7.0.0을 냈습니다. 다운로드와 설치 준비를 동시에 진행해 `brew install`, `brew upgrade`, `brew bundle`이 빨라졌고, 샌드박스가 강화됐으며, 터미널 없이 패키지를 검색하고 설치하는 공식 GUI 앱 BrewUI가 나왔습니다.
보안 쪽에서는 취약점 검사와 보안 권고 데이터베이스가 기본으로 들어갔습니다. 여러 AI 에이전트가 패키지를 알아서 설치하는 요즘 흐름에서 반가운 변화입니다.
맥 사용자라면 지원 정책 변화를 챙겨야 합니다. macOS 10.15 지원이 끝났고, Intel Mac은 Tier 3로 내려가 새 바틀이 나오지 않습니다. 2027년 9월 1일 이후에는 Intel Mac에서 Homebrew가 동작하지 않으므로 MacPorts로 옮기라고 안내하고 있습니다.

---

## 🚀 Indie Radar
{: #indie-radar}

### [fugleramme](https://github.com/arnegiacomo/fugleramme) · 오픈소스 하드웨어 · Show HN 주간 1위 (2,331점)

노르웨이 베르겐의 개발자가 만든 e-ink 액자로, 창밖에서 들리는 새소리를 인식해 그 새를 1800년대 박물화 스타일로 보여줍니다. Raspberry Pi 5와 마이크, 13.3인치 컬러 e-ink 패널로 구성되고, 새 판별은 BirdNET-Go가 로컬에서 처리합니다.
400종 이상, 800여 개의 그림은 모두 퍼블릭 도메인 박물화에서 직접 오려낸 것으로 AI 생성 그림은 쓰지 않았습니다. 큰 새일수록 가운데에 크게 배치하고, 새가 없으면 빈 횃대만 남깁니다. 이번 주 HN 전체에서 가장 많은 점수를 받았습니다.

### [InFlightSimulator](https://inflightsimulator.com) · 웹 토이 · Show HN 442점

조종사가 아니라 승객이 되는 비행 시뮬레이터입니다. 이륙부터 착륙까지 창밖을 바라보며 세계 어디로든 날아갈 수 있고, 지형과 날씨, 실시간 태양 위치가 반영됩니다.
최신 버전에는 '다리'가 생겨 장거리 비행 중 일어나 화장실에 갈 수도 있습니다. HN에서 댓글이 200개 넘게 달렸습니다.

### [Capsule](https://withcapsule.app/) · 데스크톱 앱 · Show HN 377점

HTML 앱과 그 데이터를 SQLite 파일 하나에 담아 주고받게 해주는 도구입니다. Rust와 Tauri 2.0으로 만들었고, 데이터는 localStorage 방식이나 MongoDB와 비슷한 컬렉션 API로 파일 안에 저장됩니다.
HTML 페이지는 이제 쉽게 만들 수 있는데 데이터를 저장하고 공유하려면 호스팅이 필요하다는 불편에서 출발했습니다. 문서는 기본적으로 파일 시스템에 접근할 수 없고 인터넷 연결도 권한이 필요합니다. 1.0에서 파일 형식 명세를 공개할 계획이라고 합니다.

### [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) · 오픈소스 · GitHub 주간 ★11.7k

브라우저에서 돌아가는 '정찰 위성 시뮬레이터'인데, 데이터는 실제 공개 정보입니다. 실사 3D 지구본 위에 항공기, 선박, 위성, 지진, 공개 CCTV 등을 실시간으로 띄우고, 실시간 AI 에이전트로 음성 조작도 할 수 있습니다.
유튜브 조회 500만 회가 넘은 영상 시리즈에서 시작된 프로젝트로, API 키 없이도 로컬에서 바로 실행됩니다. 교통 흐름은 실제 도로 위에 시뮬레이션한 것이고, 레이어마다 모듈로 나뉘어 있어 데이터 소스를 직접 추가할 수 있습니다.

### [Capgo](https://trustmrr.com/startup/capgo) · 오픈소스 SaaS · MRR $30.9k (TrustMRR 인증)

Capacitor 앱을 앱스토어 심사 없이 라이브 업데이트할 수 있게 해주는 오픈소스 서비스입니다. 긴급 수정이 필요한데 심사 대기로 발이 묶이는 문제를 해결합니다.
최근 30일 매출은 $39,908, 누적 매출은 $53.2만, 30일 성장률은 +24.5%입니다. 외부 투자 없이 운영하는 개발자 도구가 꾸준히 성장하는 사례입니다.

### [POST BRIDGE](https://trustmrr.com/startup/post-bridge) · SaaS · MRR $49.8k (TrustMRR 인증)

콘텐츠 하나를 여러 소셜 미디어에 한 번에 올려주는 서비스입니다. 기능만 보면 흔한 도구지만 요금제를 월 $29~$99로 단순하게 가져가며 꾸준히 커지고 있습니다.
최근 30일 매출은 $48,848, 누적 매출은 $49.7만, 30일 성장률은 +27.3%입니다. MRR과 실제 30일 매출이 거의 일치하는, 안정적인 구독 구조입니다.

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [바이올렛의 생애](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400245500) · 버지니아 울프 · 지식의날개 (주간 12위)
  - [재이](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401662202) · 조남주 · 문학동네 (주간 13위)
  - [쥬디 할머니 (한지 에디션)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401944215) · 박완서 · 문학동네 (주간 16위)
- 주목할 신간
  - [접경지대](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402275216) · 제럴드 머네인 · 문학동네 · 2018 호주 총리상 수상작
  - [절대 쫄지 마](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402254385) · 스티븐 킹 · 황금가지

### IT

- 베스트 새 진입
  - [뚝딱 바로 써먹는 AI 3대장 챗GPT·제미나이·클로드](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=396078233) · 코리아교육그룹 교육연구소 · 안경다리북스 (주간 6위)
  - [이게 되네? 제미나이 완전 미친 활용법 81제](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=385348854) · 오힘찬 · 골든래빗 (주간 13위)
  - [클로드 에이전트 협업의 기술](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=398723910) · 조쉬(김승권) · 한빛미디어 (주간 18위)
- 주목할 신간
  - [케라스 창시자에게 배우는 딥러닝 (개정 3판)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402287241) · 프랑소와 숄레, 매튜 왓슨 · 길벗 · 텐서플로, 파이토치, JAX, 케라스 실전 지침서
  - [한 땀 한 땀! 나의 첫 AI 에이전트](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402480800) · 허정준, 송영희 · 책만 · 바닥부터 만들며 배우는 AI 에이전트와 컨텍스트 엔지니어링

### 인문

- 베스트 새 진입
  - [박완서의 낱말들](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401813692) · 박완서 · 웅진지식하우스 (주간 3위)
  - [대체 ADHD가 뭐길래](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400711238) · 알렉스 코너, 제임스 브라운 · 미래의창 (주간 12위)
  - [편집자의 책읽기](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401357200) · 김영준 · 글항아리 (주간 16위)
- 주목할 신간
  - [읽는 인간](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402259894) · 오에 겐자부로 · 상상스퀘어 · 노벨문학상 수상 작가의 마지막 독서 강의
  - [주의를 기울이는 법](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402344037) · 롭 워커 · 마주

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
