---
layout: post
title: "주간 테크/개발 뉴스 #2026 8/16 ~ 8/22"
date: 2026-08-22
categories: [normal]
tags: [weekly, links, dev-news]
---

## 이번 주 pick!

**1. ["챗GPT 등장 이후 웹페이지 35%에 AI 흔적"...인터넷 생태계 지각변동](https://www.aitimes.com/news/articleView.html?idxno=214213)**

퓨 리서치 센터가 Common Crawl에서 영어 웹페이지 50만 개를 추려 분석한 결과, 챗GPT 출시 이후 만들어진 페이지의 35%에서 AI 작성 흔적이 나왔습니다.
흥미로운 건 도메인별 편차입니다. `.com`이 `.edu`·`.gov`(약 1%)보다 열 배가량 높아, AI 글쓰기가 상업적 콘텐츠 쪽으로 확연히 쏠려 있다는 게 드러납니다.
엠대시(`—`, 문장을 끊고 삽입할 때 쓰는 긴 가로줄)와 옥스포드 콤마(`eggs, toast, and juice`처럼 마지막 `and` 앞에 찍는 쉼표) 빈도 같은 문체 지표까지 같이 움직인다는 관찰도 붙었습니다. 둘 다 잘 교정된 출판물에서 흔한 격식체 표식이라, 그런 텍스트를 대량으로 학습한 모델의 습관이 그대로 웹에 번진 셈입니다. 다만 퓨 리서치 스스로 "절대적 수치로 읽지 말라"며 탐지기의 오탐 가능성을 단서로 달았으니, 35%라는 숫자보다 방향성을 보는 편이 안전합니다.
학습 데이터든 검색 결과든 결국 이 웹을 다시 읽게 된다는 점에서 남 일이 아닙니다.

**2. [익명 'Ox 알파' 등장…코딩 성능·100조 토큰 무상 제공에 '발칵'](https://www.aitimes.com/news/articleView.html?idxno=214249)**

정체를 밝히지 않은 프론티어급 모델이 오픈라우터에 스텔스로 올라왔습니다. 컨텍스트 100만 토큰, 최대 출력 131,072토큰에 텍스트·이미지·영상을 받고, 에이전틱 연산과 소프트웨어 엔지니어링 추론에 특화됐다고 소개합니다.
화제가 된 건 조건입니다. 일주일간 하루 100조 토큰을 공짜로 풉니다. 딥SWE 벤치마크에서 80%로 Claude 3.7(65%)과 GPT-5.6 Sol(52%)을 앞섰다는 결과도 돌았는데, 113문항 중 10문항만 돌린 표본이라 그대로 믿긴 이릅니다.
정체는 토크나이저 특성과 중국 민감 주제 거절 방식이 GLM 계열과 닮았다는 이유로 지푸 AI(Z.ai) 차세대 모델 필드 테스트라는 관측이 우세하고, MS의 MAI 계열이라는 설도 있습니다.
평가는 갈립니다. 100만 토큰 물려도 복잡한 코딩을 매끄럽게 해낸다는 호평과, 단순 작업에도 추론을 과하게 오래 끈다는 혹평이 같이 나옵니다. 다만 진짜 관전 포인트는 성능보다 익명으로 풀고 토큰을 무한정 뿌리는 방식 자체가 기존 벤더의 과금 구조에 어떤 압력을 넣느냐입니다.

---

## AI


- [Claudette - Claude의 BuzzFeed식 말투를 평범한 영어로 바꾸는 도구](https://news.hada.io/topic?id=32767)



- [Vomit - Claude의 장황한 출력을 로컬 LLM으로 짧게 정리해주는 도구](https://news.hada.io/topic?id=32764)



- [나는 AI가 쓴 글을 자동으로 무시하기 시작했다](https://news.hada.io/topic?id=32760)



- [Computer Use와 Skills/Files API로 프로덕션 에이전트 구축하기](https://news.hada.io/topic?id=32754)



- [Huggingface Speech To Speech - 오픈소스 모델로 로컬 음성 에이전트를 만드는 파이프라인](https://news.hada.io/topic?id=32753)



- [AI 에이전트의 제3자 침해 사례를 집계하는 Felony Bench](https://news.hada.io/topic?id=32746)



- [DeepSeek-v4-flash-vision-exp 비전 API](https://news.hada.io/topic?id=32741)



- [AI 기업이 실물 책을 파괴한다 — 너무 늦기 전에 희귀 도서를 스캔하자](https://news.hada.io/topic?id=32738)



- [앤트로픽, '미소스 5' 적용 범위 확대…악용 차단하고 사이버 방어 지원](https://www.aitimes.com/news/articleView.html?idxno=214242)



- [오픈AI, 'GPT-5.6 솔'까지 가격 일시 인하...코덱스 사용자 2천만 돌파](https://www.aitimes.com/news/articleView.html?idxno=214240)



- ["챗GPT 등장 이후 웹페이지 35%에 AI 흔적"...인터넷 생태계 지각변동](https://www.aitimes.com/news/articleView.html?idxno=214213)



- [휴먼 랩스, 피지컬 AI 전용 '인간 데이터' 플랫폼 구축...로봇 스킬 학습 가속](https://www.aitimes.com/news/articleView.html?idxno=214226)



- [AI 추론 아키텍처, 파일럿 단계에서 결정하라…AI 추론 인프라의 5가지 원칙](https://www.itworld.co.kr/article/4211748/ai-%ec%b6%94%eb%a1%a0-%ec%95%84%ed%82%a4%ed%85%8d%ec%b2%98-%ed%8c%8c%ec%9d%bc%eb%9f%bf-%eb%8b%a8%ea%b3%84%ec%97%90%ec%84%9c-%ea%b2%b0%ec%a0%95%ed%95%98%eb%9d%bc-ai-%ec%b6%94%eb%a1%a0-%ec%9d%b8.html)



- [공격엔 앞서고 방어엔 뒤처지는 AI 코딩, 얼마나 안전한가](https://www.itworld.co.kr/article/4211249/%ea%b3%b5%ea%b2%a9%ec%97%94-%ec%95%9e%ec%84%9c%ea%b3%a0-%eb%b0%a9%ec%96%b4%ec%97%94-%eb%92%a4%ec%b2%98%ec%a7%80%eb%8a%94-ai-%ec%bd%94%eb%94%a9-%ec%96%bc%eb%a7%88%eb%82%98-%ec%95%88%ec%a0%84%ed%95%9c.html)



- [보이지 않는 클로드 텍스트 워터마크, 단어 선택에도 개입하는가](https://www.itworld.co.kr/article/4210764/%eb%b3%b4%ec%9d%b4%ec%a7%80-%ec%95%8a%eb%8a%94-%ed%81%b4%eb%a1%9c%eb%93%9c-%ed%85%8d%ec%8a%a4%ed%8a%b8-%ec%9b%8c%ed%84%b0%eb%a7%88%ed%81%ac-%eb%8b%a8%ec%96%b4-%ec%84%a0%ed%83%9d%ec%97%90%eb%8a%94.html)





## Backend


- [더 나은 배터리](https://news.hada.io/topic?id=32750)



- [딥시크, 멀티모달 에이전트 'V4-플래시-비전' 공개...'오퍼스 4.8'에 도전](https://www.aitimes.com/news/articleView.html?idxno=214238)



- [데모 에이전트와 배포 에이전트 사이를 가로막는 5개의 장벽](https://www.itworld.co.kr/article/4212247/%eb%8d%b0%eb%aa%a8-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8%ec%99%80-%eb%b0%b0%ed%8f%ac-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8-%ec%82%ac%ec%9d%b4%eb%a5%bc-%ea%b0%80%eb%a1%9c%eb%a7%89%eb%8a%94-5%ea%b0%9c.html)



- [더 많은 자율성, 더 촘촘한 제약…기업 에이전틱 AI의 외줄타기](https://www.itworld.co.kr/article/4212226/%eb%8d%94-%eb%a7%8e%ec%9d%80-%ec%9e%90%ec%9c%a8%ec%84%b1-%eb%8d%94-%ec%b4%98%ec%b4%98%ed%95%9c-%ec%a0%9c%ec%95%bd%ea%b8%b0%ec%97%85-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8b%b1-ai%ec%9d%98-%ec%99%b8.html)



- [절제가 독이 된 애플, AI 시대의 주가 역설](https://www.itworld.co.kr/article/4211266/%ec%a0%88%ec%a0%9c%ea%b0%80-%eb%8f%85%ec%9d%b4-%eb%90%9c-%ec%95%a0%ed%94%8c-ai-%ec%8b%9c%eb%8c%80%ec%9d%98-%ec%a3%bc%ea%b0%80-%ec%97%ad%ec%84%a4.html)



- [“되돌릴 수 있다면, 검토도 가볍게” 변경 관리 경량화의 조건](https://www.itworld.co.kr/article/4210774/%eb%90%98%eb%8f%8c%eb%a6%b4-%ec%88%98-%ec%9e%88%eb%8b%a4%eb%a9%b4-%ea%b2%80%ed%86%a0%eb%8f%84-%ea%b0%80%eb%b3%8d%ea%b2%8c-%eb%b3%80%ea%b2%bd-%ea%b4%80%eb%a6%ac-%ea%b2%bd%eb%9f%89%ed%99%94.html)





## Infra/Cloud


- [메타, MS '애저' 최대 고객사로 부상...빅테크 ‘AI 순환 의존’ 심화](https://www.aitimes.com/news/articleView.html?idxno=214222)





## Tools


- [Tool: TanStack Table v9](https://tanstack.com/blog/announcing-tanstack-table-v9?ref=console.dev)



- [Beta: Saggar](https://saggar.marginalutility.dev?ref=console.dev)



- [Beta: TermDOM](https://termdom.org/?ref=console.dev)



- [Beta: OpenLogi](https://openlogi.org?ref=console.dev)



- [커서, 장기 목표 기능 '/goal' 도입...스스로 작업하는 자율 에이전트 진화](https://www.aitimes.com/news/articleView.html?idxno=214205)



- [씨클리너 위장 악성코드, 크롬을 자격증명 탈취 감시 도구로 악용](https://www.itworld.co.kr/article/4210717/%ec%94%a8%ed%81%b4%eb%a6%ac%eb%84%88-%ec%9c%84%ec%9e%a5-%ec%95%85%ec%84%b1%ec%bd%94%eb%93%9c-%ed%81%ac%eb%a1%ac%ec%9d%84-%ec%9e%90%ea%b2%a9%ec%a6%9d%eb%aa%85-%ed%83%88%ec%b7%a8-%ea%b0%90%ec%8b%9c.html)





## GitHub Trending


- [cursor/plugins](https://github.com/cursor/plugins)<br>이 프로젝트는 인기 있는 개발 도구, 프레임워크, SaaS 제품과 연동하는 공식 Cursor plugins 모음집으로, 각 플러그인은 `.cursor-plugin/plugin.json` 매니페스트를 가진 독립 디렉토리 형태로 제공됩니다. Gmail, GitHub, Salesforce, Playwright 등 생산성·연동 도구부터 pr-review-canvas, orchestrate, thermos 같은 개발자용 워크플로 도구까지 다양한 카테고리를 아우르며, MCP 서버 정의와 skills, rules를 포함해 에이전트 기반 개발 경험을 확장합니다. 단일 저장소에서 marketplace.json으로 전체 플러그인을 관리하는 구조라 새 플러그인을 추가하거나 기존 플러그인을 참고하기 쉽습니다.



- [cordiverse/cordis](https://github.com/cordiverse/cordis)<br>Cordis는 시공간적 조합 가능성(spatiotemporal composability)이라는 개념을 중심으로 설계된 메타 프레임워크(meta-framework)로, 플러그인/모듈 간의 생명주기와 의존성을 동적으로 구성·관리할 수 있게 해줍니다. 아직 활발히 개발 중이며 API가 안정화되지 않아 예고 없이 변경될 수 있다는 점이 특징입니다. 기존 프레임워크와 달리 시간적·공간적 조합성이라는 새로운 프로그래밍 패러다임을 제시한다는 점에서 주목할 만합니다.



- [volcengine/OpenViking](https://github.com/volcengine/OpenViking)<br>OpenViking은 AI 에이전트를 위한 오픈소스 컨텍스트 데이터베이스로, 메모리·리소스·스킬을 `viking://` 프로토콜 기반의 단일 가상 파일시스템으로 통합해 에이전트가 블랙박스 벡터 검색 대신 `ls`, `tree`, `find` 같은 방식으로 자신의 컨텍스트를 탐색할 수 있게 합니다. 콘텐츠를 L0(요약)·L1(개요)·L2(상세) 3단계로 처리해 필요한 깊이만큼만 로드함으로써 토큰 사용량을 줄이고, 모든 검색 과정의 경로(trajectory)를 추적·디버깅할 수 있는 관찰 가능성(observability)을 제공합니다. LoCoMo 및 tau2-bench 벤치마크에서 기존 에이전트 메모리 솔루션 대비 우수한 성능을 보고하고 있습니다.



- [basecamp/omarchy](https://github.com/basecamp/omarchy)<br>Omarchy는 DHH가 만든 아름답고 현대적인 Linux distribution으로, Hyprland 기반의 opinionated한 데스크톱 환경과 세심하게 큐레이션된 앱·설정을 기본 제공합니다. 터미널, Neovim, AI 도구, 테마, 단축키 등 개발자 워크플로우 전반을 통합한 상세한 manual을 갖추고 있어 별도의 설정 없이 바로 생산적인 환경을 구축할 수 있다는 점이 특징입니다. 유명 개발자(DHH, Basecamp/37signals 창업자)가 직접 설계한 배포판이라는 점과 Mac/Windows 사용자의 전환을 배려한 문서화가 주목할 만합니다.



- [modular/modular](https://github.com/modular/modular)<br>Modular Platform은 AI 개발과 배포를 위한 통합 오픈소스 플랫폼으로, 고성능 AI 커널·모델을 다루는 **MAX Framework**와 시스템급 성능을 지향하는 **Mojo Language**를 핵심으로 제공합니다. Mojo 컴파일러, Mojo 표준 라이브러리, MAX 가속기 라이브러리, OpenAI 호환 추론 서버, Python 기반 모델 파이프라인 등 AI 스택 전반의 핵심 컴포넌트를 하나의 저장소에서 오픈소스로 공개하고 있습니다.



- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)<br>MoneyPrinterTurbo는 영상 주제나 키워드만 입력하면 AI가 스크립트 작성부터 소재 매칭, 자막, 배경음악까지 자동으로 처리해 고화질 숏폼 영상을 완성하는 원스톱 AI 영상 생성 도구입니다. AI Agent, WebUI, API, CLI 등 다양한 사용 방식을 지원하며, Edge TTS, Azure Speech, ElevenLabs 등 다양한 TTS 엔진과 Pexels, Pixabay 등 무료 소재 및 WaveSpeed AI 기반 AI 소재 생성까지 폭넓게 연동됩니다. 오픈소스로 누구나 손쉽게 대량의 숏폼 콘텐츠를 자동 생산할 수 있다는 점에서 크리에이터와 마케터들 사이에서 주목받고 있습니다.



- [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)<br>OpenLogi는 Rust와 GPUI로 개발된 오픈소스 로컬 우선(local-first) 애플리케이션으로, Logitech Options+의 대안으로서 HID++와 UVC를 통해 Logitech 마우스, 키보드, 웹캠의 버튼 리매핑, DPI/제스처, RGB 조명, 카메라 이미지 제어 등 다양한 기능을 지원한다. macOS, Linux, Windows 전 플랫폼을 네이티브로 지원하며 특히 Linux를 1급 플랫폼으로 대우하고, 설정을 TOML 평문 파일로 관리하며 GUI 외에 CLI도 제공한다는 점이 특징이다. 아직 활발히 개발 중인 프로젝트지만 가벼운 리소스 사용, 강력한 커스터마이징, 크로스 플랫폼 지원으로 Options+를 대체할 만한 선택지로 주목받고 있다.



- [public-apis/public-apis](https://github.com/public-apis/public-apis)<br>public-apis/public-apis는 개발자들이 자신의 프로젝트에 활용할 수 있는 다양한 도메인(날씨, 금융, 위치정보, 이미지 등)의 무료 및 공개 API를 커뮤니티가 직접 큐레이션하여 정리한 대규모 목록 저장소입니다. 각 API는 카테고리별로 분류되어 있으며 인증 방식, HTTPS 지원 여부, CORS 지원 여부 등의 정보를 함께 제공해 실무 적용 시 빠르게 판단할 수 있도록 돕습니다.






- [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)<br>AI 코딩 에이전트를 위한 장기 기억 도구로, Claude Code, Codex 등 서로 다른 에이전트나 세션을 오가도 아키텍처, 시도했던 접근법, 미해결 질문 등을 잊지 않고 이어갈 수 있게 해준다. MCP 설정과 라이프사이클 훅을 통해 Linux, macOS, Windows(WSL2/네이티브)는 물론 Claude Code, Codex, Cursor, Gemini CLI, Devin 등 매우 폭넓은 에이전트/플랫폼을 지원하며, 일부 에이전트에는 세션 간 컨텍스트를 자동으로 이어주는 "managed workstream" 기능까지 제공한다. 특정 벤더에 종속되지 않고 다양한 CLI 코딩 에이전트 생태계 전반을 아우르는 공용 메모리 계층을 지향한다는 점이 주목할 만하다.



- [GitHub Developer: Shaw (@lalalune)](https://github.com/lalalune)






- [GitHub Developer: Julien Dubois (@jdubois)](https://github.com/jdubois)



- [GitHub Developer: Serena (@serenakeyitan)](https://github.com/serenakeyitan)



- [GitHub Developer: anionex (@Anionex)](https://github.com/Anionex)



- [GitHub Developer: Dr_rOot (@agalwood)](https://github.com/agalwood)



- [GitHub Developer: Fabio Akita (@akitaonrails)](https://github.com/akitaonrails)









- [GitHub Developer: Tobias Lütke (@tobi)](https://github.com/tobi)





## Etc


- [Tool: TurboVec](https://github.com/RyanCodrai/turbovec?ref=console.dev)



- [Beta: Hotkeys](https://tanstack.com/hotkeys/latest?ref=console.dev)



- [Beta: Needle](https://github.com/cactus-compute/needle?ref=console.dev)



- [Labor0를 만든 이유](https://news.hada.io/topic?id=32769)



- [채용 공고 1만 건에서 뽑아낸 ‘AI 엔지니어링 스킬 맵’](https://yozm.wishket.com/magazine/detail/3909)



- [요즘 클로드가 한국어를 어색하게 쓴다고 느꼈다면](https://yozm.wishket.com/magazine/detail/3908)



- [출근하면 코드부터 짜던 개발자가 이제 봇부터 켭니다](https://yozm.wishket.com/magazine/detail/3906)



- [AI-UX 포트폴리오 제작할 때 체크 포인트 7가지](https://yozm.wishket.com/magazine/detail/3905)



- [Orca vs. Paseo vs. 순정: 에이전트 관리 도구 비교하기](https://yozm.wishket.com/magazine/detail/3903)



- [모두가 AI 네이티브한다고 하지만, ‘진짜’는 아직 없다](https://yozm.wishket.com/magazine/detail/3902)



- [자동화할 일을 고르는 것도 실력이다](https://yozm.wishket.com/magazine/detail/3890)



- [익명 'Ox 알파' 등장…코딩 성능·100조 토큰 무상 제공에 '발칵'](https://www.aitimes.com/news/articleView.html?idxno=214249)


- [실수하는 AI 개발자, 그래도 채용해야 하는 이유](https://www.itworld.co.kr/article/4211725/%ec%8b%a4%ec%88%98%ed%95%98%eb%8a%94-ai-%ea%b0%9c%eb%b0%9c%ec%9e%90-%ea%b7%b8%eb%9e%98%eb%8f%84-%ec%b1%84%ec%9a%a9%ed%95%b4%ec%95%bc-%ed%95%98%eb%8a%94-%ec%9d%b4%ec%9c%a0.html)



- [카메라 없이도 침입 감지, 라우터가 감시 장치로 진화하는 시대](https://www.itworld.co.kr/article/4211719/%ec%b9%b4%eb%a9%94%eb%9d%bc-%ec%97%86%ec%9d%b4%eb%8f%84-%ec%b9%a8%ec%9e%85-%ea%b0%90%ec%a7%80-%eb%9d%bc%ec%9a%b0%ed%84%b0%ea%b0%80-%ea%b0%90%ec%8b%9c-%ec%9e%a5%ec%b9%98%eb%a1%9c-%ec%a7%84%ed%99%94.html)



- [Rust Glancer - 메모리를 100배 적게 쓰는 Rust LSP](https://news.hada.io/topic?id=32768)



- [Show GN: Three.js로 만든 일본 오늘의 운세 체험](https://news.hada.io/topic?id=32762)



- [소프트웨어가 더 이상 느릴 이유는 없다](https://news.hada.io/topic?id=32761)



- [SSL에 대해 배운 모든 것이 더는 유효하지 않음 [유튜브]](https://news.hada.io/topic?id=32756)



- [YC CEO Garry Tan이 말하는 창업자의 새로운 규칙 [유튜브]](https://news.hada.io/topic?id=32755)





