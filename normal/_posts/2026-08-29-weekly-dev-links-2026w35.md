---
layout: post
title: "주간 테크/개발 뉴스 #2026 8/23 ~ 8/29"
date: 2026-08-29
categories: [normal]
tags: [weekly, links, dev-news]
---



## 이번 주 pick!

**1. [Model Hardware Standard - AI가 로봇과 실험 장비를 함께 다루게 하는 공통 표준](https://news.hada.io/topic?id=32982)**

Anthropic과 HHMI Janelia가 AI 에이전트와 실험실 장비를 잇는 공통 명세 MHS의 연구 프리뷰를 열었습니다.
장비마다 제각각인 인터페이스를 read/write 수준의 기본 명령으로 통일해, 현미경·로봇 팔·액체 처리기를 붙일 때마다 맞춤 통합 코드를 쓰던 부담을 없애는 것이 핵심입니다.
초기 사례에서 실험 자동화 구축 기간이 수주에서 8시간으로 줄었고, QuEra에서는 AI가 만든 레이저 복구 코드가 700회 중 695회 성공했습니다.
MCP가 소프트웨어 도구 연결의 공통 규격이 됐듯, 이번엔 물리 장비 쪽에서 같은 시도가 시작된 셈이라 눈여겨볼 만합니다.

**2. [tt-a1i/archify](https://github.com/tt-a1i/archify)**

Claude Code, Cursor, Codex CLI 같은 코딩 에이전트가 만든 typed JSON IR을 결정론적으로 컴파일해 인터랙티브 아키텍처 다이어그램으로 뽑아주는 Node.js 도구입니다.
대화 중에 바로 코드베이스 구조를 그려볼 수 있고, PR 전에 아키텍처 변경을 Before/Delta/After로 비교하는 기능이 특히 실무에 바로 쓸 만합니다.
노드 검색과 업스트림·다운스트림 추적을 실제 토폴로지 기반으로 제공하며, 결과물은 의존성 없는 단일 HTML로 나와 공유도 간단합니다.

**3. [Anthropic 팀이 요즘 많이 쓰는 Claude Code 스킬 - eli5](https://x.com/trq212/status/2090884854590382515)**

Claude Code 팀의 Thariq Shihipar가 공개한 뒤 8월 내내 화제가 된 스킬입니다.
/eli5 뒤에 주제를 적으면 "이 주제를 전혀 모르는 사람에게, 큰 그림과 적은 텍스트의 HTML 아티팩트로 설명하라"는 지시가 붙어, 모듈 동작 방식이나 아키텍처 선택 이유, 장애 원인 같은 걸 도식 중심으로 풀어줍니다.
SKILL.md 전체가 321바이트뿐이라는 점이 인상적인데, 새 능력을 더하는 게 아니라 이미 있는 능력의 출력 형태만 바꾸는 스킬의 좋은 예시입니다.
claude plugin marketplace add anthropics/claude-plugins-community 후 claude plugin install eli5@claude-community 로 바로 설치해볼 수 있습니다.

---

## AI


- [Beta: Apache Maka](https://github.com/apache/maka?ref=console.dev)



- [SpaceX의 Cursor 인수 이후 OpenAI가 내린 결정](https://news.hada.io/topic?id=33003)



- [Yap - LLM이 코드에 남기는 ‘주석 슬롭’](https://news.hada.io/topic?id=32999)



- [미 법원, 국방부의 Anthropic 블랙리스트 지정은 불법이라고 판결](https://news.hada.io/topic?id=32987)






- [Hugging Face 침해 사고와 OpenAI의 대응 계획](https://news.hada.io/topic?id=32984)



- [Model Hardware Standard - AI가 로봇과 실험 장비를 함께 다루게 하는 공통 표준](https://news.hada.io/topic?id=32982)



- [OpenAI Python SDK, HTTPX에서 Pydantic의 HTTPX2로 전환](https://news.hada.io/topic?id=32981)



- [블랙박스 LLM의 크기를 재는 법](https://news.hada.io/topic?id=32977)



- [로컬 LLM으로 민감정보를 걸러봤습니다](https://yozm.wishket.com/magazine/detail/3918)



- [회고 잘하고 싶어서 만든 인터랙티브 회고 도구](https://yozm.wishket.com/magazine/detail/3917)



- [GEO 분석 툴을 만들다: E-E-A-T 분석하는 법](https://yozm.wishket.com/magazine/detail/3910)



- [구글, '제미나이 라이브'에 에이전트 탑재…음성으로 일정·이메일 제어](https://www.aitimes.com/news/articleView.html?idxno=214599)



- [구글, '제미나이 3.8 플래시' 내부 테스트 포착...'월간 출시' 속도전](https://www.aitimes.com/news/articleView.html?idxno=214546)



- ["일회성 대화도 저장 가능"...오픈AI, 챗GPT 임시 채팅 기능 강화](https://www.aitimes.com/news/articleView.html?idxno=214569)



- [구글, ‘제미나이 옴니 1.1 플래시’ 공개…영상 생성·편집 제어 기능 대폭 강화](https://www.aitimes.com/news/articleView.html?idxno=214576)



- [챗GPT 필수 설정 5가지…보안·개인정보·개성까지 한 번에 정비한다면](https://www.itworld.co.kr/article/4214563/%ec%b1%97gpt-%ed%95%84%ec%88%98-%ec%84%a4%ec%a0%95-5%ea%b0%80%ec%a7%80-%eb%b3%b4%ec%95%88%c2%b7%ea%b0%9c%ec%9d%b8%ec%a0%95%eb%b3%b4%c2%b7%ea%b0%9c%ec%84%b1%ea%b9%8c%ec%a7%80-%ed%95%9c-%eb%b2%88.html)



- [“왜 파일럿에서 멈추는가” 에이전틱 AI 배포를 결정하는 3가지 인프라 조건](https://www.itworld.co.kr/article/4214550/%ec%99%9c-%ed%8c%8c%ec%9d%bc%eb%9f%bf%ec%97%90%ec%84%9c-%eb%a9%88%ec%b6%94%eb%8a%94%ea%b0%80-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8b%b1-ai-%eb%b0%b0%ed%8f%ac%eb%a5%bc-%ea%b2%b0%ec%a0%95%ed%95%98.html)



- [슬랙, 개발자·비기술 직원 함께 쓰는 AI 코딩 채널 ‘슬랙 코드’ 출시](https://www.itworld.co.kr/article/4214539/%ec%8a%ac%eb%9e%99-%ea%b0%9c%eb%b0%9c%ec%9e%90%c2%b7%eb%b9%84%ea%b8%b0%ec%88%a0-%ec%a7%81%ec%9b%90-%ed%95%a8%ea%bb%98-%ec%93%b0%eb%8a%94-ai-%ec%bd%94%eb%94%a9-%ec%b1%84%eb%84%90-%ec%8a%ac%eb%9e%99.html)



- [AI는 들였는데, 보안은 준비됐나…도입 속도 빠를수록 보안 공백 커진다](https://www.itworld.co.kr/article/4214531/ai%eb%8a%94-%eb%93%a4%ec%98%80%eb%8a%94%eb%8d%b0-%eb%b3%b4%ec%95%88%ec%9d%80-%ec%a4%80%eb%b9%84%eb%90%90%eb%82%98-%eb%8f%84%ec%9e%85-%ec%86%8d%eb%8f%84-%eb%b9%a0%eb%a5%bc%ec%88%98%eb%a1%9d.html)



- [AI 지출 폭증 시대가 요구하는 것 ‘검증된 귀속 데이터’](https://www.itworld.co.kr/article/4213924/ai-%ec%a7%80%ec%b6%9c-%ed%8f%ad%ec%a6%9d-%ec%8b%9c%eb%8c%80%ea%b0%80-%ec%9a%94%ea%b5%ac%ed%95%98%eb%8a%94-%ea%b2%83-%ea%b2%80%ec%a6%9d%eb%90%9c-%ea%b7%80%ec%86%8d-%eb%8d%b0%ec%9d%b4%ed%84%b0.html)



- [AI가 설명할수록 인간 판단력 저하…LLM 추천 근거의 역설](https://www.itworld.co.kr/article/4212648/ai%ea%b0%80-%ec%84%a4%eb%aa%85%ed%95%a0%ec%88%98%eb%a1%9d-%ec%9d%b8%ea%b0%84-%ed%8c%90%eb%8b%a8%eb%a0%a5-%ec%a0%80%ed%95%98llm-%ec%b6%94%ec%b2%9c-%ea%b7%bc%ea%b1%b0%ec%9d%98-%ec%97%ad.html)



- [오퍼스 모델 언어 혼선, 토큰 비용 2배·개발 속도 저하로 이어져](https://www.itworld.co.kr/article/4212644/%ec%98%a4%ed%8d%bc%ec%8a%a4-%eb%aa%a8%eb%8d%b8-%ec%96%b8%ec%96%b4-%ed%98%bc%ec%84%a0-%ed%86%a0%ed%81%b0-%eb%b9%84%ec%9a%a9-2%eb%b0%b0%c2%b7%ea%b0%9c%eb%b0%9c-%ec%86%8d%eb%8f%84-%ec%a0%80%ed%95%98.html)



- [백만 마리의 카카포](https://news.hada.io/topic?id=32975)





## Backend


- [Tool: PicoMQ](https://picomq.com/?ref=console.dev)



- [Tool: MicroLighter](https://davatron5000.github.io/microlighter?ref=console.dev)



- [Beta: SelfDB](https://github.com/fzakaria/selfdb?ref=console.dev)



- [Beta: OpenViking](https://openviking.ai?ref=console.dev)



- [지금 당장 서비스에 쓸만한 API ② 사주·영화·게임·여행·검색 트렌드 편](https://yozm.wishket.com/magazine/detail/3920)



- [지금 당장 서비스에 쓸만한 API ① 지도·교통·날씨·주식·부동산 편](https://yozm.wishket.com/magazine/detail/3916)



- [오픈AI, 프롬프트 보유 없이 AI 오용 패턴 탐지하는 ‘프라이빗 세이프티 프로세싱’ 공개](https://www.itworld.co.kr/article/4213336/%ec%98%a4%ed%94%88ai-%ed%94%84%eb%a1%ac%ed%94%84%ed%8a%b8-%eb%b3%b4%ec%9c%a0-%ec%97%86%ec%9d%b4-ai-%ec%98%a4%ec%9a%a9-%ed%8c%a8%ed%84%b4-%ed%83%90%ec%a7%80%ed%95%98%eb%8a%94-%ed%94%84%eb%9d%bc.html)





## Infra/Cloud


- [vphone-cli - 애플 실리콘 Mac에서 iOS를 가상 iPhone으로 부팅하는 CLI](https://news.hada.io/topic?id=33007)



- [EasyEffects를 모든 Linux 배포판에 포함해 노트북 스피커 음질을 개선해야 함](https://news.hada.io/topic?id=32998)





## Tools


- [Anthropic 팀이 요즘 많이 쓰는 Claude Code 스킬 - eli5](https://x.com/trq212/status/2090884854590382515)


- [Beta: Huzzah](https://www.danielvaughn.dev/posts/huzzah?ref=console.dev)



- [Beta: Hunk](https://www.hunk.dev?ref=console.dev)





## GitHub Trending


- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)<br>GPT-Image2 프롬프트를 500개 이상의 리버스 엔지니어링 케이스와 20개 이상의 산업용 템플릿으로 정리한 "Prompt as Code" 프로젝트로, 산문형 프롬프트를 subject·lighting·material·layout 등으로 분해한 구조화된 스키마로 압축해 재사용성과 자동화 친화성을 높인 것이 특징입니다. UI, 인포그래픽, 포스터 등 카테고리별 케이스 갤러리와 웹사이트, Agent Skill을 함께 제공해 에이전트·스크립트 워크플로우에서 바로 활용할 수 있습니다. 배치 생성이나 프로덕션 파이프라인에 필요한 재현성과 제어 가능성을 확보했다는 점에서 단순 프롬프트 모음집과 차별화되어 주목받고 있습니다.



- [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community)<br>Claude Cowork 및 Claude Code용 커뮤니티 플러그인 마켓플레이스로, `.claude-plugin/marketplace.json`을 통해 설치 가능한 플러그인 목록을 제공하는 읽기 전용(read-only) 미러 저장소이다. 모든 플러그인은 claude.ai 제출 페이지를 통해 등록되고 자동 보안 스캔을 통과한 뒤 Anthropic 내부 검토 파이프라인의 승인을 거쳐 매일 밤 동기화되므로, 직접적인 PR 기여 없이도 검증된 플러그인만 유통되는 구조가 특징이다. Claude Code에서는 `claude plugin marketplace add`와 `claude plugin install` 명령으로 손쉽게...



- [tt-a1i/archify](https://github.com/tt-a1i/archify)<br>archify는 Cursor·Claude Code·Codex CLI·OpenCode 같은 에이전트가 생성한 typed JSON IR을 Archify가 결정론적으로 컴파일해, 코드베이스나 시스템 설명을 대화 안에서 바로 인터랙티브한 아키텍처 다이어그램(HTML/SVG)으로 만들어주는 Node.js 도구입니다. 다섯 가지 다이어그램 유형과 다크/라이트 테마, PR 전 아키텍처 변경사항을 Before/Delta/After로 비교하는 기능, 노드 검색·업스트림/다운스트림 추적·가이드 스토리 재생 등 실제 토폴로지에 근거한 인터랙션을 제공합니다. 결과물은 PNG·SVG·WebM·공유 카드까지 포함한 자체 완결형 단일 HTML...



- [omacom/omarchy](https://github.com/omacom/omarchy)<br>옴아키(Omarchy)는 DHH가 만든 미니멀하고 세련된 디자인의 Linux 배포판으로, Hyprland 기반 타일링 워크플로우와 통일된 테마·단축키·클립보드 관리 등 고도로 큐레이션된 개발자 경험을 제공합니다. Neovim, 터미널, AI 도구, 셸 유틸리티 등 개발에 최적화된 애플리케이션 구성과 상세한 매뉴얼(manual/ 디렉토리)을 기본 제공하는 것이 특징입니다. 단순 배포판을 넘어 macOS/Windows 사용자의 전환을 돕는 opinionated 설정과 문서화 수준 덕분에 개발자 커뮤니티에서 주목받고 있습니다.



- [apache/maka](https://github.com/apache/maka)<br>Apache Maka는 Apache Software Foundation에서 인큐베이팅 중인 로컬 우선(local-first) Agent 워크스페이스로, 프로젝트를 분석하고 sandbox 경계 안에서 도구를 실행하며 모델 메시지와 tool call을 복구 가능한 실행 기록으로 남기는 것이 특징입니다. Desktop(Electron+React), TUI/CLI, Eval 세 가지 진입점이 모두 하나의 Runtime Host를 공유해 세션, 설정, 실행 기록이 사용자 로컬 머신에 유지되며, 사용자가 원하는 모델(클라우드 API, 로컬 모델 등)을 자유롭게 연결할 수 있습니다. 아직 정식 Apache 릴리스는 없고 현재...



- [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)<br>FreeLLMAPI는 Google, Groq, Cerebras, Mistral, OpenRouter 등 34개 무료 LLM 제공업체(474개 모델군, 635개 엔드포인트)의 무료 티어를 합산해 월 74억 토큰 규모의 추론 자원을 단일 OpenAI 호환 `/v1` API로 통합 제공합니다. 요청마다 최적 모델을 선택하는 라우터가 특정 제공업체가 레이트리밋에 걸리면 자동으로 다음 제공업체로 폴백하고, 키별 사용량을 추적해 무료 한도를 넘지 않도록 관리하며, API 키는 암호화 저장됩니다.



- [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)<br>AI Job Search는 Claude Code 기반의 AI 구직 지원 프레임워크로, `/scrape`, `/apply`, `/interview` 같은 명령어를 통해 채용 공고 검색부터 적합도 평가, CV·커버레터 작성(LaTeX 기반), 면접 준비까지 전 과정을 자동화합니다. 개발자 본인이 실직 후 이 워크플로우로 69건의 맞춤 지원과 20건의 1차 면접을 거쳐 실제 취업에 성공한 사례로 주목받고 있으며, 핵심 워크플로우는 언어·국가에 구애받지 않도록 설계되어 있어(포털 검색 스킬만 덴마크 시장에 특화) 다른 지역으로도 확장 가능합니다. 드래프터-리뷰어 에이전트 파이프라인으로 지원서를 생성·검토·수정하는 구조가...



- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)<br>Claude Code Plugins Directory는 Anthropic이 공식 운영하는 Claude Code용 플러그인 큐레이션 저장소로, `/plugins`(Anthropic 자체 개발)와 `external_plugins`(파트너·커뮤니티 제출) 두 영역으로 구성되어 있으며 `/plugin install` 명령이나 `/plugin > Discover`를 통해 손쉽게 설치할 수 있습니다. MCP 서버, commands, agents, skills 등을 표준화된 디렉터리 구조로 담을 수 있고, plugin.json 없이 `SKILL.md`만 있는 저장소도 `strict: false` 설정으로 등록 가능해...






- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)<br>이 프로젝트는 AI 엔지니어링을 처음부터 실습으로 배울 수 있도록 구성된 무료 오픈소스(MIT) 커리큘럼으로, Python·TypeScript·Rust·Julia를 활용해 20개 phase, 523개 레슨, 약 342시간 분량의 학습 콘텐츠를 제공합니다. 단순 이론 설명이 아니라 각 레슨마다 prompt, skill, agent, MCP 서버 같은 실제 재사용 가능한 산출물을 직접 만들어보는 방식이 특징입니다. GitHub과 자체 웹사이트에서 동일한 커리큘럼을 제공하며 코딩 에이전트(tutor)와의 연동, 다국어 번역, Claude 인증 준비 과정까지 지원해 실무형 AI 엔지니어 양성을 목표로 주목받고 있습니다.



































## Etc


- [만들기도 전에 이게 돈이 될까부터 생각한 적 있다면](https://yozm.wishket.com/magazine/detail/3919)



- [[요즘IT x 노션] ‘로컬앱 자랑대회’ 출전작 모집!](https://yozm.wishket.com/magazine/detail/3915)



- [리더는 "AI 왜 안 쓰냐" VS 실무자는 "사고 나면요?"](https://yozm.wishket.com/magazine/detail/3914)



- [현장이 만든 AI를 GS는 어떻게 상용 제품으로 키웠나](https://yozm.wishket.com/magazine/detail/3913)



- [충원이 거절되자 "이거 한번 해보자"로 시작한 자동화](https://yozm.wishket.com/magazine/detail/3912)



- [[AI 이슈트렌드] 엔비디아 호재 안 통한 삼전·하이닉스…박위 사고·제주 실종 파장](https://www.aitimes.com/news/articleView.html?idxno=214606)



- [앤트로픽 "AI가 인간 대신 정렬 작업 수행…안전성 크게 높였다"](https://www.aitimes.com/news/articleView.html?idxno=214608)



- [허깅페이스, 55만원짜리 오픈소스 로봇 '마이크로덕' 공개](https://www.aitimes.com/news/articleView.html?idxno=214607)



- [실리콘밸리 매료시킨 ‘인스팅트’ 3.5조 가치 인정..."진짜 AI 비서"](https://www.aitimes.com/news/articleView.html?idxno=214605)



- [앤트로픽, 엔스케일 계약 이어 칩 스타트업 협상…컴퓨팅 용량 확보 '총력전'](https://www.aitimes.com/news/articleView.html?idxno=214604)



- [셀렉트스타 "AI 안전성, 빅테크도 못 다루는 로컬 리스크 해결이 핵심"](https://www.aitimes.com/news/articleView.html?idxno=214585)



- [학습 데이터 삭제해도 이미지는 그대로, MIT가 밝힌 확산 모델의 맹점](https://www.itworld.co.kr/article/4212715/%ed%95%99%ec%8a%b5-%eb%8d%b0%ec%9d%b4%ed%84%b0-%ec%82%ad%ec%a0%9c%ed%95%b4%eb%8f%84-%ec%9d%b4%eb%af%b8%ec%a7%80%eb%8a%94-%ea%b7%b8%eb%8c%80%eb%a1%9c-mit%ea%b0%80-%eb%b0%9d%ed%9e%8c-%ed%99%95%ec%82%b0.html)



- [경보 과부하 시대, AI로 기업 보안을 강화하는 7가지 방법](https://www.itworld.co.kr/article/4214504/%ea%b2%bd%eb%b3%b4-%ea%b3%bc%eb%b6%80%ed%95%98-%ec%8b%9c%eb%8c%80-ai%eb%a1%9c-%ea%b8%b0%ec%97%85-%eb%b3%b4%ec%95%88%ec%9d%84-%ea%b0%95%ed%99%94%ed%95%98%eb%8a%94-7%ea%b0%80%ec%a7%80-%eb%b0%a9.html)



- [버그 소문만으로 익스플로잇이 만들어지는 시대](https://news.hada.io/topic?id=33005)



- [Show GN: RIR LAB - Codex로 구현해본 22개의 미니 아이디어](https://news.hada.io/topic?id=33004)





