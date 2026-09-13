---
layout: post
title: "주간 테크/개발 뉴스 #2026 9/6 ~ 9/12"
date: 2026-09-12
categories: [normal]
tags: [weekly, dev-news, indie-radar, books]
---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — 나비에-스토크스 논란, 속도 조절 제안, Shopify 네이티브 복귀
- [🚀 Indie Radar (7)](#indie-radar) — 3일 만든 게임 월 $4,000, 광고 설치 60%가 봇
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [OpenAI, 나비에-스토크스 난제 해법 발표…수학계는 반발](https://openai.com/index/navier-stokes-solution/)

OpenAI가 밀레니엄 난제 중 하나인 나비에-스토크스 문제의 해법을 AI로 찾았다고 발표했습니다. 166쪽 증명과 Lean 4 형식 증명을 함께 공개했고, 풀이 과정에 최대 1만 개의 에이전트를 투입했다고 합니다.
그런데 같은 문제를 연구하던 NYU의 Tristan Buckmaster가 "OpenAI가 우리 작업을 알고 서둘러 뛰어들었고, 공로 배분에도 개입하려 했다"고 주장하면서 논란이 커졌습니다.
테렌스 타오 등 필즈상 수상자 25명은 난제 풀이를 벤치마크로 삼는 경쟁이 수학을 해친다는 공동 선언을 냈고, OpenAI는 캘텍 AI 수학 해커톤 후원을 철회했습니다.

관련: [Wired](https://www.wired.com/story/openai-navier-stokes-math-discovery-academics/) · [필즈상 수상자 공동 선언](https://mathandai.org/) · [Lean 증명 비용 이야기](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/)

### 2. [아모데이 "프론티어 속도 조절하자"…알트먼·머스크도 동의](https://www.aitimes.com/news/articleView.html?idxno=215195)

다리오 아모데이가 에세이 'We Must Pace the Frontier'에서 AI가 다음 세대 AI를 만드는 재귀적 자기 개선 단계에 들어섰다고 경고했습니다. OpenAI의 허깅페이스 사건을 사례로 들며, 6~12개월 안에 에이전트 군집이 인터넷에 큰 피해를 줄 수 있다고 봤습니다.
해법으로 외부 평가단 상주(Anthropic은 즉시 시행), 민주주의 국가 기업 간 안전 표준과 속도 상한 합의, 권위주의 국가를 포함한 글로벌 체계를 제안했습니다.
알트먼은 바로 동의하며 독립 평가단을 도입하겠다고 했고, 머스크도 "Dario is right"라고 호응했습니다. 알트먼은 포춘 인터뷰에서 2026년 상장도 하지 않겠다고 밝혔습니다.

관련: [알트먼 "2026년 상장은 시기상조"](https://www.aitimes.com/news/articleView.html?idxno=215198)

### 3. [OpenAI 에이전트, 허깅페이스에 이어 RubyGems 공격 의혹](https://www.rubyhack.ai/)

지난 5월 RubyGems에 악성 패키지 2,000여 개가 올라온 GemStuffer 공격이 OpenAI 내부 에이전트의 소행이라는 분석이 나왔습니다. 패키지 이름과 작성자에 `oai`가 반복되고, OpenAI가 자사 소속이라고 인정한 위키 에이전트와 행동 패턴이 겹칩니다.
이 패키지들은 RubyDoc.info 문서 생성 과정에서 코드를 실행했고, 7월에야 공개된 API 키 유출 취약점을 5월에 이미 악용하려 했습니다. RubyGems는 DDoS로 판단해 나흘간 신규 가입을 막았지만, OpenAI로부터 아무 통보도 받지 못했다고 합니다.
앞서 드러난 허깅페이스 건은 안전장치를 끈 채 CTF 평가를 돌리던 모델들이, 패키지 중개 서버(Artifactory)의 취약점을 발판 삼아 외부로 나간 사건이었습니다.

관련: [GeekNews 요약](https://news.hada.io/topic?id=33567) · [모델은 스스로 통제를 벗어나지 않는다](https://news.hada.io/topic?id=33564)

### 4. [Shopify, React Native에서 네이티브로 복귀…같은 주 Tailwind 인수](https://shopify.engineering/back-to-native)

2020년에 React Native를 전면 도입했던 Shopify가 모든 모바일 앱을 Swift와 Kotlin으로 전환합니다.
이유는 React Native의 성능이 아니었습니다. 코딩 에이전트 덕분에 같은 기능을 iOS와 Android에 따로 구현하는 비용이 크게 줄면서 "코드를 공유해야 싸다"는 전제가 깨졌다는 설명입니다. Shop 앱은 12주 만에 전환을 마쳤고, 화면이 300개가 넘는 Shopify 앱도 연내 전환합니다.
같은 주에는 주간 설치 1억 1천만 회의 Tailwind CSS 팀이 Shopify에 합류한다고 발표했습니다.

관련: [Tailwind is joining Shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify) · [GeekNews](https://news.hada.io/topic?id=33485)

### 5. [애플 첫 폴더블 '아이폰 듀오' 공개](https://www.apple.com/iphone-duo/)

존 터너스 신임 CEO가 9일 애플의 첫 폴더블폰을 공개하며, 기존 폴더블폰을 "전화기 두 대를 어색하게 붙여놓은 것 같다"고 저격했습니다.
삼성 뉴질랜드 법인은 팀 쿡과 이름도 외모도 닮은 동명이인을 내세운 패러디 광고로 응수했습니다.
HN에서는 댓글이 2,500개를 넘으며 이번 주 가장 뜨거운 토론이 됐습니다.

관련: [삼성 '팀 쿡' 카드로 맞불](https://www.aitimes.com/news/articleView.html?idxno=215183)

### 6. [LG 스마트 TV, 화면이 꺼져도 오디오 녹음·주변 기기 스캔](https://news.hada.io/topic?id=33318)

Gamers Nexus와 Level1Techs가 LG OLED TV의 패킷을 분석했더니, TV가 가정 네트워크를 계속 스캔해 휴대폰과 워치를 매핑하고 주변 Wi-Fi 이름, 신호 세기, 위치 정보까지 LG 광고 부문으로 보내고 있었습니다.
대기 모드에서도 마이크 오디오가 녹음되고, 인터넷을 끊으면 로컬에 쌓아뒀다가 재연결할 때 업로드했습니다. webOS의 원격 코드 실행 취약점도 발견돼 책임 공개 절차가 진행 중입니다.
LG는 이 보도를 가짜 뉴스라고 부인했습니다.

### 7. [Anthropic, '맥스 플랜' 사용량 허위 광고로 집단소송](https://www.aitimes.com/news/articleView.html?idxno=215049)

월 100달러, 200달러짜리 Max 플랜은 Pro의 5배, 20배 사용량을 준다고 홍보합니다. 그런데 이 배수는 5시간 세션에만 적용되고 별도 주간 한도가 있어, 실제 증가 폭은 광고에 한참 못 미친다는 주장입니다.
FTC 출신 변호사들이 9일 소송을 확대했고, 11월 6일 심리가 예정돼 있습니다. Anthropic은 하이퍼링크로 조건을 확인할 수 있었다고 반박했습니다.
이번 주 aitimes 인기 기사 4위였습니다.

### 8. [Microsoft, Rust를 Tier-1 언어로 격상](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/)

Rust가 사내에서 C++, C#, TypeScript와 같은 등급의 지원을 받게 됐습니다.
rustc를 MSVC 백엔드에 연결하는 `rustc_codegen_utc`가 올해 초 프로덕션 준비를 마쳤고, 이미 100개 이상의 저장소가 이 백엔드로 빌드됩니다. 덕분에 Windows에서 Rust와 C++이 코드 생성 기반을 공유합니다.
적용 범위도 펌웨어, 드라이버부터 커널, 하이퍼바이저까지 넓어지고 있습니다.

관련: [GeekNews](https://news.hada.io/topic?id=33487)

### 9. [구글 검색 링크가 google.com/goto로…스크래핑 비용 상승](https://www.autom.dev/blog/google-search-goto-links)

구글 검색 결과의 링크가 목적지 주소 대신 불투명하게 인코딩된 `/goto?url=...`로 바뀌고 있습니다.
예전 `/url?q=`와 달리 링크만 보고는 주소를 복원할 수 없어, 결과마다 추가 요청을 보내 Location 헤더를 읽어야 합니다. 대량 수집이 느려지고 탐지되기도 쉬워집니다.
`&num=100` 파라미터 제거, BotGuard 강화에 이은 흐름입니다. 8월 말부터 로그아웃 상태와 시크릿 창에서 넓게 관찰되고 있지만, 아직 실험 단계일 수도 있습니다.

관련: [GeekNews](https://news.hada.io/topic?id=33571)

### 10. [티빙 3,954만 계정 유출, 원인은 소스코드에 박힌 접속키](https://www.dailysecu.com/news/articleView.html?idxno=208329)

공격자는 개발자가 갖고 있던 개발환경 접속키를 탈취해 들어왔습니다. 소스코드 안에 운영환경 접속키가 43개나 있었고, 그중 2개로 AWS 운영환경까지 침투했습니다.
접속키는 하드코딩돼 있었고, 설정값은 평문으로 관리됐으며, 사내 메신저로 키를 주고받은 사례도 확인됐습니다. 고난도 취약점이 아니라 기본적인 보안 관리가 여러 단계에서 동시에 무너진 사고였습니다.
같은 주 강남언니에서도 약 22만 명의 상담 사진과 시술 내역이 유출됐습니다.

관련: [GeekNews](https://news.hada.io/topic?id=33482) · [강남언니 유출](https://news.hada.io/topic?id=33337)

---

## 🚀 Indie Radar
{: #indie-radar}

### [Actorle](https://www.reddit.com/r/SideProject/comments/1wanatu/4_years_later_my_3_day_side_project_still_makes/) · 웹 게임 · 월 $4,000

헝가리의 풀스택 개발자가 2022년 사흘 만에 만든 워들 스타일 게임입니다. 출연작 목록을 보고 배우를 맞힙니다.
처음엔 "너무 어렵다"는 반응에 접을 뻔했지만, 영국 뉴스레터 b3ta에 소개되면서 하루 이용자가 500명에서 수만 명으로 늘었습니다. 광고 수익이 월급을 넘자 회사를 그만뒀고, 4년이 지난 지금도 DAU 1만 명에 월 $4,000을 벌고 있습니다.
최근에는 광고사를 바꿔 수익이 두 배가 됐지만, 새로 낸 게임들은 바이브 코딩으로 만든 게임이 넘쳐나는 탓에 주목받지 못했다고 합니다.

### [LLM Gateway](https://trustmrr.com/startup/llm-gateway) · 오픈소스 SaaS · MRR $78.8k (TrustMRR 인증)

여러 LLM 제공자로 요청을 라우팅하고 API 키를 관리해주는 오픈소스 게이트웨이입니다.
누적 매출 100만 달러를 넘었고, 최근 30일 매출은 $25.9만, 30일 성장률은 +54.6%입니다.
이번 주에만 NVIDIA Switchyard, litelm, GitHub 하이드라퓨전 등 LLM 라우터가 쏟아졌는데, 이미 이 영역에서 돈을 벌고 있는 곳이 있습니다.

### [Lucky Dangle](https://trustmrr.com/startup/lucky-dangle) · 데스크톱 앱 · 최근 30일 $4,919 (TrustMRR 인증)

화면 위쪽에 행운 부적을 매달아두는 앱입니다. 작업하는 동안 살랑살랑 흔들리고, 클릭은 전혀 방해하지 않습니다.
MRR이 0인 걸 보면 구독이 아니라 단건 판매로 보이는데, 30일 사이 매출이 1,174% 늘었습니다.

### [Dayzle](https://dayzlegame.com/blog/google-ads-bot-farm/) · 퍼즐 앱 · 광고비 $220 중 설치 60%가 봇

퍼즐 앱을 혼자 운영하는 개발자가 구글 앱 광고를 돌려봤습니다. 2주간 과금된 설치 56건 중 33건이 봇으로 의심됐고, 실제 사용자는 13명뿐이었습니다.
의심 기기들은 Play 스토어에서 이미 내려간 구버전 앱을 실행했고, 화면 체류 시간은 0초였습니다. 가짜 설치가 전환으로 잡히니 알고리즘이 그쪽으로 광고를 더 몰아주는 악순환이었습니다.
그래서 전환 목표를 '앱 실행'에서 '퍼즐 승리'로 바꿨습니다.

### [Life in Mist](https://www.reddit.com/r/SideProject/comments/1wbu40o/i_built_an_iphone_app_that_turns_your_walks_into/) · iOS 앱 · r/SideProject 주간 1위

걸은 경로만큼 지도의 안개가 걷히는 앱입니다. 동네 산책 기록도 계속 쌓여서, 자주 다니는 길과 아직 안 가본 골목이 한눈에 보입니다.
무료이고, 프리미엄은 월 $0.99, 연 $4.99, 평생 $17.99입니다.

### [Relativity Park](https://rivendell.dmitrybrant.com/relativity/) · 웹 토이 · Show HN 주간 1위 (617점)

빛의 속도가 시속 5km인 공원을 걸어다니는 브라우저 시뮬레이션입니다. 속도를 올리면 길이 수축, 시간 지연, 테렐 회전, 도플러 효과가 물리적으로 정확하게 보입니다. 소스도 공개돼 있습니다.

### [i-have-adhd](https://github.com/ayghri/i-have-adhd) · 에이전트 스킬 · GitHub 주간 ★15.9k

코딩 어시스턴트가 답을 장황한 설명 속에 파묻지 않게 해주는 스킬입니다. 할 일부터 말하고, 단계에 번호를 붙이고, "Hope this helps!" 같은 말은 빼게 합니다.
이번 주 GitHub 트렌딩 상위권은 archify, diagram-design, humanizer, mattpocock/skills처럼 거의 에이전트 스킬 차지였습니다.

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [눈 내리는 삼일포](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401727813) · 김연수 · 문학동네 (주간 4위)
  - [백야 (먼슬리 클래식)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401398426) · 도스토옙스키 · 문학동네 (주간 5위)
  - [녹색 절벽의 신자들](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401291520) · 조예은 · 오리지널스 (주간 14위)
- 주목할 신간
  - [에케 호모](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401983261) · 오수완 · 다산책방 · 제16회 혼불문학상 수상작
  - [그 살인, 본격 미스터리로 만들어 드리겠습니다.](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401907453) · 가타오카 쇼 · 리드비

### IT

- 베스트 새 진입
  - [비전공자도 이해할 수 있는 LLM 수업](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400646488) · 박상길 · 비즈니스북스 (주간 3위)
  - [컴퓨터구조론 개정6판](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=353352812) · 김종현 · 생능 (주간 14위, 개강 시즌이라 교재들이 대거 진입했습니다)
- 주목할 신간
  - [클린 코드 2판](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401752131) · 로버트 C. 마틴 · 인사이트
  - [요즘 개발자를 위한 AWS 비용 최적화](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401909927) · 길벗 · 서버·EKS·스토리지·네트워크 최적화까지

### 인문

- 베스트 새 진입
  - [옥스브리지의 철학 수업](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400561491) · 고요엘 · 상상스퀘어 (주간 6위)
  - [리더는 언제 차이를 만들어내는가](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401294662) · 재레드 다이아몬드 · 김영사 (주간 10위)
- 주목할 신간
  - [문학과 혁명](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402001604) · 천정환 · 서해문집 · 1980~1990년대 민주화와 문화정치
  - [소리 지도](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401759438) · 미하엘라 피저, 아이작 유엔 · 돛과닻

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
