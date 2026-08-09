---
layout: post
title: "주간 테크/개발 뉴스 #2026 8/2 ~ 8/8"
date: 2026-08-08
categories: [normal]
tags: [weekly, links, dev-news]
---

## 이번 주 pick!

**1. [‘에이전트 플러그인 1.0’ 공개...스킬·MCP 묶어 에이전트 호환성 높여](https://www.aitimes.com/news/articleView.html?idxno=213705)**

지금까지 스킬, MCP 서버, 서브에이전트는 각각 따로 설치하고 따로 관리해야 하는 조각들이었습니다. 이번 규격은 이들을 하나의 플러그인 단위로 묶어 배포·설치·버전 관리를 일원화하자는 제안입니다.
특정 벤더 전용 포맷이 아니라 공용 규격을 지향한다는 점이 핵심으로, 사내에서 만든 에이전트 확장을 팀 전체에 배포하려던 조직에게는 기다리던 소식입니다.
이번 주 GitHub Trending에 오른 OpenWork나 TencentDB Agent Memory 같은 프로젝트들이 모두 "여러 에이전트에서 같은 스킬 재사용"을 내걸고 있다는 점을 보면, 업계가 같은 문제를 동시에 풀고 있다는 게 분명해 보입니다.

**2. [‘클로드’에 백업 맡겼더니 홈 디렉토리 전체 삭제..."미안, 오타였다"](https://www.aitimes.com/news/articleView.html?idxno=213702)**

백업 작업을 맡긴 에이전트가 경로 오타 하나로 홈 디렉토리를 통째로 날린 사건입니다. 실수 자체보다 뼈아픈 건, 사람이라면 `rm -rf`를 실행하기 전 한 번쯤 멈칫할 지점에서 에이전트는 그냥 지나갔다는 사실입니다.
에이전트에게 셸을 쥐여줄 때 승인 게이트와 샌드박스를 어디까지 둘 것인가는 취향 문제가 아니라 안전장치 설계 문제라는 걸 다시 확인시켜 줍니다.
같은 주에 올라온 "아무도 감시하지 않는 AI 에이전트의 보안 위기"와 함께 읽으면 더 좋습니다.

**3. [배치 처리·연산자 융합·SIMD로 Postgres 분석 성능을 300배 높인 pgrust](https://news.hada.io/topic?id=32264)**

분석 쿼리가 느릴 때 대개는 별도 OLAP 저장소로 데이터를 옮기는 길을 택하지만, 이 프로젝트는 Postgres 안에서 실행 엔진 자체를 손봤습니다.
행 단위 처리 대신 배치 처리, 연산자 융합, SIMD를 적용해 최대 300배까지 끌어올린 결과를 공개했습니다.
데이터 파이프라인을 새로 깔기 전에 "지금 쓰는 Postgres에서 얼마나 더 짜낼 수 있는가"를 먼저 따져보고 싶은 팀이라면 읽어볼 만합니다.

---

## AI


- [Tool: Mu](https://github.com/micro/mu?ref=console.dev)



- [Beta: @cloudflare/computer](https://blog.cloudflare.com/cloudflare-computer?ref=console.dev)



- [AI 시험지는 함정이 9할이다 - LLM 테스트 케이스 설계법](https://news.hada.io/topic?id=32270)



- [Paseo - 여러 코딩 에이전트를 데스크톱/모바일에서 관리하는 오케스트레이터](https://news.hada.io/topic?id=32254)



- [Orca - 여러 병렬 코딩 에이전트를 위한 오픈소스 ADE](https://news.hada.io/topic?id=32253)



- [OpenAI를 떠나 Jurassic Park를 만들다](https://news.hada.io/topic?id=32251)



- [Oracle, 사내 AI 코딩은 장려하면서 OpenJDK에는 AI 생성 코드 기여 금지](https://news.hada.io/topic?id=32246)



- [나만의 ‘UX/UI 디자인 피드백봇’ 만들기](https://yozm.wishket.com/magazine/detail/3884)



- [‘에이전트 플러그인 1.0’ 공개...스킬·MCP 묶어 에이전트 호환성 높여](https://www.aitimes.com/news/articleView.html?idxno=213705)



- [[8월7일] “챗GPT 충격 이후 최대 개편”…구글, AI 경쟁 ‘두 번째 대전환’ 나섰다](https://www.aitimes.com/news/articleView.html?idxno=213652)



- ["큐원3.8-맥스, 벤치마크 비해 경쟁력 없어"...AI 모델의 '숨은 비용' 함정](https://www.aitimes.com/news/articleView.html?idxno=213665)



- [오픈AI, '봉제인형'으로 조류 식별하는 오픈소스 프로젝트 '버딩팔' 공개](https://www.aitimes.com/news/articleView.html?idxno=213668)



- [발견한 취약점을 테스트로 남기지 않으면 어떤 일이 벌어지나](https://www.itworld.co.kr/article/4204698/%eb%b0%9c%ea%b2%ac%ed%95%9c-%ec%b7%a8%ec%95%bd%ec%a0%90%ec%9d%84-%ed%85%8c%ec%8a%a4%ed%8a%b8%eb%a1%9c-%eb%82%a8%ea%b8%b0%ec%a7%80-%ec%95%8a%ec%9c%bc%eb%a9%b4-%ec%96%b4%eb%96%a4-%ec%9d%bc%ec%9d%b4.html)



- [ChatGPT, 무료 사용자에게도 GPT‑5.6 Luna 제공 시작](https://news.hada.io/topic?id=32243)



- [AI한테 시험을 냈는데 출제자가 5번 틀렸다 - LLM 파이프라인 검증기](https://news.hada.io/topic?id=32231)





## Backend


- [Tool: syncular](https://syncular.dev/?ref=console.dev)



- [배치 처리·연산자 융합·SIMD로 Postgres 분석 성능을 300배 높인 pgrust](https://news.hada.io/topic?id=32264)



- [Show GN: 외부 AI 결과를 여러 SNS에 예약하고 실제 발행 상태를 추적하는 ANKK](https://news.hada.io/topic?id=32261)



- [23년 동안 살아남은 동네슈퍼를 데이터로 분석해봤습니다](https://yozm.wishket.com/magazine/detail/3883)



- [AI 시대의 엔지니어링: 이 일, 정말 AI에 시켜야 하는가?](https://yozm.wishket.com/magazine/detail/3882)



- [백엔드만의 영역이 아닌 프론트엔드 관찰가능성의 가치](https://www.itworld.co.kr/article/4205485/%eb%b0%b1%ec%97%94%eb%93%9c%eb%a7%8c%ec%9d%98-%ec%98%81%ec%97%ad%ec%9d%b4-%ec%95%84%eb%8b%8c-%ed%94%84%eb%a1%a0%ed%8a%b8%ec%97%94%eb%93%9c-%ea%b4%80%ec%b0%b0%ea%b0%80%eb%8a%a5%ec%84%b1%ec%9d%98.html)



- [zot – 단일 Go 바이너리부터 HA 클러스터까지 확장 가능한 가벼운 OCI Registry](https://news.hada.io/topic?id=32230)





## Infra/Cloud


- [Kitesurf - V8 격리 환경에서 실행되는 에이전트 우선 브라우저](https://news.hada.io/topic?id=32266)



- [Nixpkgs 코어 팀 해산](https://news.hada.io/topic?id=32263)



- [아무도 감시하지 않는 AI 에이전트의 보안 위기](https://www.itworld.co.kr/article/4205492/%ec%95%84%eb%ac%b4%eb%8f%84-%ea%b0%90%ec%8b%9c%ed%95%98%ec%a7%80-%ec%95%8a%eb%8a%94-ai-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8%ec%9d%98-%eb%b3%b4%ec%95%88-%ec%9c%84%ea%b8%b0.html)





## Tools


- [Beta: gh-stack](https://github.com/github/gh-stack?ref=console.dev)



- [Herdr, Y Combinator 합류 후에도 런타임은 오픈소스로 유지](https://news.hada.io/topic?id=32245)





## GitHub Trending


- [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)<br>AI 에이전트가 APK, 바이너리, 프론트엔드 JS 난독화, CTF 문제, 인가된 모의침투 대상을 만났을 때 적절한 보안 스킬로 자동 라우팅해주는 스킬 패키지입니다. 필요한 툴체인을 그때그때 자동으로 부트스트랩하고, 수행 결과를 경험 DB에 축적해 스스로 개선하는 구조가 특징입니다. Claude Code, Kiro, Cursor, Cline 등 주요 AI 코딩 클라이언트를 지원합니다.



- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)<br>텐센트가 공개한 팀 단위 AI 에이전트 메모리 허브로, 대화·문서·코드를 Chat Memory, Skill, LLM-Wiki, Code-Graph라는 네 가지 재사용 가능한 메모리 자산으로 전환합니다. 여러 에이전트와 프레임워크가 이 자산을 공유하고 권한 관리까지 할 수 있어, 에이전트를 쓸 때 반복되는 컨텍스트 설명 작업을 줄이는 것이 목표입니다. memory-core, memory-hub, proxy 세 서비스를 스크립트 하나로 띄울 수 있고 Claude Code 연동을 지원합니다.



- [lyogavin/airllm](https://github.com/lyogavin/airllm)<br>양자화·증류·프루닝 없이 70B 규모 LLM을 4GB GPU 한 장에서 추론할 수 있게 해주는 라이브러리입니다. 레이어 단위 스트리밍 로딩을 활용해 405B Llama 3.1을 8GB, DeepSeek-V3(671B)를 약 12GB에서 돌리며, sparse MoE 모델은 전문가 하나씩만 올리는 방식으로 Kimi K3(2.8T)를 4GB 미만에서 구동했다고 밝히고 있습니다. macOS도 지원합니다.



- [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)<br>마이크로소프트가 공개한 12주 24강 분량의 AI 입문 커리큘럼입니다. 실습 예제, 퀴즈, 랩을 포함하며 TensorFlow와 PyTorch 같은 실제 도구는 물론 AI 윤리까지 다룹니다. GitHub Action 기반 자동 번역으로 한국어를 포함한 다국어 버전이 항상 최신 상태로 유지되는 점도 장점입니다.



- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)<br>DeepSeek 모델에 최적화된 터미널용 AI 코딩 에이전트입니다. prefix-cache 안정성을 중심으로 설계해 세션을 오래 켜둔 채 작업해도 캐시가 깨지지 않고 비용과 지연이 낮게 유지되는 것이 핵심입니다. npm으로 `reasonix` 패키지를 설치해 쓸 수 있고, ACP 프로토콜과 확장 기능을 지원합니다.



- [usekaneo/kaneo](https://github.com/usekaneo/kaneo)<br>기능 과잉으로 무거워진 기존 프로젝트 관리 도구에 대한 반작용으로 만들어진 오픈소스 프로젝트 관리 툴입니다. 꼭 필요한 기능만 남긴 간결한 인터페이스, 셀프호스팅으로 데이터를 직접 보유하는 구조, 빠른 성능을 강조합니다. MIT 라이선스이며 클라우드 호스팅 버전도 제공합니다.



- [iv-org/invidious](https://github.com/iv-org/invidious)<br>유튜브의 오픈소스 대체 프론트엔드로, 광고와 트래킹이 없고 JavaScript 없이도 동작하는 가벼운 웹 인터페이스를 제공합니다. 다크/라이트 테마, 구독 관리, 세부 설정 등 기본적인 시청 경험을 그대로 지원합니다. AGPLv3 라이선스이며 직접 인스턴스를 띄우거나 공개 인스턴스 목록에서 골라 쓸 수 있습니다.



- [different-ai/openwork](https://github.com/different-ai/openwork)<br>Claude Cowork와 Codex의 오픈소스 대안을 표방하는 macOS/Windows/Linux 데스크톱 앱으로, AI 워크플로를 만들고 공유하는 데 초점을 맞췄습니다. OpenWork MCP 하나만 Codex나 Claude Code, Cursor에 추가하면 동일한 스킬·MCP·연결된 서비스를 여러 도구와 팀원, 여러 머신에서 재사용할 수 있습니다. 조직용 관리 콘솔인 OpenWork Den으로 권한 관리와 스킬 배포까지 다룰 수 있습니다.



- [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge)<br>Uncle Bob(Robert C. Martin)이 만든 tmux 기반 AI 에이전트 오케스트레이션 도구입니다. 에이전트마다 별도 git worktree를 할당하고 tmux 세션과 메시지 패싱으로 서로 충돌 없이 협업하게 만드는 것이 핵심입니다. two-pack(coder+cleaner), four-pack(specifier·coder·refactorer·architect) 등 브랜치별로 TDD와 Gherkin 명세를 강제하는 역할 구성을 골라 쓸 수 있습니다.



- [GitHub Developer: YHH (@esengine)](https://github.com/esengine)



- [GitHub Developer: JUN (@lidge-jun)](https://github.com/lidge-jun)



- [GitHub Developer: Chi Wang (@sonichi)](https://github.com/sonichi)



- [GitHub Developer: Marcus Quinn (@marcusquinn)](https://github.com/marcusquinn)



- [GitHub Developer: Maziyar Panahi (@maziyarpanahi)](https://github.com/maziyarpanahi)



- [GitHub Developer: Marketcalls (@marketcalls)](https://github.com/marketcalls)



- [GitHub Developer: lauren (@poteto)](https://github.com/poteto)



- [GitHub Developer: Will Pfleger (@wpfleger96)](https://github.com/wpfleger96)





## Etc


- [Beta: Gore](https://github.com/x-motemen/gore?ref=console.dev)



- [아직도 1년 전 프롬프트를 그대로 쓰고 있나요?](https://yozm.wishket.com/magazine/detail/3889)



- [넷플릭스 CPTO가 말하는, AI 시대에 채용하고 싶은 사람의 조건](https://yozm.wishket.com/magazine/detail/3888)



- [AI 싫어하는 소비자에게 AI를 써야 한다면 어떻게 할까?](https://yozm.wishket.com/magazine/detail/3886)



- [AI 에이전트와 함께 쓰는 기획/디자인 도구 6가지](https://yozm.wishket.com/magazine/detail/3885)



- [AI 논문 도구를 만들며 마주친 네 번의 갈림길](https://yozm.wishket.com/magazine/detail/3881)



- [개발자의 “할 수 있다”는 말은 어디까지일까요?](https://yozm.wishket.com/magazine/detail/3880)



- [커서 ‘Automations’으로 프로젝트 개선한 후기](https://yozm.wishket.com/magazine/detail/3864)



- ['사스포칼립스' 공포 지나자…SaaS 업계, AI 대응 여부로 희비 엇갈렸다](https://www.aitimes.com/news/articleView.html?idxno=213710)



- [트럼프, 의회의 AI 규제 움직임에 "산업 폐업" 강력 반발…여야 '우회적 방관' 초당적 비판](https://www.aitimes.com/news/articleView.html?idxno=213709)



- [미 FCC “중국산 로봇·인버터 제한, 미국 생산 확대와 안보 위한 조치”](https://www.aitimes.com/news/articleView.html?idxno=213706)



- [[AI 이슈 트렌드] 갤럭시 Z8 흥행 속 차가원 사기·하이닉스 HBF·스페이스X 달 충돌 눈길](https://www.aitimes.com/news/articleView.html?idxno=213708)



- [앤트로픽, 안전 분류기 고도화…'페이블 5' 오탐 답변 거부 85% 줄였다](https://www.aitimes.com/news/articleView.html?idxno=213699)



- [‘클로드’에 백업 맡겼더니 홈 디렉토리 전체 삭제..."미안, 오타였다"](https://www.aitimes.com/news/articleView.html?idxno=213702)



- [AI 회의록 앱의 ‘동의 없는 녹음’ 법정 공방](https://www.itworld.co.kr/article/4206507/ai-%ed%9a%8c%ec%9d%98%eb%a1%9d-%ec%95%b1%ec%9d%98-%eb%8f%99%ec%9d%98-%ec%97%86%eb%8a%94-%eb%85%b9%ec%9d%8c-%eb%b2%95%ec%a0%95-%ea%b3%b5%eb%b0%a9.html)



- [AI에 맡겨도 되는 것과 사람이 직접 해야 하는 것의 차이에 관하여](https://www.itworld.co.kr/article/4205413/ai%ec%97%90-%eb%a7%a1%ea%b2%a8%eb%8f%84-%eb%90%98%eb%8a%94-%ea%b2%83%ea%b3%bc-%ec%82%ac%eb%9e%8c%ec%9d%b4-%ec%a7%81%ec%a0%91-%ed%95%b4%ec%95%bc-%ed%95%98%eb%8a%94-%ea%b2%83%ec%9d%98-%ec%b0%a8%ec%9d%b4.html)



- [AI 에이전트의 IT 업무 자동화, 인간 감독이 결정적 변수](https://www.itworld.co.kr/article/4205385/ai-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8%ec%9d%98-it-%ec%97%85%eb%ac%b4-%ec%9e%90%eb%8f%99%ed%99%94-%ec%9d%b8%ea%b0%84-%ea%b0%90%eb%8f%85%ec%9d%b4-%ea%b2%b0%ec%a0%95%ec%a0%81-%eb%b3%80%ec%88%98.html)



- [스마트 글라스 촬영 논란, 보안 컨퍼런스 입장 금지로 확산](https://www.itworld.co.kr/article/4205359/%ec%8a%a4%eb%a7%88%ed%8a%b8-%ea%b8%80%eb%9d%bc%ec%8a%a4-%ec%b4%ac%ec%98%81-%eb%85%bc%eb%9e%80-%eb%b3%b4%ec%95%88-%ec%bb%a8%ed%8d%bc%eb%9f%b0%ec%8a%a4-%ec%9e%85%ec%9e%a5-%ea%b8%88%ec%a7%80%eb%a1%9c.html)



- [앤트로픽, AI 안전성 평가 중 클로드의 실제 기업 해킹 인정](https://www.itworld.co.kr/article/4204702/%ec%95%a4%ed%8a%b8%eb%a1%9c%ed%94%bd-ai-%ec%95%88%ec%a0%84%ec%84%b1-%ed%8f%89%ea%b0%80-%ec%a4%91-%ed%81%b4%eb%a1%9c%eb%93%9c%ec%9d%98-%ec%8b%a4%ec%a0%9c-%ea%b8%b0%ec%97%85-%ed%95%b4%ed%82%b9.html)



- [AI 데이터센터가 촉발한 메모리 대란, 2027년 이후에도 해소 불투명](https://www.itworld.co.kr/article/4204693/ai-%eb%8d%b0%ec%9d%b4%ed%84%b0%ec%84%bc%ed%84%b0%ea%b0%80-%ec%b4%89%eb%b0%9c%ed%95%9c-%eb%a9%94%eb%aa%a8%eb%a6%ac-%eb%8c%80%eb%9e%80-2027%eb%85%84-%ec%9d%b4%ed%9b%84%ec%97%90%eb%8f%84-%ed%95%b4.html)



- [“제때 살 수 있을까” 올가을 아이폰 18, 품귀 현상 예고](https://www.itworld.co.kr/article/4204226/%ec%a0%9c%eb%95%8c-%ec%82%b4-%ec%88%98-%ec%9e%88%ec%9d%84%ea%b9%8c-%ec%98%ac%ea%b0%80%ec%9d%84-%ec%95%84%ec%9d%b4%ed%8f%b0-18-%ed%92%88%ea%b7%80-%ed%98%84%ec%83%81-%ec%98%88%ea%b3%a0.html)



- [NASA, 48년 된 Voyager 2를 1년 더 가동할 전력 확보](https://news.hada.io/topic?id=32269)



- [Show GN: Toolio - 파일 업로드 없이 도는 무료 웹툴 190개 넘게 만들었습니다.](https://news.hada.io/topic?id=32267)





