---
layout: post
title: "주간 테크/개발 뉴스 #2026 7/19 ~ 7/25"
date: 2026-07-25
categories: [normal]
tags: [weekly, links, dev-news]
---

## 이번 주 pick!

**1. [앤트로픽, '클로드 오퍼스 5' 출시..."페이블 5 성능에 가격은 절반"](https://www.aitimes.com/news/articleView.html?idxno=213161)**

이번 주 가장 큰 파급력을 가진 뉴스는 Opus 5 출시입니다. 최상위 모델의 성능을 유지하면서 가격을 절반으로 낮췄다는 점이 핵심인데, 프론티어 모델 경쟁이 성능 자랑에서 가격 대비 성능 싸움으로 옮겨가고 있음을 보여줍니다. 같은 주에 Claude 5용 컨텍스트 엔지니어링 규칙과 음성 모드 강화 소식이 함께 나왔고, 국내에서는 삼성SDS가 앤트로픽과 엔터프라이즈 파트너십을 체결했습니다. 모델을 실제 서비스에 붙여 쓰는 조직이라면 이번 릴리즈를 계기로 비용 구조를 다시 계산해볼 만합니다.

**2. [한화비전 보안 카메라의 웹 UI 로그인 페이지에 GitHub 관리자 토큰이 포함돼 출하됨](https://news.hada.io/topic?id=31784)**

출하된 펌웨어의 로그인 페이지 안에 GitHub 관리자 토큰이 그대로 박혀 있었습니다. 인증을 통과하기도 전에 누구나 볼 수 있는 정적 리소스에 최고 권한 크리덴셜이 실려 나간 것으로, 유출된 토큰으로 소스 저장소와 이후 펌웨어 배포까지 손댈 수 있었다면 공급망 전체가 열린 상태였다는 뜻입니다. 빌드 파이프라인 어느 단계에서도 시크릿 스캔이 걸러내지 못했다는 점이 더 심각합니다. 남의 일이 아닌 것이, 프론트엔드 번들에 환경변수를 통째로 주입하는 관행은 여전히 흔합니다. 지금 우리 빌드 산출물에 무엇이 섞여 나가고 있는지 확인해볼 이유로 충분합니다.

**3. [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)**

AI 코딩 도구가 리뷰 때마다 저장소를 통째로 다시 읽는 문제를 정면으로 겨냥한 도구입니다. Tree-sitter로 코드 구조 지도를 만들어두고 MCP를 통해 필요한 부분만 넘겨주는 방식으로, 실제 저장소 6곳 벤치마크에서 38배에서 528배까지 토큰을 줄였다고 보고합니다. `pip install` 후 `install` 명령 한 번이면 설치된 AI 코딩 도구들의 MCP 설정을 알아서 잡아줘 도입 비용도 낮습니다. 대형 모노레포에서 컨텍스트와 토큰 비용에 시달리고 있다면 이번 주에 바로 시험해볼 만한 후보입니다.

---

## AI


- [Tool: Neko Master](https://github.com/foru17/neko-master?ref=console.dev)



- [Chrome이 Gemini 팝업용 전역 단축키를 무단 등록](https://news.hada.io/topic?id=31806)



- [Claude Cookbook: 에이전트부터 RAG·멀티모달·운영까지](https://news.hada.io/topic?id=31793)



- [OpenAI의 ‘통제 이탈 해커 에이전트’ 이야기를 회의적으로 봐야 하는 이유](https://news.hada.io/topic?id=31788)



- [Anthropic Opus 5 출시](https://news.hada.io/topic?id=31783)



- [데이터 웨어하우스의 아버지가 말하는 AI 데이터 관리법 5가지](https://yozm.wishket.com/magazine/detail/3862)



- [AI 도구 26개를 직접 만들며 알게 된 자동화 노하우](https://yozm.wishket.com/magazine/detail/3861)



- [클로드 코드로 5일 만에 웹 포털 런칭한 방법](https://yozm.wishket.com/magazine/detail/3857)



- [구글, AI 에이전트 '제미나이 스파크' 확대 출시...월 20달러 프로 요금제도 적용](https://www.aitimes.com/news/articleView.html?idxno=213166)



- [앤트로픽, '클로드 오퍼스 5' 출시..."페이블 5 성능에 가격은 절반"](https://www.aitimes.com/news/articleView.html?idxno=213161)



- [오픈AI, 데스크톱 앱에 'GPT-라이브' 음성 제어 도입](https://www.aitimes.com/news/articleView.html?idxno=213129)



- [앤트로픽, '클로드' 음성 모드 대폭 강화…오퍼스·소네트에도 탑재](https://www.aitimes.com/news/articleView.html?idxno=213130)



- [런웨이, 생성 미디어 '라우터' 출시…비용·속도 고려해 최적 모델 자동 선택](https://www.aitimes.com/news/articleView.html?idxno=213145)



- [깃허브·버셀·파이어스토어, 인디 개발자의 초고속 배포 삼각편대](https://www.itworld.co.kr/article/4200404/%ea%b9%83%ed%97%88%eb%b8%8c%c2%b7%eb%b2%84%ec%85%80%c2%b7%ed%8c%8c%ec%9d%b4%ec%96%b4%ec%8a%a4%ed%86%a0%ec%96%b4-%ec%9d%b8%eb%94%94-%ea%b0%9c%eb%b0%9c%ec%9e%90%ec%9d%98-%ec%b4%88%ea%b3%a0%ec%86%8d.html)



- [AI 모델 선택에 매몰되면 안 되는 이유](https://www.itworld.co.kr/article/4199733/ai-%eb%aa%a8%eb%8d%b8-%ec%84%a0%ed%83%9d%ec%97%90-%eb%a7%a4%eb%aa%b0%eb%90%98%eb%a9%b4-%ec%95%88-%eb%90%98%eb%8a%94-%ec%9d%b4%ec%9c%a0.html)



- [“LLM에 취해 규칙이 무너진 시대” 밖에서는 말 못 할 현대 개발자의 7가지 민낯](https://www.itworld.co.kr/article/4200324/llm%ec%97%90-%ec%b7%a8%ed%95%b4-%ea%b7%9c%ec%b9%99%ec%9d%b4-%eb%ac%b4%eb%84%88%ec%a7%84-%ec%8b%9c%eb%8c%80-%eb%b0%96%ec%97%90%ec%84%9c%eb%8a%94-%eb%a7%90-%eb%aa%bb-%ed%95%a0-%ed%98%84%eb%8c%80.html)



- [지침 완수를 위해 규칙을 스스로 깬 AI…오픈AI 미공개 모델, 샌드박스 해킹으로 자체 규칙 위반](https://www.itworld.co.kr/article/4200314/%ec%a7%80%ec%b9%a8-%ec%99%84%ec%88%98%eb%a5%bc-%ec%9c%84%ed%95%b4-%ea%b7%9c%ec%b9%99%ec%9d%84-%ec%8a%a4%ec%8a%a4%eb%a1%9c-%ea%b9%ac-ai-%ec%98%a4%ed%94%88ai-%eb%af%b8%ea%b3%b5%ea%b0%9c-%eb%aa%a8.html)



- [속도는 앞섰지만 깊이는 멈춘 구글, 제미나이 플래시 3종 출시](https://www.itworld.co.kr/article/4199751/%ec%86%8d%eb%8f%84%eb%8a%94-%ec%95%9e%ec%84%b0%ec%a7%80%eb%a7%8c-%ea%b9%8a%ec%9d%b4%eb%8a%94-%eb%a9%88%ec%b6%98-%ea%b5%ac%ea%b8%80-%ec%a0%9c%eb%af%b8%eb%82%98%ec%9d%b4-%ed%94%8c%eb%9e%98%ec%8b%9c-3.html)



- [“가격에 자신 없으면 기한을 바꾼다”…앤트로픽 페이블 무료 연장의 속내](https://www.itworld.co.kr/article/4199081/%ea%b0%80%ea%b2%a9%ec%97%90-%ec%9e%90%ec%8b%a0-%ec%97%86%ec%9c%bc%eb%a9%b4-%ea%b8%b0%ed%95%9c%ec%9d%84-%eb%b0%94%ea%be%bc%eb%8b%a4%ec%95%a4%ed%8a%b8%eb%a1%9c%ed%94%bd-%ed%8e%98%ec%9d%b4.html)



- [Claude 5 모델을 위한 새로운 컨텍스트 엔지니어링 규칙](https://news.hada.io/topic?id=31782)



- [OpenAI와 Anthropic, 자사 수익을 위협하는 오픈 웨이트 AI에 공동 대응](https://news.hada.io/topic?id=31781)



- [Show GN: ADHDev 1.0 - 로컬 코딩 에이전트를 웹/모바일에서 제어하고 병렬 작업 후 자동 병합하는 도구](https://news.hada.io/topic?id=31773)



- [Codeberg로 이전한 것을 후회하는 이유](https://news.hada.io/topic?id=31772)





## Backend


- [Tool: Databasement](https://david-crty.github.io/databasement?ref=console.dev)



- [databasement - 웹UI 기반 셀프호스팅 DB 백업 관리자](https://news.hada.io/topic?id=31799)



- [FLUX 3 x mimic: 로봇을 위한 차세대 비디오-액션 모델](https://news.hada.io/topic?id=31789)



- [“어떻게 만들고 어떻게 관리할 것인가” 데이터 제품 개발의 성패를 가르는 5가지 핵심 질문](https://www.itworld.co.kr/article/4199156/%ec%96%b4%eb%96%bb%ea%b2%8c-%eb%a7%8c%eb%93%a4%ea%b3%a0-%ec%96%b4%eb%96%bb%ea%b2%8c-%ea%b4%80%eb%a6%ac%ed%95%a0-%ea%b2%83%ec%9d%b8%ea%b0%80-%eb%8d%b0%ec%9d%b4%ed%84%b0-%ec%a0%9c%ed%92%88-%ea%b0%9c.html)



- [AI 시대 SaaS 생존…소프트웨어는 기능을 팔고 플랫폼은 책임을 판다](https://www.itworld.co.kr/article/4199703/ai-%ec%8b%9c%eb%8c%80-saas-%ec%83%9d%ec%a1%b4-%ec%86%8c%ed%94%84%ed%8a%b8%ec%9b%a8%ec%96%b4%eb%8a%94-%ea%b8%b0%eb%8a%a5%ec%9d%84-%ed%8c%94%ea%b3%a0-%ed%94%8c%eb%9e%ab%ed%8f%bc%ec%9d%80-%ec%b1%85.html)





## Infra/Cloud


- [“규칙은 지켰지만 경계는 넘었다” AI 코딩 에이전트의 샌드박스 취약점 보고](https://www.itworld.co.kr/article/4199698/%ea%b7%9c%ec%b9%99%ec%9d%80-%ec%a7%80%ec%bc%b0%ec%a7%80%eb%a7%8c-%ea%b2%bd%ea%b3%84%eb%8a%94-%eb%84%98%ec%97%88%eb%8b%a4-ai-%ec%bd%94%eb%94%a9-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8%ec%9d%98.html)





## Tools


- [Beta: termcn](https://www.termcn.dev?ref=console.dev)



- [Show GN: 에이전트의 토큰낭비를 잡는 CLI를 만들었습니다! (공개 트레이스 6,780개)](https://news.hada.io/topic?id=31802)



- [인도 정부, GitHub에 Bluetooth 채팅 앱 Bitchat 삭제 명령](https://news.hada.io/topic?id=31800)



- [FLUX 3 모델 공개](https://news.hada.io/topic?id=31791)



- [한화비전 보안 카메라의 웹 UI 로그인 페이지에 GitHub 관리자 토큰이 포함돼 출하됨](https://news.hada.io/topic?id=31784)



- [스팀 머신 리뷰 : 귀엽지만 아쉬운 161만원짜리 미니 PC](https://www.itworld.co.kr/article/4199108/%ec%8a%a4%ed%8c%80-%eb%a8%b8%ec%8b%a0-%eb%a6%ac%eb%b7%b0-%ea%b7%80%ec%97%bd%ec%a7%80%eb%a7%8c-%ec%95%84%ec%89%ac%ec%9a%b4-161%eb%a7%8c%ec%9b%90%ec%a7%9c%eb%a6%ac-%eb%af%b8%eb%8b%88-pc.html)





## GitHub Trending


- [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)<br>"Agent = LLM + 컨텍스트 + 도구"라는 공식을 축으로 AI 에이전트의 원리부터 프로덕션 엔지니어링까지 10개 장으로 다룬 책의 오픈소스 저장소입니다. 본문·도표는 물론 92개의 실습 프로젝트(70여 개는 단독 실행 가능)를 모두 공개했고, PDF/EPUB 다운로드와 웹 열람을 지원합니다. 중국어 원문 외에 영어·일본어·러시아어 등 7개 언어 번역본이 제공됩니다.



- [koala73/worldmonitor](https://github.com/koala73/worldmonitor)<br>전 세계 뉴스·지정학 이슈·인프라 상태를 한 화면에서 실시간으로 추적하는 상황 인식 대시보드입니다. AI 기반 뉴스 집계를 중심으로 tech·finance·commodity·energy 등 주제별 변형 사이트를 함께 운영하며, TypeScript로 작성되어 AGPL v3로 공개돼 있습니다. 웹 앱뿐 아니라 npm CLI, Python SDK, MCP 서버 형태로도 제공돼 다른 도구에 붙여 쓸 수 있습니다.



- [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)<br>AI 코딩 도구가 리뷰 때마다 코드베이스를 통째로 다시 읽으며 토큰을 낭비하는 문제를 겨냥한 로컬 우선 코드 인텔리전스 그래프입니다. Tree-sitter로 코드의 구조 지도를 만들어 증분 추적하고, MCP를 통해 AI 어시스턴트에 필요한 부분만 정확히 전달합니다. 실제 저장소 6곳 벤치마크에서 38배~528배 토큰 절감을 보고했고, `pip install` 후 `install` 명령 하나로 지원 도구들의 MCP 설정을 자동 구성합니다.



- [1jehuang/jcode](https://github.com/1jehuang/jcode)<br>멀티 세션 워크플로우와 성능에 초점을 맞춘 차세대 코딩 에이전트 하네스입니다. RAM 사용량과 부팅 속도를 극단적으로 최적화해, 로컬 임베딩을 끄면 27.8MB로 동작하며 Codex CLI·OpenCode 등 경쟁 도구 대비 수 배 적은 메모리를 쓴다고 밝히고 있습니다. macOS·Linux·Windows를 모두 지원하고 설치 스크립트 한 줄로 시작할 수 있습니다.



- [agegr/pi-web](https://github.com/agegr/pi-web)<br>pi 코딩 에이전트를 브라우저에서 다룰 수 있게 해주는 로컬 웹 UI입니다. 로컬 세션 파일을 읽어 이전 대화를 프로젝트별로 탐색하고, 특정 메시지 지점에서 이어가거나 세션을 분기할 수 있으며, Git worktree 전환도 사이드바에서 처리합니다. 컨텍스트 사용량·비용·압축 상태를 상단에서 확인할 수 있고 모델·API 키·스킬 설정도 웹에서 관리합니다.



- [earendil-works/pi](https://github.com/earendil-works/pi)<br>스스로를 확장할 수 있는 코딩 에이전트를 포함한 Pi 에이전트 하네스의 본체 저장소입니다. OpenAI·Anthropic·Google 등을 하나로 묶은 통합 LLM API(`pi-ai`), 툴 호출과 상태 관리를 담당하는 에이전트 런타임(`pi-agent-core`), 대화형 CLI, 차등 렌더링 TUI 라이브러리를 패키지로 나눠 제공합니다. 자체 권한 시스템이 없어 강한 격리가 필요하면 마이크로 VM이나 Docker로 감싸는 세 가지 패턴을 안내합니다.



- [ruvnet/RuView](https://github.com/ruvnet/RuView)<br>평범한 WiFi 신호를 공간 감지 시스템으로 바꿔주는 프로젝트입니다. 저가 ESP32 센서로 Channel State Information(CSI)을 수집해 사람의 존재, 호흡·심박 같은 생체 신호, 움직임을 카메라나 웨어러블 없이 벽 너머로도 감지합니다. Home Assistant, Apple Home, Google Home, Alexa와 MQTT·Matter로 연동되며 수면 감지·낙상 위험·재실 여부 등 10가지 의미론적 상태를 엔티티로 노출합니다.



- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)<br>선형대수부터 자율 에이전트 군집까지 20단계 503개 레슨, 약 320시간 분량으로 구성된 무료 AI 엔지니어링 커리큘럼입니다. 모든 알고리즘을 수식부터 직접 구현하게 해 역전파·토크나이저·어텐션·에이전트 루프를 손으로 만든 뒤에야 PyTorch를 꺼내는 방식이 특징입니다. Python·TypeScript·Rust·Julia 네 언어를 다루고, 레슨마다 프롬프트·스킬·에이전트·MCP 서버 같은 재사용 가능한 산출물이 남습니다.



- [GitHub Developer: Owain Lewis (@owainlewis)](https://github.com/owainlewis)



- [GitHub Developer: Elie Habib (@koala73)](https://github.com/koala73)



- [GitHub Developer: なるみ (@narumiruna)](https://github.com/narumiruna)



- [GitHub Developer: AstroHan (@Astro-Han)](https://github.com/Astro-Han)



- [GitHub Developer: David Zhang (@Git-on-my-level)](https://github.com/Git-on-my-level)



- [GitHub Developer: Owen Schwartz (@oschwartz10612)](https://github.com/oschwartz10612)



- [GitHub Developer: Jeremy Huang (@1jehuang)](https://github.com/1jehuang)



- [GitHub Developer: Assaf Elovic (@assafelovic)](https://github.com/assafelovic)



- [GitHub Developer: Dream Hunter (@dreamhunter2333)](https://github.com/dreamhunter2333)





## Etc


- [Beta: topcoat](https://github.com/tokio-rs/topcoat?ref=console.dev)



- [클로드 코드, 42주 동안 사용한 팀의 워크플로우는 어떨까?](https://yozm.wishket.com/magazine/detail/3863)



- [AI가 다 만드는데, 왜 자꾸 기획을 말할까?](https://yozm.wishket.com/magazine/detail/3858)



- [검색은 변해도 '결정의 순간'은 인간의 영역이다](https://yozm.wishket.com/magazine/detail/3856)



- [AI 시대 프로덕트팀 재설계법(feat. 보리스 체르니)](https://yozm.wishket.com/magazine/detail/3855)



- [AI로 작성하셨나요? 'Im-not-ai'로 AI 티 지우기](https://yozm.wishket.com/magazine/detail/3854)



- ["국산 칩 안 쓰면 반역자"…중국, AI 기업들에 '강력 경고'](https://www.aitimes.com/news/articleView.html?idxno=213176)



- [젠슨 황, 한국 정부·기업과 회동…”25년 협력, AI 혁신으로 확장”](https://www.aitimes.com/news/articleView.html?idxno=213174)



- [삼성SDS, 앤트로픽과 파트너십 체결..."국내 엔터프라이즈 시장 공략"](https://www.aitimes.com/news/articleView.html?idxno=213172)



- [‘샌프란시스코 AI 서밋’서 한국-빅테크 협약 6건 체결…”반도체부터 AX까지 협력”](https://www.aitimes.com/news/articleView.html?idxno=213173)



- [[AI 이슈 트렌드] 쿠팡 화재·삼전닉스 레버리지 논란...BTS 월드컵·영화 '호프'도 눈길](https://www.aitimes.com/news/articleView.html?idxno=213170)



- [Show GN: 캐치마인드 좋아하세요?](https://news.hada.io/topic?id=31803)




- [Substack의 AI 투명성 도구를 둘러싼 작가들의 반응](https://news.hada.io/topic?id=31797)



- [AI 투자 실패로 Oracle, 직원 2만 1,000명 해고](https://news.hada.io/topic?id=31796)





