---
layout: post
title: "주간 테크/개발 뉴스 #2026 10/11 ~ 10/17"
date: 2026-10-17
categories: [normal]
tags: [weekly, dev-news, indie-radar, observability, books]
---

## 이번 주 pick

![Frank Herbert, Dune](/img/2026_10_17/dune_quote.jpg)

"사람들은 기계에 생각을 넘기면 자유로워질 거라 기대했다. 하지만 그 결과는 기계를 가진 다른 사람들이 그들을 노예로 부릴 수 있게 된 것뿐이었다." — Frank Herbert, 『Dune』(1965)

<small>출처: [r/singularity](https://www.reddit.com/r/singularity/comments/1x5ty7c/this_line_was_written_in_1960s_btw_felt_like_he/)</small>

---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — 30년 묵은 NIST 곡선 시드의 정체를 밝힌 Claude, git을 버리고 자체 VCS로 옮긴 Anthropic, 공중제비 도는 Tesla Roadster
- [🚀 Indie Radar (6)](#indie-radar) — 키보드로 치는 가상 기타 Guitoro, 브라우저에서 돌아가는 Gran Turismo 4
- [🛠️ 엔지니어링 사례 & 강좌 (4)](#observability) — 엉뚱한 파드가 쫓겨나는 노드 메모리 압박, 에이전트가 쓴 코드를 리뷰하는 Claude Code 팀의 방식
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [구글, '제미나이 4 아르곤' 본격 상용화…실무 성과·제품 생태계로 승부](https://www.aitimes.com/news/articleView.html?idxno=216220)

9월 30일 일부 사이버보안 파트너에게만 공개했던 Gemini 4 Argon이 10월 13일 Google AI Studio와 Gemini API로 풀렸습니다. AI Pro·Ultra 구독자는 Gemini 앱과 검색 AI 모드에서, Ultra 구독자는 코딩 도구 Antigravity에서도 쓸 수 있습니다. API 가격은 11월 30일까지 100만 토큰당 입력 $2/출력 $10이고, 12월 1일부터 $4/$20으로 오릅니다.
구글은 성능 수치보다 실무 사례를 앞세웠습니다. 약 800개 파일, 20만 5천 줄 규모의 ADK 파이썬 코드베이스에서 Argon이 11시간 무인으로 작업해 최적화 제안 6개를 냈는데, 팀이 리뷰 후 채택한 건 2개였고 나머지는 오래된 데이터 반환 위험이나 비공개 구현 의존 때문에 뺐습니다. "에이전트는 탐색하고, 메인테이너는 걸러낸다"는 설명이 붙었습니다.
외부 평가는 조심스럽습니다. Artificial Analysis 지수에서는 Anthropic과 Meta의 최상위 모델에 뒤졌고, 한 컨설턴트는 모델은 좋지만 Antigravity가 Claude Code나 Codex만큼은 아니라고 평가했습니다.

관련: [Google DeepMind Gemini](https://deepmind.google/models/gemini/)

### 2. [Claude, 25년 넘게 미스터리였던 NIST 타원곡선 시드의 출처를 밝히다](https://www.anthropic.com/research/ecdsa-curve-origins)

NIST P-256 등 ECDSA 표준 곡선은 NSA가 설명 없이 건넨 시드 값의 해시로 계수를 정했습니다. 이 때문에 백도어 의혹이 오래 따라다녔고, 시드 출처를 찾는 현상금까지 걸려 있었습니다. 유력한 설은 NSA 직원이 "Bob과 Jerry에게 월급 인상을" 같은 농담 문구를 해시했다는 것이었는데, 그 문구로는 아무도 시드를 재현하지 못했습니다.
Anthropic 직원이 단서 없이 내부 연구 모델에 물었더니 30분이 안 돼 P-192부터 P-521까지 시드를 재현했습니다. 시드는 해시가 아니라 Unix 타임스탬프로 초기화한 C 라이브러리 `lrand48` 난수 생성기의 출력이었습니다. 일부 시드에서 32비트 단어의 최상위 비트가 모두 0인 패턴(우연일 확률 1/5,810)을 보고 `lrand48`을 짚었고, 잘린 출력에서 내부 상태를 복구하는 부분은 LLL 격자 축소로 풀었습니다.
Anthropic은 암호학적 취약점이 아니며, 오히려 누구나 재현할 수 있는 단순한 방식으로 만들어져 의도적 조작 가능성이 낮아졌다고 정리했습니다. 해야 할 조치는 없습니다.

관련: [GeekNews: 현상금 지급 소식](https://news.hada.io/topic?id=35509)

### 3. [Anthropic, 하루 3만 건 머지를 버티려 git을 버리고 자체 버전 관리 시스템 Scion으로 이전](https://www.anthropic.com/engineering/redesigning-source-control)

Anthropic 모노레포의 하루 머지 수는 5월 약 2,500건에서 9월 3만 건 이상으로 늘었습니다. main 브랜치 이력만 100GB에 가깝고, CI용 체크아웃이 하루 2,500만 번이라 그대로 받으면 하루 600PB의 git 트래픽이 나오는 규모입니다. shallow clone, sparse checkout, 수백 대의 내부 git 미러로 버티다가 한계에 닿았습니다.
그래서 5개월 만에 자체 VCS Scion을 만들고 모노레포 이전을 마쳤습니다. 클라이언트 대부분이 늘 온라인인 에이전트와 CI 작업이라는 점에 맞춰, 이력·blame·머지·리베이스는 서버가 처리하고 클라이언트는 제한된 캐시와 작업 사본만 들고 있는 구조입니다. Google Piper, Meta Sapling의 선례를 참고했다고 밝혔습니다.
코딩 에이전트가 코드 생산량을 끌어올리면 다음 병목은 소스 관리, 빌드, CI 같은 개발 인프라라는 사례입니다. Anthropic은 다른 조직도 머지않아 같은 압력을 겪을 것으로 봤습니다.

### 4. [OpenCode 2.0 출시 직후, 콘솔 침해로 사용자 API 키 유출](https://startupfortune.com/opencode-breach-exposes-stored-openai-and-anthropic-keys-prompts-urgent-key-rotation/)

오픈소스 코딩 에이전트 OpenCode가 이번 주 2.0을 냈습니다. 서버가 백그라운드 프로세스 하나로 늘 떠 있고 TUI·웹·데스크톱 앱이 모두 여기에 붙으며, API를 처음부터 다시 만들었습니다. MCP 서버와 OpenAPI 엔드포인트를 스크립트에서 부를 수 있는 함수로 바꾸는 code mode가 기본으로 켜지고, 백그라운드 하위 에이전트와 비동기 셸 명령도 들어갔습니다.
그런데 10월 17일 개발사 Anomaly Innovations(옛 SST)가 OpenCode Console 사용자 약 1.4%에게 침해 사실을 알렸습니다. 종료 중이던 레거시 시스템에 무단 접근이 있었고, 외부 제공자를 연결해 둔 일부 계정의 OpenAI·Anthropic·Google API 키가 노출됐을 수 있다는 내용입니다. 회사는 "대규모 distillation 공격"과 관련됐다며 세 회사와 함께 대응 중이라고 했습니다.
OpenCode를 콘솔과 연결해 썼다면 제공자 키를 교체하는 게 안전합니다. 알림 메일이 오기 전에 이미 청구서에 이상한 사용량이 찍혔다는 사용자 제보도 나왔습니다.

관련: [OpenCode 2.0 릴리스 노트](https://anoma.ly/notes/opencode-2-0/) · [OpenCode 공지](https://x.com/opencode/status/2111519637049319818)

### 5. [Meta, 'Muse Spark Open' 공개…Mac Studio 2대로 돌리는 오픈 웨이트 모델](https://research.meta.ai/blog/muse-spark-open)

Meta가 Muse Spark의 가중치를 공개했습니다. 총 816B(활성 42B) 파라미터의 네이티브 멀티모달 MoE 모델이고 컨텍스트는 100만 토큰입니다. Meta는 "현재까지 가장 뛰어난 미국산 오픈 웨이트 모델"이라고 소개했습니다.
눈에 띄는 건 로컬 실행입니다. M5 Ultra Mac Studio는 한 대당 GPU가 최대 512GB 통합 메모리를 쓸 수 있어서, MLX로 두 대를 묶으면 모델 전체가 올라갑니다. Meta는 이 구성에서 Mastodon 클라이언트 Ice Cubes의 iOS 버그 수정과 빌드까지 온디바이스로 돌린 사례를 보여 줬습니다.
라이선스는 상업적 이용 조건이 제한된 Muse Model License입니다. 같은 주에 DeepSeek도 V4.1-Flash-1017 업데이트를 내놓아 오픈 모델 소식이 몰렸습니다.

관련: [Hugging Face 컬렉션](https://huggingface.co/collections/meta-models/muse-spark-open) · [DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

### 6. [Andrej Karpathy: "LLM 역량에 대한 인식 격차가 날카로운 깔때기 모양으로 벌어지고 있다"](https://x.com/karpathy/status/2109361546505966046)

Karpathy가 10월 11일 X에, 4월에 쓴 "서로 딴소리하는 두 집단" 글을 다시 꺼내며 격차가 더 커졌다고 적었습니다. 본인이 대략 추산이라고 밝힌 수치로는 세계 인구의 약 75%(60억 명)가 LLM을 거의 접하지 않았고, 약 20%(10억~20억 명)는 무료 챗봇을 조금 나은 검색이나 글쓰기 보조로 가끔 씁니다. 수학과 코드 분야에서 최첨단 모델을 전문적으로 쓰는 사람은 약 0.2%(2,000만 명)로, 몇 주~몇 달 걸리던 일을 에이전트가 끝내는 걸 직접 보고 있습니다. 내부 최첨단 시스템에 접근하는 사람은 약 5,000명입니다.
격차를 만드는 요인으로는 세 가지를 들었습니다. 맡기는 문제의 규모와 작업 기간, 디지털 환경에서 검증할 수 있고 돈이 되는 분야(수학, 코드)에 역량이 몰리는 강화 학습 방식, 그리고 무료·유료·내부 시스템 사이의 접근 차이입니다. 한 문단짜리 질문으로는 시스템의 역량을 거의 시험할 수 없다는 지적입니다.
최상위 구간에서는 이미 사람의 검토가 산출 속도를 못 따라간다며, AI가 낸 최첨단 수학 원고 722편을 수학자들이 검토하는 데 한참 걸릴 것이라는 예를 들었습니다.

관련: [AI타임스](https://www.aitimes.com/news/articleView.html?idxno=216191) · [GeekNews](https://news.hada.io/topic?id=35202)

### 7. [AI로 복제한 어도비 무료 대안 '아트크래프트' 등장…저작권 논란](https://www.aitimes.com/news/articleView.html?idxno=216149)

한 개발자가 Claude와 Rust로 Photoshop, Lightroom, Illustrator, Premiere Pro를 흉내 낸 오픈소스 제품군 ArtCraft를 공개했습니다. PhotoCraft, LightCraft, ImageCraft, FilmCraft 같은 이름으로, 어도비 사용자가 따로 배우지 않아도 되도록 비슷한 UI를 목표로 합니다. JSON 제어 채널과 MCP 서버를 둬서 AI가 직접 메뉴와 도구를 조작하는 "에이전트 네이티브" 설계도 내세웠습니다.
Adobe Creative Cloud 관련 Reddit 커뮤니티에 올라온 소개 글이 큰 반응을 얻었습니다. 개발자는 한 달 안에 어도비와 기능적으로 100% 같은 수준에 도달하겠다고 했지만, 이는 목표일 뿐입니다.
기대만큼 우려도 큽니다. 인터페이스와 제품군을 통째로 모방한 데 따른 저작권 문제, 실제 기능 완성도, 보안·안정성 검증이 아직 안 됐다는 지적이 나옵니다. AI 코딩으로 기존 소프트웨어를 빠르게 복제할 수 있게 되면서 생긴 새 유형의 논쟁입니다.

### 8. [유럽 슈퍼마켓 냉장 설비 해킹…냉장고를 50℃ 제상 모드로 돌려](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident)

10월 11일 밤부터 프랑스 Intermarché, Leclerc, Coopérative U 매장의 Danfoss 냉장 제어 장치가 공격을 받았습니다. 하루 2시간 정도만 도는 자동 제상 기능을 50℃ 연속 제상으로 바꿔 놓아 냉장고와 냉동고에서 열기가 뿜어져 나왔다고 합니다. Coopérative U 대표는 "전례 없는 일"이라며 조사를 약속했고, 초기 손실은 약 30만 유로로 추정됩니다.
같은 시기 네덜란드에서도 Albert Heijn, Etos, Gall & Gall 웹사이트가 내려가 배송이 멈췄고, 전자 가격표가 오작동해 매장 가격 표시가 흐트러졌습니다. 두 사건이 연결됐는지는 아직 확인되지 않았습니다.
데이터를 노린 공격이 아니라 냉장 설비 설정을 바꿔 신선식품 재고에 직접 피해를 낸 사례입니다.

### 9. [테슬라, '하늘 나는 로드스터' 공개…"전시용일 뿐" 지적도](https://www.aitimes.com/news/articleView.html?idxno=216356)

Tesla가 현지 시간 10월 15일(한국 시간 16일) 텍사스 맥그리거의 SpaceX 시험장에서 신형 Roadster를 공개했습니다. 2017년 첫 공개 후 약 9년 만이고, 생산은 2028년에 시작한다고 밝혔습니다. 시험차가 휘어진 경사로를 거꾸로 달리다 공중에서 회전해 착지하고, 일렬로 세운 Tesla 차량들 위를 뛰어넘는 시연이 X로 생중계됐습니다. 공중 기동 시연 차량에는 사람이 타지 않았습니다.
차체 하부 팬이 공기를 빨아들여 차를 노면에 붙이고, 공중 기동은 SpaceX와 함께 개발한 냉가스 추진기(고압 기체 분사)로 합니다. 사양은 2인승 Performance, 후방 추진기를 단 Thrust, 차체 둘레에 추진기를 둔 1인승 Rocket 세 가지이고, 0→60마일 목표는 각각 1.6초, 0.9초, 0.59초 미만입니다. 예약금은 Performance 5만 달러, Thrust 25만 달러이며 Rocket은 초청 고객만 신청할 수 있습니다.
Tesla는 Rocket 사양이 일반 도로 주행 승인을 받지 않았다고 명시했고, 예약 약관에도 인도 시점이나 인도 여부를 보장하지 않는다고 적었습니다. John Carmack은 안전 문제를 지적했고, 기술 시연과 실제 판매는 별개라는 평가가 이어졌습니다. 반대로 Tesla와 SpaceX 합병 가능성을 보여 주는 행사라는 분석도 나왔습니다.

관련: [Tesla Roadster](https://www.tesla.com/roadster)

### 10. [Linus Torvalds, Claude Code로 커널 읽기 경로 개선…"AI 사용 금지 규칙은 만들지 않겠다"](https://news.hada.io/topic?id=35265)

Linux 7.3-rc7을 앞두고 torvalds/linux.git에 `noref-filemap-read-with-llm` 브랜치가 생겼습니다. 여러 스레드가 같은 파일을 조금씩 읽을 때 folio 참조 카운트 경합이 생기는 문제를, 참조 카운트를 건드리지 않고 페이지 캐시를 읽는 경로로 푸는 패치입니다. Torvalds는 코드, 테스트 프로그램, 검토 항목, 패치 설명 초안을 자신의 지휘 아래 Claude Code로 작성했고 측정은 직접 했다고 밝혔습니다.
4코어 노트북에서 8스레드가 `pread()`로 16바이트씩 읽는 테스트의 경우, 읽기당 커널 CPU 사이클이 약 2,950에서 725로 줄었습니다. 다만 노트북 한 대에서만 측정했고, 7.4 병합 기간에 들어갈지는 정해지지 않았습니다.
같은 주 커널 메일링 리스트에서는 특정 작업에 AI 사용을 막자는 논의에 Torvalds가 반대했습니다. 이해를 증명하려면 컴파일러 없이 어셈블리를 쓰라는 규칙과 다를 바 없다며, 기여자에게 바라는 건 최선을 다하고 자기가 하는 일을 이해하는 것이고 이는 어떤 도구를 쓰는지와 거의 관계가 없다고 했습니다.

관련: [GeekNews: "AI 사용을 금지하지 않겠다"](https://news.hada.io/topic?id=35504)

---

## 🚀 Indie Radar
{: #indie-radar}

### [Guitoro](https://guitoro.com/) · 웹 토이 · Show HN 571점

브라우저에서 키보드나 터치로 치는 가상 기타입니다. 왼손으로 코드를 잡고 오른손으로 스트로크하는 식으로 키를 배치했고, 어쿠스틱·클래식·일렉트릭·베이스 4종의 소리는 모두 실제 악기를 녹음했습니다. 51곡을 20%까지 느리게 틀면 줄과 운지가 화면에 표시되고, 연주자가 코드를 바꿀 때까지 곡이 기다려 줍니다. 설치나 가입 없이 바로 열립니다.

### [PS2 Web Recomp](https://github.com/snuri00/ps2-web-recomp) · 오픈소스 정적 리컴파일러 · Show HN 314점

PS2 게임의 Emotion Engine 기계어를 미리 C++로 번역해 WebAssembly로 컴파일하고, 나머지 하드웨어는 WebGPU 런타임으로 에뮬레이션합니다. 첫 타이틀인 Gran Turismo 4는 노트북 내장 GPU의 Chrome에서 원본의 2배 해상도로 50fps(PAL)를 내고, God of War II도 게임별 코드 없이 같은 스크립트로 돌아갑니다. 게임 데이터는 포함하지 않으며 직접 가진 디스크 이미지로 로컬에서 웹 페이지를 만듭니다.

### [Unfenced](https://unfenced.land/) · 데이터 웹 서비스 · Show HN 313점

국유림, 사냥 허가지, 야생 보호구역 같은 공공 토지와 경계가 맞닿은 매물 토지만 모아 보여 주는 서비스입니다. 49개 지역의 매물 69만여 건을 USGS PAD-US 경계 데이터와 필지 경계로 대조해 1만 3천여 건을 추렸고, 매물마다 공공 토지와 맞닿은 경계 길이를 표시합니다. 매물 설명 문구가 아니라 공식 경계 지도로 확인한다는 점을 내세웁니다.

### [Simple Analytics](https://trustmrr.com/startup/simple-analytics) · 프라이버시 웹 분석 SaaS · MRR $38.2k (TrustMRR 인증)

2018년 네덜란드에서 시작한, 방문자를 식별하지 않는 웹 분석 도구입니다. TrustMRR 기준 MRR $38.2k, 최근 30일 매출 $47.6k, 누적 매출 약 $191만이고 활성 구독은 1,255개입니다. 방문자가 쿠키 동의를 거부해도 개인 식별 없이 트래픽을 셀 수 있다는 점을 내세우며, GA4와 함께 쓰는 에이전시·기업 고객을 노립니다. 8년째 운영 중인 서비스가 여전히 30일 성장률 31.6%를 기록하고 있습니다.

### [REA](https://github.com/morluto/rea) · 오픈소스 리버스 엔지니어링 MCP · GitHub 주간 ★24.9만

코딩 에이전트에 네이티브 바이너리, JavaScript·Electron 앱, .NET 어셈블리, 웹사이트를 분석하는 도구를 붙여 주는 MCP입니다. 다른 앱에서 본 기능이 어떻게 동작하는지 소스 없이 조사하고 근거와 한계를 함께 정리해 준다는 콘셉트이며, 분석은 로컬에서 돌고 Ghidra·Hopper·IDA를 엔진으로 쓸 수 있습니다. 일주일 만에 스타 20만 개를 넘기며 이번 주 GitHub Trending 1위였습니다.

### [The No Jumpscare Show](https://polypaw.itch.io/the-no-jumpscare-show) · 인디 게임 · itch.io 신작 인기 1위

"점프스케어가 하나도 없다"고 약속하는 코미디 단편 호러 게임입니다. 무서워하지 않으면 1만 달러를 준다는 수상한 귀신의 집에 주인공이 들어가는 이야기로, 이번 공개분은 첫 파트이며 플레이 시간은 30~40분입니다. 9월에 나온 Windows·Linux용 무료(원하는 만큼 지불) 게임으로, 평점 4.8을 받고 있습니다.

---

## 🛠️ 엔지니어링 사례 & 강좌
{: #observability}

### [Kubernetes 노드 메모리 압박: 첫 파드 축출 7분 전에 잡아내기](https://www.elastic.co/observability-labs/blog/kubernetes-node-pressure-anomaly-detection)

kubelet은 노드의 가용 메모리가 축출 임계값 아래로 내려가면 `MemoryPressure`를 켜고 파드를 축출합니다. 그런데 축출 순서는 request 초과 여부, 우선순위, 초과량으로 정해져서, 메모리를 늘린 파드가 아니라 request 없는 작은 NGINX 파드가 쫓겨나 서비스가 내려갔습니다.
글은 이상 탐지, 여유 경고, `MemoryPressure` 경보를 함께 두는데 실습에서 셋 다 한계가 드러났습니다. 이상 탐지는 메모리가 한 번에 빠지면 울리지 않았고, 여유 경고는 여유 폭(0.5GiB)보다 큰 하락에 `MemoryPressure`보다 늦게 울렸습니다. 실제로 대응할 시간을 벌어 준 건 임계값을 넘어도 5분 기다렸다 축출하는 soft 축출 유예였습니다.
그래서 세 경보를 모두 켜 두고, 유예 시간은 팀의 대응 시간에 맞추고, 여유 폭은 한 평가 주기 동안 빠질 수 있는 메모리보다 넉넉히 잡으라는 게 결론입니다. 실습은 Elastic ML을 쓰지만 이 구성은 Prometheus 기반 환경에도 그대로 옮길 수 있습니다.

<details>
<summary>그림으로 한눈에 보기</summary>
<p><img src="/img/2026_10_17/node_pressure_timeline.svg" alt="노드 메모리 압박 타임라인"></p>
<p><img src="/img/2026_10_17/node_pressure_summary.svg" alt="노드 메모리 압박 대응의 핵심"></p>
</details>

### [Datadog은 수천 개 내부 서비스의 중요도를 어떻게 정하는가](https://www.datadoghq.com/blog/how-datadog-defines-service-criticality-at-scale/)

Datadog은 모든 서비스에 같은 SLO와 배포 절차를 적용하다 보니, 데이터센터가 늘수록 배포가 느려지고 신뢰성 투자가 고르게 흩어지는 문제를 겪었습니다. 그래서 고객 영향 기준의 서비스 중요도를 자동으로 분류하는 시스템을 만들었습니다.
첫 신호는 포스트모템입니다. LLM으로 SEV-1·SEV-2 포스트모템 수백 건에서 원인 서비스와 영향받은 서비스를 뽑았는데, 하루가 안 걸렸고 비용은 약 32달러였습니다. 여기에 에러 트레이스 경로, 트래픽(거의 0이면 중요도를 낮추기만 함), 온콜로 페이징하는 모니터 유무를 더해 중요도와 신뢰도 점수를 냅니다. 신호끼리 어긋나면 등급은 그대로 두고 신뢰도만 낮춥니다.
중요 서비스를 안전하다고 잘못 보는 쪽이 더 비싸기 때문에 일부러 false positive를 허용하도록 맞췄고, 서비스 오너가 사유를 적어 등급을 덮어쓸 수 있습니다. 결과는 배포 속도 차등, 의존성 업데이트 자동 머지 여부 판단에 쓰입니다. 알람 정책이나 SLO를 서비스별로 차등화하려는 팀이 참고할 만한 설계입니다.

<details>
<summary>그림으로 한눈에 보기</summary>
<p><img src="/img/2026_10_17/datadog_criticality.svg" alt="Datadog 서비스 중요도 시스템"></p>
</details>

### [Claude Code 팀은 에이전트가 쏟아내는 코드를 어떻게 리뷰하는가](https://claude.dev/blog/solving-code-review-at-anthropic/)

Claude Code 코드의 약 90%를 Claude가 쓰다 보니, 6월부터 9월 사이 머지된 PR이 두 배 넘게 늘었습니다. 팀은 사람이 모든 diff를 읽는 대신 "PR당 사람의 시간을 최소로 쓰되 revert와 장애는 늘지 않게"를 목표로 잡았습니다. 그 결과 같은 기간 revert 비율은 40% 넘게 줄었습니다.
방법은 관문 하나가 아니라 여러 겹의 검사입니다. 작성자 쪽에서 Claude가 테스트·빌드 결과를 직접 보여 주고, PR마다 AI 리뷰와 보안 리뷰가 돌며 모든 지적에 답해야 머지됩니다. 사람 승인 수는 변경의 위험도로 정합니다. 문서처럼 위험이 낮으면 0명, 일반 변경과 캐시·자동 업데이트 같은 민감 영역은 1명, 가장 위험한 코드와 지정 경로는 2명이고, 위험도는 작성자가 아니라 분류기가 변경 내용을 보고 정합니다. 마지막은 플래그, 단계 배포, 빠른 롤백입니다.
리뷰어를 개선하는 방식도 참고할 만합니다. 과거 장애를 일으킨 PR을 평가 셋으로 만들어 매일 돌리고, 작성자가 지적을 고쳤는지 무시했는지로 노이즈를 잽니다. 에이전트끼리 리뷰와 수정을 50번 넘게 주고받은 PR도 있어서, 세 번째 라운드부터는 접근을 다시 생각하라고 요청하도록 바꿨습니다. 사람은 만들지 말지, 위험한 코드, 아키텍처, 검증 결과 판단, 결과 책임을 맡습니다.

관련: [GeekNews](https://news.hada.io/topic?id=35495)

<details>
<summary>그림으로 한눈에 보기</summary>
<p><img src="/img/2026_10_17/claude_code_review_flow.svg" alt="Claude Code 팀의 코드 리뷰 단계"></p>
</details>

### [게임이 곧 하네스다: 게임 개발에 코딩 에이전트를 제대로 쓰는 설계](https://kylekukshtel.com/ai-harness-engineering-game-development-claude-code)

15년 차 게임 프로그래머인 글쓴이는 Claude Code로 웹 앱은 못 만드는 게 없다고 느낄 정도인데, 게임 개발에서는 에이전트가 번번이 막혔다고 합니다. 원인을 모델의 한계가 아니라 컨텍스트 문제로 봅니다. 게임에는 에셋, 상태, 시각 결과처럼 코드 밖에 있는 요소가 많아서, 코드만 보는 에이전트는 그 블랙박스를 열지 못한다는 것입니다.
해법은 게임을 에이전트가 읽고 조작하고 검증할 수 있게 짓는 것입니다. 시드가 있는 단일 난수원으로 상태를 결정론적으로 재현하고, 저장·불러오기를 처음부터 설계합니다. 모든 객체를 하나의 Thing 타입으로 표현해 직렬화를 단순하게 하고, 상태 변경은 명령 패턴으로 기록해 버그 상황을 재생합니다. 수치 데이터는 코드 밖으로 빼서 재컴파일 없이 바꾸고, 화면 변화는 odiff 같은 도구로 "85% 유사"처럼 숫자로 비교하게 합니다.
이렇게 하면 게임 자체가 하네스가 되어 수정, 실행, 검증 주기가 몇 초 안에 돕니다. 대부분은 AI가 없어도 좋은 게임 설계이고, 에이전트와 결합하면 효과가 커진다는 게 글쓴이의 주장입니다. 다만 작은 게임에는 이런 설계까지는 필요 없을 수 있다고 덧붙였습니다.

관련: [GeekNews](https://news.hada.io/topic?id=35355)

<details>
<summary>그림으로 한눈에 보기</summary>
<p><img src="/img/2026_10_17/game_harness.svg" alt="게임이 곧 하네스"></p>
</details>

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [남편의 아름다움](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=353241663) · 앤 카슨 · 한겨레출판 (주간 5위)
  - [나는 살아야겠다](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401487844) · 전은옥 · 삶창 (주간 11위)
  - [레드 닥>](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=222539055) · 앤 카슨 · 한겨레출판 (주간 19위)
- 주목할 신간
  - [2026 김승옥문학상 수상작품집](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404305083) · 송지현, 박서련, 서유미, 안보윤 외 · 문학동네
  - [레시타티프](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404308546) · 토니 모리슨 · 문학동네

### IT

- 베스트 새 진입
  - [AI 작곡 with SUNO](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=396054430) · 제이린 · 삼호ETM (주간 6위)
  - [하네스 엔지니어링 with 클로드 코드](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=393763673) · 황민호 · 한빛미디어 (주간 16위)
  - [AI 쓰는 어른의 IT 상식](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402489426) · 스펜서 · 한빛미디어 (주간 19위)
- 주목할 신간
  - [작고 쓸모 있는 코딩 딴짓](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403862833) · 권경열 · 한빛미디어 · 코덱스와 시작하는 10분 바이브 코딩 프로젝트 29
  - [내가 다시 AI를 처음 공부한다면](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404532409) · 권구민 · 프리렉 · 수식 번역에서 논문 재현, 취업까지 AI 엔지니어 학습 로드맵

### 인문

- 베스트 새 진입
  - [잘난 여자들을 위한 ADHD](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401919691) · 트레이시 오츠카 · 심심 (주간 8위)
  - [두려움 없는 삶에 대하여](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=403492396) · 에픽테토스 · 현대지성 (주간 13위, 스토아 철학 전집 국내 최초 단권 완역본)
- 주목할 신간
  - [진화심리학 (제7판)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404242311) · 데이비드 M. 버스 · 웅진지식하우스 · 마음과 행동을 탐구하는 새로운 과학
  - [베짱이](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404302832) · 버나드 슈츠 · 연암서가 · 게임, 삶, 유토피아

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
