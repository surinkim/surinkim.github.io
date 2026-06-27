---
layout: post
title: "주간 테크/개발 뉴스 #2026 6/21 ~ 6/27"
date: 2026-06-27
categories: [normal]
tags: [weekly, links, dev-news]
---



## 이번 주 pick!

**1. [오픈AI, 최고 성능 'GPT-5.6' 3종 공개..."정부 요청으로 제한적 출시"](https://www.aitimes.com/news/articleView.html?idxno=212175)**

OpenAI가 GPT-5.6 시리즈 3종을 공개했지만, 트럼프 행정부의 안보 우려에 따라 일반 사용자가 아닌 미국 정부가 배포 대상을 결정하는 이례적인 출시 방식을 취했다. 민간 AI 기업의 최신 모델이 국가 통제 채널을 통해 단계적으로 공개된다는 것은 AI 거버넌스의 새로운 전례로, 업계 전반의 규제 지형에 영향을 줄 수 있다. "안보가 아닌 복종 요구"라는 앤트로픽의 반발과 함께 AI 주도권을 둘러싼 기업-정부 갈등이 본격화되고 있다.

**2. [새로운 HTTP QUERY 메소드](https://news.hada.io/topic?id=30846)**

GET 요청에 body를 실을 수 없고 POST는 캐시가 안 된다는 REST의 고질적 딜레마를 해결하기 위해 IETF에서 QUERY 메소드를 표준화하고 있다. 복잡한 검색·필터 조건을 URL 파라미터에 우겨넣지 않고 구조화된 body로 전달하면서도 GET처럼 안전하고 멱등한 요청이 가능해진다. 이미 수많은 GraphQL API와 Elasticsearch가 임시방편으로 GET+body나 POST를 혼용해왔는데, 이 관행이 표준으로 정착될 경우 API 설계의 오랜 논쟁이 정리된다.

**3. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)**

텍스트 프롬프트만으로 리서치·스크립팅·에셋 생성·편집·렌더링까지 전 과정을 자동화하는 오픈소스 agentic 영상 제작 시스템이다. Claude Code, Cursor 같은 AI 코딩 어시스턴트를 내부 오케스트레이터로 활용하며, Veo·Kling 등 AI 영상 생성 모델, TTS 내레이션, 스톡 영상 검색까지 통합한다. 60초 애니메이션 단편을 $1.33에 제작한 사례처럼 영상 제작 비용 구조를 완전히 바꿀 가능성이 있고, 참고 영상 URL을 넣으면 스타일을 분석해 기획안과 비용 견적까지 제시해준다.

---

## AI


- [Tool: Go Micro](https://go-micro.dev/?ref=console.dev)



- [Tool: Hasp](https://gethasp.com/?ref=console.dev)



- [Beta: Flue](https://flueframework.com?ref=console.dev)



- [미국, Anthropic의 Mythos AI를 ‘신뢰된’ 미국 조직에 공개 허용](https://news.hada.io/topic?id=30878)



- [미국 정부가 GPT-5.6 사용자를 결정할 예정](https://news.hada.io/topic?id=30867)



- [GPT‑5.6 Sol 프리뷰: 차세대 모델](https://news.hada.io/topic?id=30866)



- [Show HN: OpenKnowledge – Obsidian/Notion의 오픈소스 AI 우선 대안](https://news.hada.io/topic?id=30860)



- [Vibecoding 공개로 Emacs 패치가 거절됨](https://news.hada.io/topic?id=30856)



- [AI에게 주도권을 빼앗기지 마세요 — 두 번의 자동화 실패에서 배운 것](https://news.hada.io/topic?id=30855)



- [Show GN: SongRyeon Core - LLM이 쓴 말과 코드가 검증한 정보를 분리하는 로컬 에이전트 런타임 실험](https://news.hada.io/topic?id=30854)



- [Claude Tag, 앤트로픽이 공개한 슬랙에 상주하는 AI 팀원](https://yozm.wishket.com/magazine/detail/3821)



- [K8s 운영을 AI 에이전트에 맡길 수 있을까?](https://yozm.wishket.com/magazine/detail/3817)



- [바이두, '언리미티드 OCR' 공개… "메모리 한계 깨고 수십페이지 문서 한 번에"](https://www.aitimes.com/news/articleView.html?idxno=212177)



- [엔비디아, 'GLM-5.2' 4비트 양자화 모델 공개...“정확도 유지하며 용량 70% 절감”](https://www.aitimes.com/news/articleView.html?idxno=212178)



- [중국, 휴머노이드 로봇 이어 AI 에이전트에도 '디지털 신분증' 도입](https://www.aitimes.com/news/articleView.html?idxno=212180)



- [오픈AI, 최고 성능 ‘GPT-5.6’ 3종 공개..."정부 요청으로 제한적 출시"](https://www.aitimes.com/news/articleView.html?idxno=212175)



- [구글, '제미나이 3.5 플래시'에 컴퓨터 유즈 탑재...기업용 에이전트 시장 조준](https://www.aitimes.com/news/articleView.html?idxno=212160)



- [업무용 챗봇 시대 끝나…오픈AI "사내 업무 99% 코덱스가 처리"](https://www.aitimes.com/news/articleView.html?idxno=212125)



- [LGU+, 휴대폰결제 AI 구독료 최대 45% 할인 프로모션 진행](https://www.aitimes.com/news/articleView.html?idxno=212170)



- [오픈AI, 'GPT-5.5 인스턴트' 업데이트… "컨텍스트 추적 능력 강화로 대화 원활"](https://www.aitimes.com/news/articleView.html?idxno=212129)



- [트럼프 행정부, 안보 우려로 "GPT-5.6 순차적 출시" 압박](https://www.aitimes.com/news/articleView.html?idxno=212122)



- [[6월25일] "모델이 하네스를 먹어 치울 것"...구글이 본 AI 경쟁의 다음 단계](https://www.aitimes.com/news/articleView.html?idxno=212092)



- [잘 만든 AI 에이전트도 실패하는 이유…답은 ‘실행 거버넌스’](https://www.itworld.co.kr/article/4189709/%ec%9e%98-%eb%a7%8c%eb%93%a0-ai-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8%eb%8f%84-%ec%8b%a4%ed%8c%a8%ed%95%98%eb%8a%94-%ec%9d%b4%ec%9c%a0%eb%8b%b5%ec%9d%80-%ec%8b%a4%ed%96%89-%ea%b1%b0.html)



- [API를 바꾸는 AI와 ‘의도 이해’ 기반 웹 아키텍처 시대](https://www.itworld.co.kr/article/4189147/api%eb%a5%bc-%eb%b0%94%ea%be%b8%eb%8a%94-ai%ec%99%80-%ec%9d%98%eb%8f%84-%ec%9d%b4%ed%95%b4-%ea%b8%b0%eb%b0%98-%ec%9b%b9-%ec%95%84%ed%82%a4%ed%85%8d%ec%b2%98-%ec%8b%9c%eb%8c%80.html)



- [“안보가 아닌 복종 요구”…트럼프 vs. 앤트로픽의 AI 주도권 전쟁](https://www.itworld.co.kr/article/4188660/%ec%95%88%eb%b3%b4%ea%b0%80-%ec%95%84%eb%8b%8c-%eb%b3%b5%ec%a2%85-%ec%9a%94%ea%b5%ac%ed%8a%b8%eb%9f%bc%ed%94%84-vs-%ec%95%a4%ed%8a%b8%eb%a1%9c%ed%94%bd-ai-%ec%a3%bc%eb%8f%84%ea%b6%8c.html)



- [‘지식 붕괴’가 온다, AI 남용이 부르는 기업 역량 위기](https://www.itworld.co.kr/article/4188622/%ec%a7%80%ec%8b%9d-%eb%b6%95%ea%b4%b4%ea%b0%80-%ec%98%a8%eb%8b%a4-ai-%eb%82%a8%ec%9a%a9%ec%9d%b4-%eb%b6%80%eb%a5%b4%eb%8a%94-%ea%b8%b0%ec%97%85-%ec%97%ad%eb%9f%89-%ec%9c%84%ea%b8%b0.html)



- [API 키 하나가 무너뜨리는 중소기업 AI 보안 지키기](https://www.itworld.co.kr/article/4187538/api-%ed%82%a4-%ed%95%98%eb%82%98%ea%b0%80-%eb%ac%b4%eb%84%88%eb%9c%a8%eb%a6%ac%eb%8a%94-%ec%a4%91%ec%86%8c%ea%b8%b0%ec%97%85-ai-%eb%b3%b4%ec%95%88-%ec%a7%80%ed%82%a4%ea%b8%b0.html)



- [도구와 대화하는 것의 피로감](https://news.hada.io/topic?id=30841)





## Backend


- [Beta: Hotswap](https://hotswap.arcjet.com?ref=console.dev)



- [Beta: Nub](https://nubjs.com/?ref=console.dev)



- [새로운 HTTP QUERY 메소드](https://news.hada.io/topic?id=30846)



- [모든 고객을 위한 Cloudflare OAuth](https://news.hada.io/topic?id=30845)




- [데이터센터의 탐욕, AI 인플레이션 시대 청구서로 돌아온다](https://www.itworld.co.kr/article/4188205/%eb%8d%b0%ec%9d%b4%ed%84%b0%ec%84%bc%ed%84%b0%ec%9d%98-%ed%83%90%ec%9a%95-ai-%ec%9d%b8%ed%94%8c%eb%a0%88%ec%9d%b4%ec%85%98-%ec%8b%9c%eb%8c%80-%ec%b2%ad%ea%b5%ac%ec%84%9c%eb%a1%9c-%eb%8f%8c%ec%95%84.html)



- [AI가 쌓는 ‘보이지 않는 빚’ 인지적 부채의 위기](https://www.itworld.co.kr/article/4187513/ai%ea%b0%80-%ec%8c%93%eb%8a%94-%eb%b3%b4%ec%9d%b4%ec%a7%80-%ec%95%8a%eb%8a%94-%eb%b9%9a-%ec%9d%b8%ec%a7%80%ec%a0%81-%eb%b6%80%ec%b1%84%ec%9d%98-%ec%9c%84%ea%b8%b0.html)



- [Nub - Node.js용 Bun 유사 올인원 툴킷](https://news.hada.io/topic?id=30832)







## Tools


- [“윈도우 팬도 설득했다” 크롬북을 선택하게 만든 3가지 반전](https://www.itworld.co.kr/article/4189163/%ec%9c%88%eb%8f%84%ec%9a%b0-%ed%8c%ac%eb%8f%84-%ec%84%a4%eb%93%9d%ed%96%88%eb%8b%a4-%ed%81%ac%eb%a1%ac%eb%b6%81%ec%9d%84-%ec%84%a0%ed%83%9d%ed%95%98%ea%b2%8c-%eb%a7%8c%eb%93%a0-3%ea%b0%80%ec%a7%80.html)





## GitHub Trending


- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)<br>OpenMontage는 AI 코딩 어시스턴트(Claude Code, Cursor 등)를 활용해 텍스트 프롬프트만으로 리서치, 스크립팅, 에셋 생성, 편집, 렌더링까지 전 과정을 자동화하는 최초의 오픈소스 agentic 영상 제작 시스템입니다. 단순히 이미지를 이어 붙이는 수준이 아니라, 실제 스톡 영상 검색·AI 영상 생성(Veo, Kling 등)·TTS 내레이션·자막·음악 소싱·Remotion 기반 컴포지션까지 처리하며, 참고 영상(YouTube, TikTok 등)을 붙여넣으면 스타일을 분석해 새로운 기획안과 비용 견적까지 제시해 줍니다. 60초 애니메이션 단편을 $1.33, 제품 광고를 $0.69에 제작한 사례처럼...






- [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native)<br>Agent-Native는 AI 에이전트가 챗봇처럼 앱 옆에 붙는 것이 아니라, 앱 내부에서 직접 동작하도록 설계된 오픈소스 프레임워크로, 하나의 Action 정의만으로 UI·에이전트·API·MCP·CLI 등 모든 인터페이스에서 동일하게 사용할 수 있는 것이 핵심이다. SQL 기반 상태 관리, 실시간 멀티플레이어 편집, 에이전트 간 통신(A2A), observability 등 프로덕션급 기능을 기본 제공하며, DB·호스팅·모델을 자유롭게 선택할 수 있다. Slides, Analytics, Design 등 완성된 SaaS 수준의 템플릿을 fork하여 바로 시작할 수 있고, 에이전트가 스스로 UI를 개선하고 버그를 수정하는...



- [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes)<br>`no-mistakes`는 `git push` 앞에 AI 기반 검증 파이프라인을 두어, 코드 리뷰·테스트·린트 등 모든 체크를 통과한 경우에만 실제 remote에 push하고 깔끔한 PR을 자동으로 생성해주는 로컬 git 프록시입니다. 일회용 worktree에서 파이프라인이 돌아가므로 작업 흐름을 방해하지 않으며, 안전한 수정은 자동 적용하고 의도가 개입되는 부분만 사용자에게 판단을 맡기는 구조입니다. Claude Code, Codex, Copilot 등 다양한 코딩 에이전트와 연동되고, `/no-mistakes` 스킬을 통해 에이전트가 직접 게이트를 구동할 수 있어 AI 코딩 워크플로우의 품질 관문 역할을 합니다.



- [penpot/penpot](https://github.com/penpot/penpot)<br>Penpot은 SVG, CSS, HTML 등 웹 표준 기반으로 동작하는 오픈소스 디자인 플랫폼으로, 셀프 호스팅을 지원해 디자인 인프라의 완전한 소유권과 벤더 락인 없는 운영이 가능합니다. 디자인을 코드로 표현하는 접근 방식과 네이티브 Design Tokens, MCP server, 플러그인 시스템을 통해 디자이너와 개발자 간 협업을 극대화하고 AI 워크플로우까지 연결합니다. Figma 등 상용 도구의 대안으로서 실시간 협업, CSS Grid/Flex Layout, 강력한 API를 갖춘 풀스택 디자인 플랫폼이라는 점에서 주목할 만합니다.



- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)<br>AI 대형 모델(Gemini, OpenAI, Claude, DeepSeek 등)을 활용해 A주·홍콩·미국·일본·한국 주식을 매일 자동 분석하고, 매수/매도/관망 판단이 담긴 '결정 대시보드'를 WeChat·Telegram·Discord·Slack·이메일 등으로 푸시해주는 시스템이다. GitHub Actions로 5분 만에 무료 배포가 가능하고, Web 워크스페이스·Agent 전략 질의·백테스트·포지션 관리까지 갖춘 올인원 구조가 특징이다. AkShare·YFinance·Tushare 등 다양한 데이터 소스와 SerpAPI·Tavily 등 뉴스 검색을 결합해 기술 지표·자금 흐름·뉴스 심리까지 종합 분석한다는 점에서...



- [jamiepine/voicebox](https://github.com/jamiepine/voicebox)<br>Voicebox는 ElevenLabs와 WisprFlow를 대체하는 오픈소스 로컬 AI 음성 스튜디오로, 몇 초의 오디오 샘플만으로 음성을 복제하고 7개 TTS 엔진(Qwen3-TTS, Kokoro, Chatterbox 등)을 통해 23개 언어로 음성을 생성하며, 글로벌 단축키 기반 음성 받아쓰기(dictation)까지 하나의 앱에서 제공한다. 모든 모델과 데이터가 로컬에서 실행되어 프라이버시를 보장하고, REST API 및 MCP 서버를 내장해 Claude Code나 Cursor 같은 AI 에이전트에 음성 I/O를 바로 연결할 수 있다는 점이 핵심 차별점이다. Tauri(Rust) 기반 네이티브 앱으로 macOS...






- [koala73/worldmonitor](https://github.com/koala73/worldmonitor)<br>WorldMonitor는 500개 이상의 뉴스 피드를 AI로 요약하고, 3D 지구본(globe.gl)과 WebGL 맵(deck.gl) 위에 지정학·금융·재난·군사 신호를 실시간으로 시각화하는 글로벌 상황 인식 대시보드입니다. Ollama를 통한 로컬 AI 실행을 지원해 외부 API 키 없이도 동작하며, 하나의 코드베이스에서 6개 사이트 변형(world, tech, finance, commodity, happy, energy)과 Tauri 2 기반 데스크톱 앱까지 빌드할 수 있는 점이 특징적입니다. 31개국 불안정성 지수(CII) 산출, 29개 증권거래소 모니터링, 24개 언어 지원 등 개인 프로젝트치고는 이례적으로...



- [stablyai/orca](https://github.com/stablyai/orca)<br>Orca는 Codex, Claude Code, OpenCode 등 여러 AI 코딩 에이전트를 하나의 데스크톱 앱에서 병렬로 실행·관리할 수 있는 오케스트레이터로, 각 에이전트가 독립된 git worktree에서 작업하므로 결과를 비교한 뒤 최적안만 머지할 수 있습니다. 내장 터미널(WebGL 렌더링), Design Mode(Chromium UI 요소를 에이전트 프롬프트로 전달), GitHub/Linear 네이티브 통합, SSH 원격 worktree, diff 어노테이션 등 에이전트 기반 개발에 필요한 워크플로를 올인원으로 제공합니다. 모바일 컴패니언 앱(iOS/Android)으로 외부에서도 에이전트 상태를 모니터링하고...



- [GitHub Developer: Cole Murray (@ColeMurray)](https://github.com/ColeMurray)



- [GitHub Developer: zhulinsen (@ZhuLinsen)](https://github.com/ZhuLinsen)



- [GitHub Developer: Huang Xin (@chrox)](https://github.com/chrox)



- [GitHub Developer: Duy /zuey/ (@mrgoonie)](https://github.com/mrgoonie)



- [GitHub Developer: Elie Habib (@koala73)](https://github.com/koala73)



- [GitHub Developer: Fayner Brack (@FagnerMartinsBrack)](https://github.com/FagnerMartinsBrack)



- [GitHub Developer: rUv (@ruvnet)](https://github.com/ruvnet)



- [GitHub Developer: Otto Sulin (@ottosulin)](https://github.com/ottosulin)





## Etc


- [Beta: TypeScript 7 RC](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc?ref=console.dev)



- [Beta: Lore](https://lore.org?ref=console.dev)



- ["AI 도입하고 싶다" 한마디가 8억 견적서 되는 이유](https://yozm.wishket.com/magazine/detail/3823)



- [시장에서 이기는 AI 프로덕트를 위한 지표와 운영법](https://yozm.wishket.com/magazine/detail/3820)



- [손 코딩은 죽었는가?](https://yozm.wishket.com/magazine/detail/3819)



- [AX에 꼭 필요한 '온톨로지', 회의록으로 시작하는 법 (feat. 티로)](https://yozm.wishket.com/magazine/detail/3818)



- [SaaS의 종말? AI 시대에 적합한 소프트웨어는 무엇일까](https://yozm.wishket.com/magazine/detail/3815)



- [런던에서 만난 AI 시대 디자이너의 5가지 생존 전략](https://yozm.wishket.com/magazine/detail/3814)



- [개발자는 여전히 수학을 잘해야 할까요?](https://yozm.wishket.com/magazine/detail/3813)



- [“M6 프로는 건너뛸까” 애플, AI 대응 위해 M7 조기 투입 전망](https://www.itworld.co.kr/article/4189725/m6-%ed%94%84%eb%a1%9c%eb%8a%94-%ea%b1%b4%eb%84%88%eb%9b%b8%ea%b9%8c-%ec%95%a0%ed%94%8c-ai-%eb%8c%80%ec%9d%91-%ec%9c%84%ed%95%b4-m7-%ec%a1%b0%ea%b8%b0-%ed%88%ac%ec%9e%85-%ec%a0%84.html)







