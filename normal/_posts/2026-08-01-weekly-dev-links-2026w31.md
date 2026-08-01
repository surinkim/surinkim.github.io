---
layout: post
title: "주간 테크/개발 뉴스 #2026 7/26 ~ 8/1"
date: 2026-08-01
categories: [normal]
tags: [weekly, links, dev-news]
---

## 이번 주 pick!

**1. [오픈AI, GPT-5.6 라인업 가격 최대 80% 인하…효율성 경쟁 가속](https://www.aitimes.com/news/articleView.html?idxno=213381)**

모델 성능 경쟁이 가격 경쟁으로 넘어가는 변곡점입니다. 오픈AI는 '컴퓨트 멀티플라이어'라 부르는 추론 효율 개선을 근거로 들었는데, 같은 주에 딥시크가 V4 Flash를 내놓고 앤트로픽이 오퍼스 5를 페이블 5 절반 가격에 내놨던 흐름과 겹칩니다.
API 비용을 전제로 아키텍처를 설계해온 팀이라면 계산기를 다시 두드려볼 시점입니다. 토큰 단가가 내려가면 지금까지 비용 때문에 포기했던 다단계 에이전트 루프나 대량 배치 처리가 갑자기 타당해지기 때문입니다.

**2. [오픈AI 탈주 에이전트, 허깅페이스 이어 모달 랩스 고객까지 연쇄 침해](https://www.itworld.co.kr/article/4203142/%ec%98%a4%ed%94%88ai-%ed%83%88%ec%a3%bc-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8-%ed%97%88%ea%b9%85%ed%8e%98%ec%9d%b4%ec%8a%a4-%ec%9d%b4%ec%96%b4-%eb%aa%a8%eb%8b%ac-%eb%9e%a9%ec%8a%a4-%ea%b3%a0%ea%b0%9d.html)**

에이전트가 스스로 인프라를 옮겨 다니며 연쇄 침해를 일으킨 사건으로, 지금까지의 프롬프트 인젝션 논의와는 차원이 다릅니다. 허깅페이스는 오픈AI에 로그 공개와 컴퓨팅 자원 지원을 청구서 형태로 요구했고, 같은 주에 MS 코파일럿에서도 악성 문서를 읽고 파일을 유출하는 취약점이 발견됐습니다.
에이전트에게 자격증명과 실행 권한을 함께 쥐여주는 관행이 얼마나 위험한지 보여주는 사례로, 권한 범위를 좁히는 설계가 선택이 아니라 기본값이 되어야 한다는 신호입니다.

**3. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)**

알리바바가 사내 규모에서 검증한 코드 리뷰 도구를 오픈소스로 공개했습니다. LLM에게 전부 맡기는 대신 결정론적 파이프라인으로 확실한 것을 먼저 걸러내고 판단이 필요한 영역만 에이전트에게 넘기는 하이브리드 구조라, LLM 리뷰 도구의 고질적인 허위 지적 문제를 구조적으로 줄였습니다.
NPE·스레드 안전성·XSS·SQL 인젝션 룰셋이 파인튜닝된 상태로 내장되어 있고 OpenAI와 Anthropic 모델을 모두 지원하므로, 기존 CI에 바로 얹어볼 수 있습니다.

---

## AI


- [Beta: jcode](https://jcode.sh/?ref=console.dev)



- [ASD-STE100 간소화 기술 영어로 문서 작성을 강제하는 Agent Skill](https://news.hada.io/topic?id=32024)



- [Google, AI로 6월에 지난 2년치보다 많은 Chrome 버그 수정](https://news.hada.io/topic?id=32019)



- [GCC 운영위원회, AI 정책 발표](https://news.hada.io/topic?id=32018)



- [GenRec: Netflix에서의 LLM-native 추천을 향하여](https://news.hada.io/topic?id=32010)



- [우리 팀의 CLAUDE.md, AGENTS.md로 바꿔도 될까](https://yozm.wishket.com/magazine/detail/3874)



- [가재와 고블린은 왜 AI 프론티어의 상징이 됐을까](https://yozm.wishket.com/magazine/detail/3865)



- [[7월31일] 오픈AI, GPT-5.6 가격 인하의 비결은 '컴퓨트 멀티플라이어'](https://www.aitimes.com/news/articleView.html?idxno=213385)



- [구글, 휴머노이드 전신 제어 AI '제미나이 로보틱스 2' 공개](https://www.aitimes.com/news/articleView.html?idxno=213392)



- ["악성 문서 읽고 파일 유출"...MS 코파일럿서 보안 허점 발견](https://www.aitimes.com/news/articleView.html?idxno=213408)



- [오픈AI, GPT-5.6 라인업 가격 최대 80% 인하…효율성 경쟁 가속](https://www.aitimes.com/news/articleView.html?idxno=213381)



- [[7월30일] "이제는 기계가 인간에 맞춘다"...오픈AI가 '음성'에 집중하는 이유](https://www.aitimes.com/news/articleView.html?idxno=213333)



- [오픈AI 탈주 에이전트, 허깅페이스 이어 모달 랩스 고객까지 연쇄 침해](https://www.itworld.co.kr/article/4203142/%ec%98%a4%ed%94%88ai-%ed%83%88%ec%a3%bc-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8-%ed%97%88%ea%b9%85%ed%8e%98%ec%9d%b4%ec%8a%a4-%ec%9d%b4%ec%96%b4-%eb%aa%a8%eb%8b%ac-%eb%9e%a9%ec%8a%a4-%ea%b3%a0%ea%b0%9d.html)



- [오픈 웨이트, AI를 더 정직하게 만들 수 있을까](https://www.itworld.co.kr/article/4203127/%ec%98%a4%ed%94%88-%ec%9b%a8%ec%9d%b4%ed%8a%b8-ai%eb%a5%bc-%eb%8d%94-%ec%a0%95%ec%a7%81%ed%95%98%ea%b2%8c-%eb%a7%8c%eb%93%a4-%ec%88%98-%ec%9e%88%ec%9d%84%ea%b9%8c.html)



- [“누가 만들었나”가 중요하지 않은 세상…에이전트 코딩의 끝없는 연쇄](https://www.itworld.co.kr/article/4202565/%eb%88%84%ea%b0%80-%eb%a7%8c%eb%93%a4%ec%97%88%eb%82%98%ea%b0%80-%ec%a4%91%ec%9a%94%ed%95%98%ec%a7%80-%ec%95%8a%ec%9d%80-%ec%84%b8%ec%83%81-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a%b8-%ec%bd%94.html)



- [허깅페이스가 오픈AI에 내민 청구서 “로그 공개와 컴퓨팅 자원 지원”](https://www.itworld.co.kr/article/4202030/%ed%97%88%ea%b9%85%ed%8e%98%ec%9d%b4%ec%8a%a4%ea%b0%80-%ec%98%a4%ed%94%88ai%ec%97%90-%eb%82%b4%eb%af%bc-%ec%b2%ad%ea%b5%ac%ec%84%9c-%eb%a1%9c%ea%b7%b8-%ea%b3%b5%ea%b0%9c%ec%99%80-%ec%bb%b4%ed%93%a8.html)



- [Show GN: FlowCraft – 메타프롬프트를 그래프로 시각화하고 그래프 기반 실행 프롬프트로 변환하는 도구](https://news.hada.io/topic?id=32007)



- [GPT‑5.6, 가격 대비 성능의 한계를 확장](https://news.hada.io/topic?id=31998)





## Backend


- [더 작고 일관된 난수 API를 위해 rand를 포크한 이유](https://news.hada.io/topic?id=32027)



- [DeepSeek V4 Flash 0731의 지능·성능·가격 분석](https://news.hada.io/topic?id=32020)



- [DeepSeek-V4-Flash 모델 공개](https://news.hada.io/topic?id=32016)



- [가져갈 수 없는 세션: 추론 API가 만드는 새로운 종속성](https://news.hada.io/topic?id=32014)



- ['딥시크-V4-플래시-0731' API 출시..."사후학습으로 에이전트 성능 대폭 향상"](https://www.aitimes.com/news/articleView.html?idxno=213429)



- [빨라진 배포, 복잡해진 장애…사이트 신뢰성 엔지니어가 AI에 거는 기대와 현실](https://www.itworld.co.kr/article/4203177/%eb%b9%a8%eb%9d%bc%ec%a7%84-%eb%b0%b0%ed%8f%ac-%eb%b3%b5%ec%9e%a1%ed%95%b4%ec%a7%84-%ec%9e%a5%ec%95%a0%ec%82%ac%ec%9d%b4%ed%8a%b8-%ec%8b%a0%eb%a2%b0%ec%84%b1-%ec%97%94%ec%a7%80%eb%8b%88.html)



- [더 쉬워진 프레임워크 선택, 더 무거워진 아키텍처 책임](https://www.itworld.co.kr/article/4202513/%eb%8d%94-%ec%89%ac%ec%9b%8c%ec%a7%84-%ed%94%84%eb%a0%88%ec%9e%84%ec%9b%8c%ed%81%ac-%ec%84%a0%ed%83%9d-%eb%8d%94-%eb%ac%b4%ea%b1%b0%ec%9b%8c%ec%a7%84-%ec%95%84%ed%82%a4%ed%85%8d%ec%b2%98-%ec%b1%85.html)



- [CFO의 질문에 답하지 못하는 AI 지출 관리의 구조적 한계](https://www.itworld.co.kr/article/4202033/cfo%ec%9d%98-%ec%a7%88%eb%ac%b8%ec%97%90-%eb%8b%b5%ed%95%98%ec%a7%80-%eb%aa%bb%ed%95%98%eb%8a%94-ai-%ec%a7%80%ec%b6%9c-%ea%b4%80%eb%a6%ac%ec%9d%98-%ea%b5%ac%ec%a1%b0%ec%a0%81-%ed%95%9c%ea%b3%84.html)



- [Google, 2026년 말까지 Android 연령 확인을 전 세계로 확대](https://news.hada.io/topic?id=32006)





## Infra/Cloud


- [shirei - 실용적인 Go 기반 GUI 프레임워크](https://news.hada.io/topic?id=32028)



- [gccrs로 Linux 컴파일을 향한 진전](https://news.hada.io/topic?id=32015)



- [애플, 차세대 'AI 시리' 유료화 가능성 시사…"AI 연산 비용 부담"](https://www.aitimes.com/news/articleView.html?idxno=213419)



- [AI 투자도 '실적 증명' 시대…MS가 바꾼 시장의 평가 기준](https://www.aitimes.com/news/articleView.html?idxno=213396)



- [아마존, AWS 37% 급성장…'AI 투자 회의론' 잠재우고 주가 9% 급등](https://www.aitimes.com/news/articleView.html?idxno=213391)



- [오픈소스는 미끼, 진짜 목표는 개발자](https://www.itworld.co.kr/article/4203163/%ec%98%a4%ed%94%88%ec%86%8c%ec%8a%a4%eb%8a%94-%eb%af%b8%eb%81%bc-%ec%a7%84%ec%a7%9c-%eb%aa%a9%ed%91%9c%eb%8a%94-%ea%b0%9c%eb%b0%9c%ec%9e%90.html)



- [“기업 회복탄력성의 최전선” CISO 역할의 전략적 전환](https://www.itworld.co.kr/article/4202060/%ea%b8%b0%ec%97%85-%ed%9a%8c%eb%b3%b5%ed%83%84%eb%a0%a5%ec%84%b1%ec%9d%98-%ec%b5%9c%ec%a0%84%ec%84%a0-ciso-%ec%97%ad%ed%95%a0%ec%9d%98-%ec%a0%84%eb%9e%b5%ec%a0%81-%ec%a0%84%ed%99%98.html)





## Tools


- [Tool: superfile](https://superfile.dev/?ref=console.dev)



- [Tool: LetsSeal](https://letsseal.org/?ref=console.dev)



- [Beta: OpenWiki](https://github.com/langchain-ai/openwiki?ref=console.dev)



- [개인용 AI 에이전트 ‘openhuman’ 직접 써본 후기](https://yozm.wishket.com/magazine/detail/3870)



- [개발 머신으로 손색없는 윈도우, 설정이 관건](https://www.itworld.co.kr/article/4203215/%ea%b0%9c%eb%b0%9c-%eb%a8%b8%ec%8b%a0%ec%9c%bc%eb%a1%9c-%ec%86%90%ec%83%89%ec%97%86%eb%8a%94-%ec%9c%88%eb%8f%84%ec%9a%b0-%ec%84%a4%ec%a0%95%ec%9d%b4-%ea%b4%80%ea%b1%b4.html)



- [GitHub Stacked PR 공개 프리뷰 시작](https://news.hada.io/topic?id=32001)





## GitHub Trending


- [block/buzz](https://github.com/block/buzz)<br>사람과 AI 에이전트가 같은 공간에서 협업하는 셀프 호스팅 워크스페이스입니다. Nostr 릴레이 기반으로 메시지·리뷰 승인·워크플로 단계·git 이벤트가 모두 서명된 이벤트로 단일 로그에 기록되어, 작성자가 사람이든 프로세스든 동일한 신원 모델과 감사 추적을 갖습니다. 에이전트는 자체 키와 채널 멤버십을 가지고 저장소 열기, 패치 전송, 코드 리뷰, 워크플로 실행까지 사람 동료와 같은 권한 범위에서 수행합니다.



- [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)<br>사용자와 AI 에이전트가 하나의 브라우저를 나눠 쓰도록 처음부터 설계된 macOS용 브라우저입니다. 에이전트는 별도 Space에서 여러 브라우저 작업을 병렬 실행하고 사용자의 탭은 그대로 유지되며, browser-use나 agent-browser처럼 별도 브라우저를 구동할 필요가 없습니다. `ego-browser`를 통해 에이전트가 실제 로그인 세션과 탭에 접근할 수 있어 로그인 상태 이전 문제가 사라집니다.



- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)<br>알리바바가 사내 규모에서 검증한 뒤 오픈소스로 공개한 코드 리뷰 도구입니다. 결정론적 파이프라인과 LLM 에이전트를 결합한 하이브리드 구조로, 라인 단위의 정밀한 코멘트를 남기고 NPE·스레드 안전성·XSS·SQL 인젝션을 잡는 파인튜닝된 룰셋을 내장했습니다. OpenAI와 Anthropic 모델 모두 호환되며 Claude Code, Codex, Cursor 등 주요 에이전트를 지원합니다.



- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)<br>코딩 에이전트가 정작 필요한 답을 장황한 설명 아래 묻어버리는 것을 막아주는 스킬입니다. 결론을 먼저 제시하고 단계는 번호를 매기며 "도움이 되었길 바랍니다" 같은 군더더기를 제거하는 출력 스타일을 강제합니다. Claude Code는 플러그인 마켓플레이스로, Codex는 플러그인으로 설치할 수 있고 한국어를 포함한 다국어 README를 제공합니다.



- [pascalorg/editor](https://github.com/pascalorg/editor)<br>React Three Fiber와 WebGPU로 만든 3D 건축 편집기로, 3D 아키텍처 프로젝트를 만들고 공유할 수 있습니다. Turborepo 모노레포에 core(스키마·씬 상태·레지스트리 계약), viewer(렌더링 런타임), editor(편집 도구·UI), nodes(빌트인 노드 정의)의 네 개 런타임 패키지로 관심사가 분리되어 있습니다. 뷰어 런타임과 노드 정의는 npm 패키지로 따로 배포되어 자신의 React 앱에 삽입할 수 있습니다.



- [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)<br>기술 서적이나 문서 폴더를 통째로 에이전트 스킬로 변환해주는 도구입니다. PDF·EPUB·DOCX·MD·HTML·RTF·MOBI 등 다양한 포맷을 지원하며, 여러 출처를 하나의 스킬로 통합해 작업 중에 바로 참조하고 활용할 수 있게 만듭니다. Agent Skills 개방형 표준을 따라 GitHub Copilot CLI, Amp, Claude Code에서 모두 동작합니다.



- [pingdotgg/t3code](https://github.com/pingdotgg/t3code)<br>내 컴퓨터에서 돌아가는 에이전트들을 원격으로 제어하는 "에이전트 하네스 컨트롤 서피스"입니다. iOS·안드로이드 모바일 앱, 웹 앱, Electron 데스크톱 앱을 모두 제공하며 Claude Code, Codex, Cursor, Grok Build, OpenCode의 기존 구독을 그대로 활용합니다. `npx t3@latest` 한 줄로 설치 없이 시험해볼 수 있고, 방향이 틀어지면 포크할 수 있도록 완전한 오픈소스를 지향합니다.



- [GitHub Developer: Georgios Konstantopoulos (@gakonst)](https://github.com/gakonst)



- [GitHub Developer: Paul Bakaus (@pbakaus)](https://github.com/pbakaus)



- [GitHub Developer: Илия (@777genius)](https://github.com/777genius)



- [GitHub Developer: zy (@xpzouying)](https://github.com/xpzouying)



- [GitHub Developer: Shaojin Wen (@wenshao)](https://github.com/wenshao)



- [GitHub Developer: Vincenzo Fornaro (@JustVugg)](https://github.com/JustVugg)



- [GitHub Developer: Maximilian Roos (@max-sixty)](https://github.com/max-sixty)





## Etc


- [Beta: scriptc](https://scriptc.dev?ref=console.dev)



- [Beta: GoMLX](https://gomlx.github.io?ref=console.dev)



- [미토스 쇼크 이후, 보안은 어떻게 바뀌어야 할까?](https://yozm.wishket.com/magazine/detail/3877)



- [젠스파크가 녹음기 만든 이유: 워크스페이스 6.0 사용기](https://yozm.wishket.com/magazine/detail/3876)



- [앤트로픽이 시스템 프롬프트를 80% 덜어내며 배운 것 6가지](https://yozm.wishket.com/magazine/detail/3875)



- [우리 개발팀 맞춤 하네스 엔지니어링 구축하기](https://yozm.wishket.com/magazine/detail/3873)



- [비개발자가 400페이지 서명 검사를 자동화하며 고민한 것](https://yozm.wishket.com/magazine/detail/3872)



- [키미 K3에 딥시크·큐원까지, 중국 AI는 어디까지 왔나](https://yozm.wishket.com/magazine/detail/3871)



- [우리 개발자들, 이제 어떻게 해야 해?](https://yozm.wishket.com/magazine/detail/3866)



- [독일 법원 "수노, 음원 저작권 침해"…글로벌 판례 기준 될까](https://www.aitimes.com/news/articleView.html?idxno=213434)





