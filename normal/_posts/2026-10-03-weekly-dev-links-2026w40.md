---
layout: post
title: "주간 테크/개발 뉴스 #2026 9/27 ~ 10/3"
date: 2026-10-03
categories: [normal]
tags: [weekly, dev-news, indie-radar, observability, books]
---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — 한 주에 쏟아진 Gemini 4 Argon·Sonnet 5.5·GPT-6.1 Sol, OpenAI의 상시 에이전트 Dots, Git 3.0 SHA-256 기본값 논쟁
- [🚀 Indie Radar (6)](#indie-radar) — 위치를 직접 정하는 다이어그램 언어 reladraw, 누적 매출 대부분을 최근 30일에 올린 에이전트용 영상 도구 Hypit-AI
- [🔭 모니터링 사례 & 강좌 (4)](#observability) — 그래프 읽는 법을 정리한 서버 모니터링 분석 가이드, 로그 때문에 커넥션 풀이 마른 무신사 장애기
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [구글, '제미나이 4 아르곤' 공개…성능 1위 탈환에도 "일반 사용 제한"](https://www.aitimes.com/news/articleView.html?idxno=215821)

Google이 9월 30일 차세대 플래그십 Gemini 4 Argon을 공개했습니다. 자체 공개한 18개 벤치마크 중 13개에서 1위를 차지했고, 장기 소프트웨어 엔지니어링 평가 DeepSWE v1.1에서는 77.9%로 Claude Opus 5.5(74.2%)와 GPT-6 Astra(74.1%)를 앞섰습니다. 출력 토큰 한도도 6만 4천에서 100만으로 늘려, 한 번의 작업 흐름에서 긴 추론과 코드 생성을 이어 가도록 했습니다.
다만 초기 접근은 'Fairwind' 프로그램을 통한 사이버 보안 방어 파트너와 미국 정부의 출시 전 평가 참가자로 제한됐고, AI Ultra 구독자와 일반 API 배포는 이후 단계적으로 진행됩니다. 가격은 프로모션 기간 100만 토큰당 입력 $2/출력 $10, 이후 정가 $4/$20입니다.
Artificial Analysis 지능 지수에서는 53점으로 GPT-6 Astra와 같은 수준이어서, 고난도 과학·터미널 작업까지 합친 종합 점수로는 1위가 아닙니다. 커뮤니티에서는 반격에 성공했다는 평가와 함께 당장 쓸 수 없는 "그림의 떡"이라는 불만이 함께 나왔습니다.

관련: [Google 블로그: Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

### 2. [앤트로픽, '클로드 소네트 5.5' 공개…오퍼스급 지능에 최강 가성비](https://www.aitimes.com/news/articleView.html?idxno=215734)

Anthropic이 9월 28일 Claude Sonnet 5.5를 내놓았습니다. 가격은 Sonnet 5와 같은 100만 토큰당 입력 $2/출력 $10(캐시 읽기 $0.20)이지만, 같은 일을 더 적은 토큰으로 끝내 작업당 비용이 최대 30% 줄었다고 밝혔습니다.
Terminal-Bench 4.0에서 70.6%를 기록해 Sonnet 5(10.3%)는 물론 Opus 5.5(66.4%)도 넘었고, Artificial Analysis 지능 지수에서는 56점으로 Opus 5.5(58점)에 이어 2위에 올랐습니다. 빠르고 저렴한 Haiku 5.5도 몇 주 안에 나올 예정입니다.
같은 주 The Information은 두 회사의 기업 영업 방식 차이도 전했습니다. Anthropic은 약정 사용량 한도에 닿으면 할인을 바로 끝내고 재계약을 제안하는 반면, OpenAI는 유예 기간을 주거나 더 공격적인 할인으로 고객을 끌어오고 있다는 내용입니다. 모델 성능 경쟁이 그대로 가격·계약 경쟁으로 이어지는 모습입니다.

관련: [Anthropic: Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) · [AI타임스: "한도 차면 할인 끝" 앤트로픽](https://www.aitimes.com/news/articleView.html?idxno=215761)

### 3. [오픈AI, 24시간 자율 에이전트 '닷츠' 공개…소비자용 아닌 B2B 승부수](https://www.aitimes.com/news/articleView.html?idxno=215779)

OpenAI가 9월 29일 DevDay 2026에서 상시 작동하는 에이전트 Dots를 공개했습니다. GPT-6 Astra 기반으로 각자 클라우드 컴퓨터와 브라우저를 갖고, 플러그인으로 4,000개가 넘는 앱에 연결되며, ChatGPT·Slack·Teams 어디서든 같은 맥락으로 대화합니다. 개발자라면 고객 피드백을 지켜보다 작은 버그 수정을 직접 만들어 PR로 가져오는 식의 사용 예를 들었습니다.
사용자가 자리를 비운 동안의 '선제적 리서치'는 메시지 발송이나 데이터 변경이 불가능한 읽기 전용 도구로만 돌고, 저장된 비밀번호는 모델에 노출하지 않으며, 비밀번호 변경 같은 민감한 작업은 항상 사람이 하도록 했습니다. Pro와 Business Premium부터 배포하고, 자체 ID와 권한을 갖고 조직 업무를 맡는 'specialist dots'는 엔터프라이즈 파일럿으로 시작합니다.
같은 행사에서 GPT-6.1 Sol(100만 토큰당 $2/$10, 캐시 입력 $0.10)과 외부 서비스에 ChatGPT 계정으로 로그인해 구독 사용량을 그대로 쓰는 기능도 나왔습니다. 반면 상위 모델 GPT-6.1 Astra는 기만 행동과 무단 접근 등 에이전트 안전 문제로 출시를 철회했습니다.

관련: [OpenAI: Introducing dots](https://openai.com/index/introducing-dots/) · [AI타임스: GPT-6.1 솔](https://www.aitimes.com/news/articleView.html?idxno=215778) · [AI타임스: 로그인과 플러그인](https://www.aitimes.com/news/articleView.html?idxno=215882)

### 4. [Pi 1.0 출시: "MCP는 안 한다"던 미니멀 코딩 에이전트, MCP를 코어에 넣다](https://earendil.com/posts/pi-1-0/)

매주 수십만 명이 쓰는 터미널 코딩 에이전트 Pi가 1.0을 냈습니다. 새 기능은 JavaScript로 여러 도구 호출을 엮는 Codemode(MCP와 Jev 같은 비LLM 모델, 이미지 모델 기본 지원), 여러 모델을 하나처럼 쓰는 가상 모델, 대화 도중 프롬프트와 도구를 바꾸는 시스템 메시지입니다. 데모에서는 Claude가 계획하고 GPT가 구현하며 Jev가 단계 전환 시점을 판단했습니다.
화제가 된 건 MCP입니다. 그동안 MCP를 공개적으로 낮게 평가해 온 팀이 별도 글에서 MCP가 1년 사이 많이 달라졌고, MCP를 위해 필요한 변경이 Jev 같은 다른 모델을 붙이는 데도 유용해서 코어에 넣었다고 설명했습니다.
터미널 밖에서 오래 이어지는 대화와 작업을 위한 실험 패키지 Pi Durable도 함께 공개됐습니다. 둘 다 MIT 라이선스입니다.

관련: [You said no MCP](https://earendil.com/posts/you-said-no-mcp/) · [Pi Durable](https://earendil.com/posts/pi-durable/) · [GeekNews](https://news.hada.io/topic?id=34632)

### 5. [Cloudflare, Jev 호환 오픈 판단 모델 Clef 공개…Amazon·Upstage도 가세](https://blog.cloudflare.com/clef-decision-models/)

문장 대신 선택지와 확률을 돌려주는 '판단 모델'이 Jev 이후 한 달도 안 돼 경쟁 분야가 됐습니다. Cloudflare는 Clef와 Clef-flash를 Apache 2.0으로 공개했습니다. Jev API와 호환되고, 비전 인코더로 이미지도 분류하며 컨텍스트는 64k(Jev는 32k)입니다. Qwen 백본을 고정한 채 선택지를 병렬로 채점하는 비자기회귀 방식이라, 자사 위협 인텔리전스 팀의 도메인 분류에서 2.2초가 걸려 gpt-oss-120b(4.7초)보다 빨랐다고 합니다. 고객이 직접 조정할 수 있는 RL 파인튜닝 제품도 함께 내놓았습니다.
Amazon은 Qwen3.5-2B 기반 Strands Decider 2B를 학습 데이터와 스크립트까지 공개했습니다. RTX 3090에서 짧은 작업의 중앙값 지연이 약 115ms로 로컬 실행을 겨냥했습니다. Upstage는 OpenRouter에 Solar Decide를 내놓고, JevBench 공개 문항에서 정확도 87.0%로 Jev 1.13(86.1%)보다 높고 판단당 0.14초로 더 빠르다고 밝혔습니다.
API가 호환되니 모델 이름만 바꿔 비교해 볼 수 있다는 점이 이 분야 경쟁을 더 빠르게 만들고 있습니다.

관련: [AI타임스: 아마존 스트랜즈 디사이더 2B](https://www.aitimes.com/news/articleView.html?idxno=215887) · [AI타임스: 업스테이지 솔라 디사이드](https://www.aitimes.com/news/articleView.html?idxno=215919)

### 6. [Git 3.0의 SHA-256 기본값 전환은 값비싼 실수다](https://blog.gitbutler.com/git-3-sha-256)

GitHub 공동 창업자 Scott Chacon이 Git 3.0에서 새 저장소의 기본 해시를 SHA-1에서 SHA-256으로 바꾸는 계획에 반대하는 글을 썼습니다. SHA-1은 큰 비용을 들이면 의도적인 충돌을 만들 수 있지만, 이미 있는 파일과 같은 해시를 만드는 제2역상 공격은 여전히 현실적이지 않고, 실제 공급망 공격은 해시가 아니라 쓰기 권한 탈취나 사회공학으로 일어난다는 주장입니다.
반면 전환 비용은 큽니다. SHA-1 저장소와 SHA-256 저장소가 나뉘면 서브모듈과 Git 라이브러리 호환성을 맞춰야 하고, 서명, 커밋 링크, 해시 길이를 가정한 도구도 영향을 받습니다. 대안으로 SHA-1을 콘텐츠 식별자로 두고 별도로 계산한 강한 해시를 서명에 넣는 방식을 제안했으며, 개념 증명은 Chromium(35GB, 210만 파일)을 5초에 처리했습니다.
해시 길이를 가정한 스크립트나 도구가 있다면 `git init --object-format=sha256`으로 미리 시험해 볼 만합니다.

관련: [GeekNews](https://news.hada.io/topic?id=34627)

### 7. [Debian 커널 보안 업데이트 한 번에 CVE 1,313건](https://lwn.net/Articles/1097401/)

Debian이 stable(trixie) 커널 보안 권고 DSA-6528-1을 냈는데, 한 권고에 담긴 CVE가 1,313건입니다. 권한 상승, 서비스 거부, 정보 유출로 이어질 수 있는 취약점들이 한꺼번에 수정됐습니다.
커뮤니티에서는 숫자 자체가 화제였습니다. 요즘은 커널 버그 수정 대부분이 CVE를 받는다는 지적, 아직 CVSS 점수가 없는 항목이 많지만 점수가 매겨진 것 중엔 7.0 이상도 적지 않다는 관찰, AI 도움으로 찾은 버그가 늘어난 것 아니냐는 질문이 이어졌습니다. 올해 CVE 번호가 처음으로 10만을 넘었다는 언급도 있었습니다.
CVE를 하나씩 검토해서 패치 여부를 정하는 방식은 이 규모에선 사실상 불가능합니다. 배포판 커널 업데이트를 정기적으로 따라가는 체계가 그만큼 중요해졌습니다.

### 8. [Apple, macOS '전체 디스크 접근' 권한 부여 절차 강화 예고](https://developer.apple.com/news/?id=p6zjojqw)

Apple이 10월 2일 개발자 공지로 macOS의 Full Disk Access 권한에 추가 통제를 도입하겠다고 밝혔습니다. 이 권한은 원래 백업 앱이 제대로 동작하도록 개인정보 보호 통제를 대부분 우회하게 해 주는 장치인데, 일부 앱이 사용자가 충분히 이해하지 못한 상태에서 파일, 메일, 메시지, 브라우징 기록까지 읽는 데 쓰고 있다는 설명입니다. 메신저 앱이라면 대화 상대의 개인정보까지 노출된다는 점도 짚었습니다.
앞으로는 정말 원하는 사용자만 매우 명시적인 동작을 거쳐 권한을 줄 수 있도록 바뀝니다. Apple은 AI 에이전트가 더 유능하고 자율적이 될수록 이런 권한의 위험이 크게 커진다고 이유를 들었습니다. 구체적인 방식과 적용 시점은 아직 공개하지 않았습니다.
최근 Mac용 ChatGPT의 메시지 앱 연동이나 Meta Muse처럼 이 권한을 요구하는 데스크톱 에이전트가 늘어난 상황이라, Full Disk Access에 기대는 앱을 배포하고 있다면 권한 요청 흐름과 안내 문구를 미리 점검해 둘 필요가 있습니다.

관련: [AI타임스](https://www.aitimes.com/news/articleView.html?idxno=215938) · [GeekNews](https://news.hada.io/topic?id=34706)

### 9. [개발 의뢰로 위장해 git post-checkout 훅으로 악성 코드를 실행하려 한 표적 공격](https://frankwiles.com/posts/i-got-targeted/)

Django Steering Council 멤버이자 개발사 REVSYS 대표인 Frank Wiles가 직접 겪은 공격을 공개했습니다. 교육 분야 웹 앱 개발 문의로 시작해, 상대는 미팅 전에 프로젝트 자료를 읽고 NDA에 서명해 달라며 Markdown 문서가 든 Dropbox 폴더를 공유했습니다. NDA 파일을 찾을 수 없다고 하자 저장소의 NDA 브랜치로 전환해서 작성해 달라고 요구했습니다.
이 요청을 수상하게 여긴 Wiles가 저장소를 살펴보니 post-checkout 훅이 들어 있었습니다. 브랜치를 바꾸는 순간 Vercel 앱을 명령·제어 서버로 삼아 운영체제에 맞는 바이너리를 내려받아 실행하고, 훅 자신을 지우도록 되어 있었습니다. Wiles는 GitHub 계정이나 고객사 접근 권한을 노린 것으로 보고 Dropbox와 Vercel에 신고했습니다. 공격자는 실제 개발사 대표까지 사칭했습니다.
`git clone`으로 받은 저장소에는 훅이 따라오지 않지만, 폴더째 공유된 저장소는 `.git/hooks`까지 그대로 옵니다. 출처가 불분명한 저장소에서 checkout이나 빌드를 하기 전에 `.git/hooks`부터 확인하는 습관이 필요합니다. 과제형 면접이나 채용 제안을 가장한 비슷한 공격도 잇따르고 있습니다.

관련: [GeekNews](https://news.hada.io/topic?id=34709)

### 10. [Supabase, 1억 5천만 달러 투자 유치하고 Turso 인수](https://supabase.com/blog/supabase-is-acquiring-turso)

Postgres 기반 백엔드 플랫폼 Supabase가 싱가포르 국부펀드 GIC 주도로 1억 5천만 달러를 투자받고, SQLite를 Rust로 다시 작성한 Turso를 인수한다고 발표했습니다. 인수 금액은 공개하지 않았습니다.
Supabase는 이미 주당 100만 개 넘는 데이터베이스를 만들고 있다며, 에이전트가 파일을 만들듯 데이터베이스를 만드는 시대에는 지금과 다른 인프라가 필요하다고 설명했습니다. Turso는 서버 한 대가 수백만 개 데이터베이스를 관리하며 필요할 때만 올리고 쓰지 않을 때는 멈추는 구조라, 에이전트마다 데이터베이스를 하나씩 주는 패턴에 맞습니다.
기존 사용자에게 바뀌는 것은 없으며, Supabase는 Postgres, Turso는 SQLite 작업을 이어 갑니다. 작은 작업은 SQLite로 시작하고 커지면 Postgres로 옮기는 경로를 같은 개발 경험으로 묶겠다는 구상입니다.

관련: [SiliconANGLE](https://siliconangle.com/2026/10/02/database-startup-supabase-raises-150m-acquires-turso/)

---

## 🚀 Indie Radar
{: #indie-radar}

### [reladraw](https://github.com/reladraw/reladraw) · 오픈소스 다이어그램 언어 · Show HN 411점

Mermaid나 D2처럼 텍스트로 다이어그램을 쓰되, 배치를 자동에 맡기지 않고 "app 오른쪽, 같은 높이"처럼 상대 위치로 직접 정하는 언어입니다. 좌표를 일일이 고르는 draw.io와 자동 배치 언어의 중간을 노렸습니다. 사람뿐 아니라 에이전트가 다루기 쉽게 만들었다는 점도 내세워, 코딩 에이전트용 스킬 설치 명령을 함께 제공합니다. Apache 2.0이며 설치 없이 써 볼 수 있는 플레이그라운드가 있습니다.

### [Lofi Cities](https://loficities.com/) · 웹 토이 · Show HN 319점

픽셀아트 도시의 밤 풍경에 브라우저에서 실시간으로 생성한 lofi 음악을 붙인 무료 웹 앱입니다. 도시마다 480×270 픽셀 애니메이션이 4분 주기로 끊김 없이 반복되고, 날씨와 랜드마크, 도시 소리가 다릅니다. 교토의 단풍 밤, 안개 낀 베네치아 같은 도시가 계속 추가되고 있고, 설치나 가입 없이 휴대폰에서도 돌아갑니다.

### [Hypit-AI](https://trustmrr.com/startup/hypit-ai) · 오픈소스 영상 SaaS · MRR $14.0k (TrustMRR 인증)

Claude Code나 Codex 같은 코딩 에이전트에게 영상 제작용 언어와 런타임을 주는 도구입니다. 참고할 바이럴 영상을 넣으면 다시 실행할 수 있는 영상 프로그램으로 바꾸고, 자막과 B-roll을 초가 아닌 단어 기준으로 묶어 대본을 바꿔도 타이밍이 자동으로 맞춰집니다. 셀프 호스팅은 무료이고 멀티테넌트 SaaS용 상업 라이선스로 돈을 법니다. 누적 매출 $30.5k 거의 전부가 최근 30일($30.5k)에 나왔습니다.

### [VoiceStudio](https://github.com/debpalash/VoiceStudio) · 오픈소스 데스크톱 앱 · GitHub 주간 ★16.8k

"완전 로컬 ElevenLabs 대안"을 내건 음성 앱으로, 음성 복제와 음성 디자인, 영상 더빙, 받아쓰기, 오디오북 제작을 646개 언어로 지원합니다. 기본 엔진은 k2-fsa의 OmniVoice이고, 에이전트가 쓸 수 있는 로컬 API와 MCP도 제공합니다. 전용 GPU가 없어도 CPU로 느리게나마 돌아가며, 이번 주까지 누적 스타 5만 2천 개를 넘겼습니다. 라이선스는 AGPL-3.0입니다.

### [Tiny Brutalism](https://placeholders.itch.io/tiny-brutalism) · 인디 게임 · itch.io 신작 인기 10위

9월 25일 나온, 브루탈리즘 건축에서 영감을 받은 아늑한 샌드박스 건설 게임입니다. 목표도 정답도 없이 콘크리트 탑이나 이상한 기념비, 아주 큰 벽을 쌓기만 하면 됩니다. 클릭으로 블록을 놓고 낮과 밤을 바꿀 수 있으며, Windows·macOS·Linux용으로 최소 $5에 판매 중입니다.

### [SEEDS의 PasRISCV](https://againstallodds.games/blog/2026/10/03/our-risc-v-emulator-pasriscv/) · 게임 속 오픈소스 에뮬레이터 · Show HN

우주 게임 SEEDS는 게임 안 컴퓨터에서 실제 Linux를 돌리고, 행성 개요 같은 인게임 도구를 그 위의 네이티브 Linux 프로그램으로 만들었습니다. 이를 위해 개발사가 Object Pascal로 만든 64비트 RISC-V 에뮬레이터 PasRISCV는 사용자 공간만이 아니라 디스플레이, 저장 장치, 인터럽트까지 기기 전체를 에뮬레이션하며, Alpine Linux가 그대로 부팅됩니다. 에뮬레이터는 zlib 라이선스 오픈소스로 공개돼 있습니다.

---

## 🔭 모니터링 사례 & 강좌
{: #observability}

### [서버 모니터링 분석 가이드](https://kciter.so/posts/server-monitoring-analysis-guide/)

대시보드를 설치하는 글은 많아도 그래프를 읽고 진단하는 법을 다룬 글은 드물다는 문제의식에서 쓴 긴 강좌입니다. 모든 지표를 Google SRE의 네 가지 황금 신호(트래픽, 지연 시간, 에러, 포화도)로 묶고, 사용자가 겪는 증상(지연, 에러)을 먼저 본 뒤 원인(CPU, 메모리, 풀)으로 범위를 좁히는 순서를 정상·이상 패턴 애니메이션과 함께 설명합니다.
평균 대신 P50/P95/P99로 읽어야 하는 이유, 에러는 개수가 아니라 비율로 봐야 하는 이유, 장애 중 서버 지표가 전부 깨끗하면 요청이 아예 도달하지 못하는 것이라는 해석처럼 바로 써먹을 판단 기준이 많습니다. 쿠버네티스 CPU limit에 걸리면 100ms 주기마다 통째로 멈추는데 그 대기 시간은 사용률 그래프에 남지 않는다는 점, 동시 요청 수 = 초당 유입량 × 평균 처리 시간(리틀의 법칙)이라 DB가 느려지면 트래픽이 그대로여도 스레드 풀이 마르는 이유도 짚습니다.
알람은 "CPU 80% 초과" 같은 원인이 아니라 에러율 같은 증상에 걸어야 한다는 원칙과, 평시·장애 중·장애 후에 각각 무엇을 봐야 하는지까지 다룹니다.

관련: [GeekNews 요약](https://news.hada.io/topic?id=34478)

### [로그가 서비스를 죽였다: 관측성과 가용성을 동시에 잡는 법](https://techblog.musinsa.com/%EB%A1%9C%EA%B7%B8%EA%B0%80-%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC-%EC%A3%BD%EC%98%80%EB%8B%A4-4013e35a463b)

무신사의 한 고트래픽 서비스에서 요청이 정확히 30초 주기로 무더기 실패한 장애 분석기입니다. 발단은 관측성을 위한 전사 표준이었습니다. 로그에 OpenTelemetry trace_id를 넣으려는데 비동기 로거(AsyncAppender)의 워커 스레드에서는 trace_id가 비어 나오자, 표준 가이드가 동기 로깅으로 바꾸게 했습니다.
그 상태에서 DEBUG 로그가 켜진 채 트래픽이 몰리자 로그량이 평소의 약 100배가 됐습니다. 컨테이너 로그는 stdout → 커널 파이프 버퍼(약 64KB) → containerd → 로그 파일 → fluent-bit 순으로 흐르는데, 수집이 못 따라가면 버퍼가 차고 `log.info()`를 부른 요청 스레드가 멈춥니다. DB 커넥션을 쥔 채 멈추니 커넥션 풀이 고갈됐고, 30초는 커넥션 획득 타임아웃 기본값이었습니다.
해결은 30줄 남짓한 커스텀 Appender였습니다. 큐에 넣기 전, 아직 요청 스레드일 때 trace_id를 읽어 로그 이벤트에 담고 출력만 비동기로 넘겼습니다. 극한 부하에서 로그 일부를 버리더라도 요청 처리는 지키는 쪽을 택했고, 출력된 로그의 trace_id 누락은 0%였습니다. Java 사례지만 "로그 쓰기도 블로킹 I/O이고, 컨텍스트는 스레드 경계를 넘지 않는다"는 교훈은 언어와 상관없이 통합니다.

### [40초에서 10초 미만으로: Atlassian의 OpenTelemetry·Kafka·Flink 기반 장애 감지 재구축](https://www.cncf.io/blog/2026/09/30/from-40-seconds-to-under-10-rebuilding-incident-detection-on-opentelemetry-apache-kafka-and-apache-flink-on-kubernetes/)

Atlassian이 사용자 동작 이벤트로 중대 장애를 자동 감지하는 시스템을 다시 만든 18개월 기록입니다. 기존 시스템은 VM 약 90대에서 돌았고, 이벤트가 메트릭이 되기까지 좋은 날에도 40초 넘게 걸렸으며, 연간 운영비가 약 $120K에서 $230K로 불어났습니다.
새 구조는 Kafka 이벤트 버스에서 담당 제품만 고르는 구독 필터(약 770줄 YAML)로 토픽을 작게 만들고, Kubernetes 위 Flink 작업이 60초 윈도로 집계해 OpenTelemetry로 Prometheus 호환 시계열 DB에 보냅니다. 영향받은 고유 사용자 수는 윈도마다 HLL 스케치로 남겨 조회 시점에 합칩니다. 장애 영향 대시보드 비용은 로그를 훑는 대신 사전 집계 저장소를 읽게 바꾸며 월 $20,000 이상에서 약 $1,000으로 줄었습니다.
성공담으로 포장하지 않은 점이 인상적입니다. 계측 범위 안의 재현율은 약 60%에서 최고 86%까지 올랐다가 나쁜 달엔 64%로 떨어졌고, 장애 중 동시 접속 약 100명에 영향 조회 API가 다운되기도 했습니다. 실패가 아니라 이벤트의 부재를 봐야 DB 샤드 전체 장애를 잡을 수 있다는 점, 감지기의 재현율과 계측 범위를 구분해야 한다는 점이 교훈으로 정리돼 있습니다.

### [Go 서비스에 코드 수정 없이 트레이스 붙이기: OpenTelemetry 컴파일 타임 계측 v1](https://opentelemetry.io/blog/2026/go-compile-time-instrumentation-v1/)

Java는 에이전트를 붙이면 코드 수정 없이 트레이스가 나오지만, Go는 단일 정적 바이너리라 그동안 손으로 계측 코드를 넣어야 했습니다. Alibaba와 Datadog이 함께 만든 OpenTelemetry 컴파일 타임 계측이 v1에 도달하면서, `go build` 대신 `otelc go build`로 빌드만 바꾸면 애플리케이션과 의존성, 표준 라이브러리에 계측 코드가 들어갑니다.
v1 지원 목록에는 `net/http`, gRPC, `database/sql`, Gin, go-redis, segmentio/kafka-go, `log/slog` 등이 있습니다. 목록에 없는 라이브러리는 규칙을 추가하거나 직접 쓴 span과 섞어 쓰면 됩니다. 다시 빌드할 수 없는 바이너리라면 eBPF 기반 OBI, 업무 로직에 맞춘 세밀한 span이 필요하면 수동 계측이 맞다는 선택 기준도 정리돼 있습니다.
트레이싱을 처음 시도해 본다면 기존 서비스 하나를 `otelc`로 빌드해 어떤 span이 나오는지 보는 것만으로도 좋은 출발점이 됩니다. 같은 주 opentelemetry-go v1.47.0에서는 Logs API와 SDK도 처음으로 안정 버전이 됐습니다.

관련: [지원 라이브러리 목록](https://opentelemetry.io/docs/zero-code/go/compile-time/supported-libraries/) · [시작 가이드](https://opentelemetry.io/docs/zero-code/go/compile-time/getting-started/)

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [가호](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403216369) · 무라카미 하루키 · 문학동네 (주간 1위)
  - [아메리칸 학원 1](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403217560) · 이민진 · 현대문학 (주간 13위)
  - [어두운 상점들의 거리 (먼슬리 클래식)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403489383) · 파트릭 모디아노 · 문학동네 (주간 17위)
- 주목할 신간
  - [호르두발](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403426860) · 카렐 차페크 · 휴머니스트 · 정보라 옮김
  - [미미소기](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403431824) · 미쓰다 신조 · 북로드 · 듣지 말았어야 했다

### IT

- 베스트 새 진입
  - [Do it! 바이브 코딩 + 클로드 코드](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402375028) · 고경희 · 이지스퍼블리싱 (주간 15위)
  - [하네스 엔지니어링, 클로드 코드로 내 일을 대신하는 AI 에이전트 만들기](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401975476) · 서지영 · 한빛미디어 (주간 18위)
  - [요즘 AI 루프 엔지니어링](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400136983) · 박승규 · 골든래빗 (주간 20위)
- 주목할 신간
  - [핸즈온 머신러닝 with 사이킷런, 파이토치](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403219344) · 오렐리앙 제롱 · 한빛미디어 · 머신러닝 기본기부터 트랜스포머·LLM까지 직접 구현하며 배우기
  - [AI, 자동화, 전쟁](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403233062) · 앤서니 킹 · 두번째테제 · 군-테크 복합체의 부상

### 인문

- 베스트 새 진입
  - [그거 사전 2](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=400587637) · 홍성윤 · 인플루엔셜 (주간 7위)
  - [관찰 연습](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402211115) · 니콜라 노바 · 책사람집 (주간 16위)
  - [인생의 짧음에 대하여 (라틴어 원전 완역본)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=368684382) · 세네카 · 현대지성 (주간 17위)
- 주목할 신간
  - [슬픈 열대](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403343894) · 클로드 레비스트로스 · 한길사
  - [한글](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403354261) · 영케이(데이식스), 김이나 외 · 민음사

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
