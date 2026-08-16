---
layout: post
title: "주간 테크/개발 뉴스 #2026 8/9 ~ 8/15"
date: 2026-08-15
categories: [normal]
tags: [weekly, links, dev-news]
---

## 이번 주 pick!

**1. [앤트로픽 '워터마크' 도입에 사용자 반발…'클로드' 구독 취소 확산](https://www.aitimes.com/news/articleView.html?idxno=213998)**

이번 주 국내외 매체가 한목소리로 다룬 사건입니다. 앤트로픽이 클로드 출력물에 눈에 보이지 않는 워터마크를 심기 시작하자 구독 취소 움직임이 번졌습니다.
AI 생성물 표기는 규제 대응 측면에서 불가피한 흐름이지만, 사용자 입장에서는 "내가 쓴 글에 제조사 식별자가 따라붙는다"는 문제로 읽힙니다.
[작동 원리](https://news.hada.io/topic?id=32518)를 보면 토큰 선택 확률에 통계적 편향을 주는 방식이라 텍스트를 조금 고쳐도 남습니다. 앞으로 다른 모델 벤더들이 어떤 선택을 하는지가 관전 포인트입니다.

**2. [장애 대응의 숨겨진 비용과 옵저버빌리티가 답하지 못하는 질문](https://www.itworld.co.kr/article/4208429/%ec%9e%a5%ec%95%a0-%eb%8c%80%ec%9d%91%ec%9d%98-%ec%88%a8%ea%b2%a8%ec%a7%84-%eb%b9%84%ec%9a%a9%ea%b3%bc-%ec%98%b5%ec%a0%80%eb%b2%84%eb%b9%8c%eb%a6%ac%ed%8b%b0%ea%b0%80-%eb%8b%b5%ed%95%98%ec%a7%80.html)**

"모든 것이 보이는데 설명할 수는 없다." 대시보드와 알림을 아무리 정교하게 만들어도 원인 파악에 두세 시간이 걸리는 이유를 짚은 글입니다.
옵저버빌리티는 '지금 무슨 일이 벌어지는가'에는 답하지만 '왜 벌어졌는가'는 이틀 전 배포, 지원 대기열, 스프린트 변경 이력처럼 텔레메트리 밖에 흩어져 있다는 지적이 핵심입니다.
게다가 이 수작업 상관관계 분석은 늘 가장 맥락을 많이 아는 시니어에게 돌아가는데, 평균 복구 시간(MTTR, Mean Time to Resolution)은 조사가 끝난 시점부터 재기 때문에 그 비용이 지표에 잡히지 않습니다. 장애 회고를 준비 중이라면 읽어볼 만합니다.

**3. [지금 전 세계에서 가장 인기 있는 에이전트 스킬 Top5는 뭘까?](https://yozm.wishket.com/magazine/detail/3895)**

스킬을 서너 개 만들어 보면 "내가 제대로 만들고 있는 게 맞나" 싶어지는데, 그때 가장 빠른 답은 잘 만든 남의 것을 열어보는 것이라는 문제의식에서 출발한 글입니다.
GitHub 스타 기준으로 상위 5개 레포를 어디에 쓰는지, 내부에서 무슨 일이 벌어지는지, 나머지와 뭐가 다른지 세 축으로 정리했습니다.
1위 `obra/superpowers`는 세션마다 부트스트랩 스킬을 주입해 설계 문답부터 병합 정리까지 7단계를 강제하는데, 시작하자마자 22,000토큰을 먹는다는 트레이드오프까지 같이 짚어줍니다.

---

## AI


- [Tool: Amp](https://ampcode.com/?ref=console.dev)



- [실전 루프 엔지니어링](https://news.hada.io/topic?id=32519)



- [AI 텍스트 워터마킹의 작동 원리](https://news.hada.io/topic?id=32518)



- [AI 모델 고르기: 같은 프롬프트, 11개 모델, 매우 다른 결과](https://news.hada.io/topic?id=32505)



- [X, For You 알고리듬 공개 범위 확대 - 랭킹 가중치와 노출 제한 시스템까지](https://news.hada.io/topic?id=32491)



- [23년 된 동네슈퍼를 데이터로 분석하기: 무엇이 팔렸나?](https://yozm.wishket.com/magazine/detail/3900)



- [이제 클로드가 만든 글엔 눈에 안 보이는 워터마크가 붙습니다](https://yozm.wishket.com/magazine/detail/3899)



- [지금 전 세계에서 가장 인기 있는 에이전트 스킬 Top5는 뭘까?](https://yozm.wishket.com/magazine/detail/3895)



- [[티켓 증정 이벤트] 개발자·PM도 알아야 할 검색의 미래, 구글에게 직접 듣는다](https://yozm.wishket.com/magazine/detail/3892)



- [오픈AI, 맥용 챗GPT '컴퓨터 히스토리' 출시...앱·웹 활동 기억한다](https://www.aitimes.com/news/articleView.html?idxno=213986)



- [오픈AI 기업용 매출, '챗GPT' 넘어섰다…“강력한 매출로 악재 돌파”](https://www.aitimes.com/news/articleView.html?idxno=213994)



- [MS, 개인·기업용 코파일럿 통합…‘슈퍼 앱’으로 재탄생](https://www.aitimes.com/news/articleView.html?idxno=213970)



- [애플, 중국 시장 겨냥한 자체 모델 개발...알리바바와 협력](https://www.aitimes.com/news/articleView.html?idxno=213966)



- [오픈AI, 14배 빠른 '울트라패스트' 모드 공개..."지능과 속도 다 잡았다"](https://www.aitimes.com/news/articleView.html?idxno=213946)



- [AI 토큰을 많이 소비할수록 우수한 개발자인가](https://www.itworld.co.kr/article/4209009/ai-%ed%86%a0%ed%81%b0%ec%9d%84-%eb%a7%8e%ec%9d%b4-%ec%86%8c%eb%b9%84%ed%95%a0%ec%88%98%eb%a1%9d-%ec%9a%b0%ec%88%98%ed%95%9c-%ea%b0%9c%eb%b0%9c%ec%9e%90%ec%9d%b8%ea%b0%80.html)



- [“에이전트 배포보다 어려운 건 통제” AI 오케스트레이션 플랫폼 선택 전략 5가지](https://www.itworld.co.kr/article/4209005/%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8-%eb%b0%b0%ed%8f%ac%eb%b3%b4%eb%8b%a4-%ec%96%b4%eb%a0%a4%ec%9a%b4-%ea%b1%b4-%ed%86%b5%ec%a0%9c-ai-%ec%98%a4%ec%bc%80%ec%8a%a4%ed%8a%b8%eb%a0%88%ec%9d%b4.html)



- [“AI 글래스·딥페이크 대응 시급” 마에스트로 포렌식, 차세대 포렌식 솔루션 선보여](https://www.itworld.co.kr/article/4208932/ai-%ea%b8%80%eb%9e%98%ec%8a%a4%c2%b7%eb%94%a5%ed%8e%98%ec%9d%b4%ed%81%ac-%eb%8c%80%ec%9d%91-%ec%8b%9c%ea%b8%89-%eb%a7%88%ec%97%90%ec%8a%a4%ed%8a%b8%eb%a1%9c-%ed%8f%ac%eb%a0%8c%ec%8b%9d-%ec%b0%a8.html)



- [보이지 않지만 지워지지 않는 워터마크, 클로드가 심는다](https://www.itworld.co.kr/article/4208389/%eb%b3%b4%ec%9d%b4%ec%a7%80-%ec%95%8a%ec%a7%80%eb%a7%8c-%ec%a7%80%ec%9b%8c%ec%a7%80%ec%a7%80-%ec%95%8a%eb%8a%94-%ec%9b%8c%ed%84%b0%eb%a7%88%ed%81%ac-%ed%81%b4%eb%a1%9c%eb%93%9c%ea%b0%80-%ec%8b%ac.html)



- [AI로 무장한 사이버 범죄, 가드레일 우회부터 공급망 침투까지](https://www.itworld.co.kr/article/4207554/ai%eb%a1%9c-%eb%ac%b4%ec%9e%a5%ed%95%9c-%ec%82%ac%ec%9d%b4%eb%b2%84-%eb%b2%94%ec%a3%84-%ea%b0%80%eb%93%9c%eb%a0%88%ec%9d%bc-%ec%9a%b0%ed%9a%8c%eb%b6%80%ed%84%b0-%ea%b3%b5%ea%b8%89%eb%a7%9d-%ec%b9%a8.html)





## Backend


- [Tool: SolidStart 2](https://docs.solidjs.com/solid-start/v2/getting-started?ref=console.dev)



- [지루한 기술을 선택하라 (2015)](https://news.hada.io/topic?id=32496)



- [모델 임차인에서 모델 소유자로, 오픈 웨이트의 부상](https://www.itworld.co.kr/article/4208402/%eb%aa%a8%eb%8d%b8-%ec%9e%84%ec%b0%a8%ec%9d%b8%ec%97%90%ec%84%9c-%eb%aa%a8%eb%8d%b8-%ec%86%8c%ec%9c%a0%ec%9e%90%eb%a1%9c-%ec%98%a4%ed%94%88-%ec%9b%a8%ec%9d%b4%ed%8a%b8%ec%9d%98-%eb%b6%80%ec%83%81.html)



- [클라우드플레어, AI 퍼스트 기업 겨냥한 운영체제 출시](https://www.itworld.co.kr/article/4207020/%ed%81%b4%eb%9d%bc%ec%9a%b0%eb%93%9c%ed%94%8c%eb%a0%88%ec%96%b4-ai-%ed%8d%bc%ec%8a%a4%ed%8a%b8-%ea%b8%b0%ec%97%85-%ea%b2%a8%eb%83%a5%ed%95%9c-%ec%9a%b4%ec%98%81%ec%b2%b4%ec%a0%9c-%ec%b6%9c%ec%8b%9c.html)



- [AI 에이전트 킬 스위치, 선택 아닌 필수](https://www.itworld.co.kr/article/4207005/ai-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8-%ed%82%ac-%ec%8a%a4%ec%9c%84%ec%b9%98-%ec%84%a0%ed%83%9d-%ec%95%84%eb%8b%8c-%ed%95%84%ec%88%98.html)





## Infra/Cloud


- [장애 대응의 숨겨진 비용과 옵저버빌리티가 답하지 못하는 질문](https://www.itworld.co.kr/article/4208429/%ec%9e%a5%ec%95%a0-%eb%8c%80%ec%9d%91%ec%9d%98-%ec%88%a8%ea%b2%a8%ec%a7%84-%eb%b9%84%ec%9a%a9%ea%b3%bc-%ec%98%b5%ec%a0%80%eb%b2%84%eb%b9%8c%eb%a6%ac%ed%8b%b0%ea%b0%80-%eb%8b%b5%ed%95%98%ec%a7%80.html)





## Tools


- [Show GN: PasteClip - 무료 오픈소스 macOS 클립보드 매니저 (Paste 대체제)](https://news.hada.io/topic?id=32526)



- [GLM-5.3: 포스트 트레이닝 확장으로 프런티어급 코딩·사이버 역량 달성](https://news.hada.io/topic?id=32493)





## GitHub Trending


- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)<br>Claude Code, Codex, Pi에서 쓸 수 있는 다이어그램 생성 에이전트 스킬로, 아키텍처·플로우차트·시퀀스 등 27종의 시각화 타입을 제공한다. 빌드 과정이나 JavaScript 없이 브라우저에서 바로 열리는 정적 HTML + SVG로 출력되며, 라이트/다크/풀 에디토리얼 3가지 변형을 지원한다. draw.io나 Mermaid 소스를 원하는 포맷과 밀도로 다시 그려주는 기능도 있다.



- [semantica-agi/semantica](https://github.com/semantica-agi/semantica)<br>기업 데이터를 수집해 Context Graph와 지식 그래프(KG)로 만들고, 그 위에서 그래프 분석과 인과 추론을 수행하는 오픈소스 인프라다. 모든 판단에 결정 근거(provenance)가 기록되어 설명 가능하고 추적 가능한 AI 시스템을 목표로 하며, RDF와 LPG를 모두 지원하는 폴리글랏 그래프 저장소를 갖췄다. 규제가 엄격한 고위험 도메인을 겨냥한 셀프 호스팅형 "오픈소스 Palantir"를 표방한다.



- [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)<br>장시간 자율 실행을 목표로 한 오픈소스 코딩·리서치 에이전트로, 컨텍스트를 변수처럼 다루는 RLM(Recursive Language Model)과 세션을 넘어 유지되는 Continual Harness를 핵심 추상화로 삼는다. 파일 조작·셸·서브에이전트 호출이 모두 영속 IPython 환경에서 코드로 이뤄지며, `rlm(...)` 호출로 자식 에이전트를 병렬 실행할 수 있다. `/refine` 명령으로 에이전트가 자신의 보조 프롬프트와 스킬을 근거 기반으로 점진 개선하는 자기 개선 루프를 지원한다.



- [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard)<br>NVIDIA가 공개한 Rust 기반 LLM 트래픽 프록시로, OpenAI Chat·Anthropic Messages·OpenAI Responses 포맷 간 프로토콜 변환을 지원한다. Claude Code나 Codex 같은 코딩 에이전트가 네이티브 API를 그대로 쓰면서 vLLM, NVIDIA NIM, Ollama 등 오픈 모델로 요청을 넘길 수 있고, 여러 모델에 트래픽을 분산해 A/B 벤치마킹도 가능하다. Prometheus 메트릭을 제공하지만 아직 pre-alpha 단계로 프로덕션 사용은 권장되지 않는다.



- [megadose/holehe](https://github.com/megadose/holehe)<br>이메일 주소 하나로 twitter, instagram, imgur 등 120개 이상의 사이트에 계정이 등록돼 있는지 확인하는 Python 기반 OSINT 도구다. 각 서비스의 비밀번호 찾기 기능을 이용해 부분 마스킹된 복구 이메일이나 전화번호까지 수집하며, 대상 이메일에는 알림이 가지 않는다. CLI로 바로 쓰거나 async 모듈 형태로 기존 Python 애플리케이션에 임베드할 수 있다.



- [cactus-compute/needle](https://github.com/cactus-compute/needle)<br>툴 호출과 구조화된 추출에 특화된 45M 파라미터 오픈 모델로, 전체가 14MB 단일 바이너리이며 약 28MB RAM에서 세션 하나를 돌린다. 스키마에서 컴파일한 바이트 단위 문법으로 모든 토큰을 제약해 항상 유효한 JSON을 내놓고, 학습된 헤드가 응답마다 신뢰도 점수를 붙여 임계값 이하는 상위 모델로 에스컬레이션할 수 있다. 256토큰 슬라이딩 윈도우로 대화가 길어져도 메모리가 고정되어 폰·웨어러블·로봇 같은 초소형 디바이스를 노린다.



- [macro-inc/macro](https://github.com/macro-inc/macro)<br>이메일·메시지·문서·태스크·에이전트·CRM을 하나의 인터페이스로 통합한 팀 워크스페이스로, Slack·Linear·Notion·HubSpot을 각각 쓰던 흐름을 단일 시스템으로 대체하는 것을 목표로 한다. 모든 항목이 @링크로 연결되고 문서-태스크, 채널 메시지-이메일 간 상호 참조가 양방향 그래프로 저장되어 팀과 에이전트가 같은 메모리를 공유한다. SolidJS와 Rust로 만들어졌고 자체 팀이 2년간 도그푸딩한 뒤 오픈소스로 공개했다.



- [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag)<br>모노레포를 대상으로 한 RAG 도구로, 여러 언어가 섞인 코드베이스를 지식 그래프로 인덱싱해 질의·이해·편집을 돕는다. 단순 벡터 검색이 아니라 코드 구조를 그래프로 표현해 함수·모듈 간 관계를 따라가며 답을 찾는 것이 특징이다. PyPI로 설치할 수 있고 엔터프라이즈 지원 옵션도 제공한다.



- [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet)<br>사내 도구·대시보드·워크플로우·AI 에이전트를 만드는 오픈소스 로우코드 플랫폼으로, 60개 이상의 반응형 컴포넌트와 드래그앤드롭 빌더를 제공한다. 80종 이상의 데이터 소스(DB, API, 클라우드 스토리지, SaaS)에 연결되고 내장 노코드 DB, 멀티플레이어 편집, 앱 내 JavaScript·Python 실행을 지원한다. Docker·Kubernetes·AWS·GCP 등으로 셀프 호스팅할 수 있으며, 자연어 앱 생성 같은 AI 기능은 유료 엔터프라이즈 버전에 포함된다.



- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)<br>Addy Osmani가 시니어 엔지니어의 개발 워크플로우와 품질 게이트를 AI 코딩 에이전트용 스킬로 패키징한 모음이다. `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship` 등 8개 슬래시 커맨드가 개발 라이프사이클에 매핑되며, API 설계나 프런트엔드 작업처럼 상황에 따라 관련 스킬이 자동 활성화된다. `/build auto`를 쓰면 계획을 한 번 승인한 뒤 각 태스크를 테스트 주도로 구현·커밋하며 자율 실행하고, Claude Code·Cursor·Codex 등 70여 개 에이전트에 설치할 수 있다.



- [GitHub Developer: Soju06 (@Soju06)](https://github.com/Soju06)



- [GitHub Developer: callumalpass (@callumalpass)](https://github.com/callumalpass)



- [GitHub Developer: TisonK (@TheCodingDad-TisonK)](https://github.com/TheCodingDad-TisonK)



- [GitHub Developer: Sirui Lu (@LionSR)](https://github.com/LionSR)



- [GitHub Developer: Kane Wang (@kane50613)](https://github.com/kane50613)



- [GitHub Developer: Michael Ramos (@backnotprop)](https://github.com/backnotprop)



- [GitHub Developer: Nico Burns (@nicoburns)](https://github.com/nicoburns)



- [GitHub Developer: Arthur R Longbottom (@artokun)](https://github.com/artokun)





## Etc


- [Beta: Wails](https://v3.wails.io/blog/wails-v3-beta?ref=console.dev)



- [AI by Hand — 손으로 익히는 AI 수학·알고리듬·아키텍처](https://news.hada.io/topic?id=32530)



- [ActivityPub은 지루했기에 승리했다](https://news.hada.io/topic?id=32527)



- [Going Dark와 법 집행기관 해킹의 시대](https://news.hada.io/topic?id=32524)



- [클로드 코드 길들이기: 6인의 실제 사례집 출시](https://yozm.wishket.com/magazine/detail/3901)



- [10년 전 자격증 교재가 AI 테스트를 살렸다](https://yozm.wishket.com/magazine/detail/3897)



- [AI 챗봇이 있어도 왜 콜센터 전화는 줄지 않을까?](https://yozm.wishket.com/magazine/detail/3896)



- [B2B AI SaaS가 성공하려면 뭐가 중요할까?](https://yozm.wishket.com/magazine/detail/3894)



- [MCP 새로운 스펙 총정리: 무엇을 결정하고 바꿔야 할까?](https://yozm.wishket.com/magazine/detail/3893)



- [테스트 코드 없이 웹을 검수하는 Manta AI, 믿을만할까?](https://yozm.wishket.com/magazine/detail/3891)



- [앤트로픽 '워터마크' 도입에 사용자 반발…'클로드' 구독 취소 확산](https://www.aitimes.com/news/articleView.html?idxno=213998)



- [알리바바, '큐원3.8-맥스' 가중치 공개…상업적 이용엔 라이선스 필요](https://www.aitimes.com/news/articleView.html?idxno=213997)



- [알리바바, ‘큐원3.8-27B’ 가중치 공개...오퍼스 4.6급 성능 도전](https://www.aitimes.com/news/articleView.html?idxno=213987)



- [미스트랄 AI, 문서 레이아웃 보존 능력 높인 'OCR 4.1' 공개](https://www.aitimes.com/news/articleView.html?idxno=213991)



- [슬랙·메일·녹음까지 싹쓸이...AI 데이터 고갈에 '사내 기록' 몸값 폭등](https://www.aitimes.com/news/articleView.html?idxno=213993)



- [존 터너스 체제 첫 이벤트, 애플이 9월에 공개할 제품은?](https://www.itworld.co.kr/article/4209501/%ec%a1%b4-%ed%84%b0%eb%84%88%ec%8a%a4-%ec%b2%b4%ec%a0%9c-%ec%b2%ab-%ec%9d%b4%eb%b2%a4%ed%8a%b8-%ec%95%a0%ed%94%8c%ec%9d%b4-9%ec%9b%94%ec%97%90-%ea%b3%b5%ea%b0%9c%ed%95%a0-%ec%a0%9c%ed%92%88%ec%9d%80.html)



- [Google, 동형 암호화로 프라이빗 AI를 실용화](https://news.hada.io/topic?id=32522)



- [Suno Studio 2.0 - MIDI와 AI Chat을 결합한 본격적인 음악 제작 도구](https://news.hada.io/topic?id=32520)



- [아직 이해하지 못한 것에 대해 블로그를 써라](https://news.hada.io/topic?id=32517)



- [hubble.md - 사람과 에이전트를 위한 노트패드](https://news.hada.io/topic?id=32516)



- [Qwen3.8-27B, 17~19GB 메모리에서 4-bit 로컬 실행 가능](https://news.hada.io/topic?id=32514)





