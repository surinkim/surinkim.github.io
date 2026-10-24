---
layout: post
title: "주간 테크/개발 뉴스 #2026 10/18 ~ 10/24"
date: 2026-10-24
categories: [normal]
tags: [weekly, dev-news, indie-radar, observability, books]
---

## 이번 주 pick

![Nick Dobos 트윗: 지난 한 달 동안 역사상 치명적 보안 버그의 3%가 발견됐다](/img/2026_10_24/critical-bugs-3-percent.jpg)

"기록된 역사 전체에서 '치명적' 소프트웨어 보안 버그의 3%가 지난 한 달 사이에 발견됐다. 이 속도면 올해에만 약 10만 개가 더 나와, 역대 취약점 총수에 26%쯤을 더하게 된다." — Nick Dobos(@NickADobos), 2026년 10월 23일. 인용된 그래프는 월별 CVE 공개 건수를 보여 주는 CVE Tracker입니다.

<small>출처: [r/singularity](https://www.reddit.com/r/singularity/comments/1xdh8vq/cybersecurity_is_currently_experiencing_a/)</small>

---

**바로가기**

- [📰 테크 뉴스 (10)](#tech-news) — PHP 인증 없는 RCE 2건, 개인 키가 256보다 작았던 eMudhra 인증서, 먼저 일을 챙기는 Claude Duet
- [🚀 Indie Radar (5)](#indie-radar) — 인허가에 막히는 시장 시뮬레이션 Permit Pending, AI가 쓴 코드를 이해했는지 묻는 Git 훅 Sphinx
- [🛠️ 엔지니어링 사례 & 강좌 (2)](#observability) — GPU 파드가 Pending에 머무는 이유, 지우지 않고 컨텍스트 창 밖으로 옮기는 에이전트
- [📚 도서](#books) — 소설 · IT · 인문 베스트 새 진입과 신간

---

## 📰 테크 뉴스
{: #tech-news}

### 1. [PHP, 인증 없는 원격 코드 실행 취약점 2건 수정…"지금 바로 업데이트"](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

10월 21일 PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35가 나왔습니다. CVE-2026-109618은 요청이 `memory_limit`에 걸리는 순간 덜 초기화된 내부 데이터가 남아 메모리가 오염되는 문제이고, CVE-2026-109619는 이전 요청의 해제된 메모리를 같은 워커의 다음 요청이 쓰는 use-after-free입니다. Apache `mod_php`에서는 애플리케이션 코드가 돌기도 전에 인증 없는 요청으로 기본 설정에서 RCE가 시연됐고, PHP-FPM, php-cgi, FrankenPHP, LiteSpeed도 영향 대상입니다. 메모리 제한 조정 같은 완화책으로는 막을 수 없어 업데이트만이 해결책입니다.
PHP Foundation은 OOM 문제의 첫 징후를 2024년 외부 감사 때 이미 찾았지만, 수정안마다 호환성·성능 부담이 있어 합의제로 결정을 미루다 몇 달을 흘려보냈다며 "구조적 실패"라고 인정했습니다. 올해 8월 Calif 연구자와 OpenAI가 같은 근본 원인을 각각 보고했고, Wiz도 다른 공격 경로를 보고했습니다. 공개 직전 한 HN 사용자가 엠바고를 모른 채 업데이트를 미리 알리는 글을 올려 일정이 흔들리기도 했습니다.

관련: [php.net 보안 공지](https://www.php.net/archive/2026.php#2026-10-21-5) · [GeekNews 요약](https://news.hada.io/topic?id=35759) · [Tell HN: 엠바고를 깨서 죄송합니다](https://news.ycombinator.com/item?id=50193416)

### 2. [eMudhra 중간 인증서 8개, 개인 키가 256보다 작은 정수였다](https://emudhra.we-have-a-problem.com/)

10월 17일 한 연구자가 CCADB의 인증서를 검사하다 인도 인증기관 eMudhra의 중간 인증서 8개가 모두 256 미만의 정수를 개인 키로 쓰고 있다는 사실을 발견했습니다. 사실상 즉시 복구할 수 있는 키라 Mozilla도 제보자의 방법을 모른 채 독립적으로 키를 복구했습니다. eMudhra는 데이터 주권 요구에 맞추려 HSM 키를 내보내는 테스트를 하다 코드 결함으로 약한 키 쌍이 생겼고, 비슷한 라벨 때문에 그 키로 인증서 서명 요청을 만들었다고 설명했습니다.
Mozilla와 Chrome은 중간 인증서 차단에 이어 emSign ECC Root CA - G3 루트의 신뢰를 긴급 제거하기로 했고, 이전해야 할 인증서는 초기 추산으로 약 3만 개입니다. eMudhra는 결국 글로벌 SSL/TLS 인증서 사업 철수를 발표했지만, Mozilla 조사에는 기한을 넘기고도 답하지 않았습니다.
시스템 루트 저장소가 바로 갱신되지 않는 환경을 위해 언어 런타임도 움직였습니다. Go는 긴급(URGENT) 트랙으로 1.27.3·1.26.10 보안 릴리스를 내, `crypto/x509`의 `Verify`가 문제의 중간 인증서가 들어간 체인을 걸러 내도록 했습니다(CVE-2026-111943). Node.js, Python, Deno, Bun도 패치 버전을 냈고, 버전별 목록은 제목 링크의 사이트에 정리돼 있습니다.

관련: [Scott Helme: Eight Bits of Trust](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/) · [eMudhra 사업 철수 발표](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) · [GeekNews 요약](https://news.hada.io/topic?id=35880) · [Go 취약점 GO-2026-6809](https://pkg.go.dev/vuln/GO-2026-6809)

### 3. [앤트로픽, 메타 '뮤즈' 대항마 AI 에이전트 '클로드 듀엣' 공개](https://www.aitimes.com/news/articleView.html?idxno=216510)

Anthropic이 10월 21일 업무용 에이전트 Claude Duet의 연구용 미리보기를 공개했습니다. 미국 Pro·Max 구독자에게 대기자 명단 순으로 열리며, Claude Opus 5.5 기반으로 기존 메모리·스킬·앱 연결을 그대로 씁니다. 매일 아침 연결된 앱에서 중요한 일을 추려 브리핑하고, 몇 시간 간격으로 계정을 확인해 주의가 필요한 일을 먼저 알려 줍니다. 상시 감시는 사용량 한도를 빨리 소진해 확인 주기를 몇 시간으로 잡았다고 합니다.
작업은 원격 가상 머신의 브라우저에서 돌아 노트북을 닫아도 이어집니다. 메시지 전송, 결제, 서명, 삭제 같은 작업 전에는 사용자 승인을 받고, 증권 거래와 계좌 이체는 승인과 관계없이 막혀 있습니다. Meta의 Muse, OpenAI의 Dots와 함께 "먼저 일을 찾아 주는 에이전트" 경쟁이 본격화하는 모습입니다.

### 4. [구글, AI 성능 스스로 높이는 자기개선 프레임워크 '하네스²' 공개](https://www.aitimes.com/news/articleView.html?idxno=216410)

Google이 모델을 다시 학습하지 않고 에이전트를 둘러싼 하네스만 고쳐 성능을 올리는 오픈소스 프레임워크 Harness²를 공개했습니다. 여기서 하네스는 시스템 프롬프트, 가이드라인, 메모리, 도구 사용 지침, 하위 에이전트, 스킬, 스크립트, 플러그인 등 파일로 마운트되는 8가지 구성 요소를 말합니다.
정답을 알려 주는 검증기가 없는 작업에서도 쓸 수 있게, 공통 문제를 겨냥한 수정안과 분야 지식을 겨냥한 수정안 두 개를 같은 작업에 적용해 실행 결과를 비교하고 나은 쪽을 고릅니다. 얻은 교훈은 LESSONS 라이브러리에 쌓되, 새 작업은 기본 하네스에서 다시 시작해 특정 작업에 맞춘 수정이 번지는 것을 막습니다. GLM-5를 OpenCode와 함께 쓴 구성은 WorkBuddy-Bench 점수가 64.2에서 75.7로 올랐습니다.

### 5. [Kimi K3.1 Pro 공개: 3T급 오픈 웨이트, Terminal-Bench에서 Opus 5.5에 근접](https://www.kimi.ai/blog/kimi-k3-1-pro)

Moonshot AI가 K3에 사후 학습을 크게 늘린 3조 파라미터급 Kimi K3.1 Pro를 내놨습니다. 컨텍스트는 100만 토큰이고, Terminal-Bench 4.0에서 65.7%로 Claude Opus 5.5(66.4%)에 근접했습니다. 2~3배 빠른 Highspeed 버전도 함께 나왔고, 전체 가중치는 11월 4일까지 공개할 예정입니다. Artificial Analysis 지수에서는 Opus 5.5, Sonnet 5.5, Muse Wonder Full에 이어 4위에 올라 오픈 웨이트 1위가 됐습니다.
가중치 공개를 앞두고 중간 학습과 강화학습 단계에서 사이버 보안 관련 데이터를 뺀 점도 눈에 띕니다. 공격 역량은 통제하지 않은 모델보다 낮아졌지만, 일반 코딩·디버깅 실력이 늘면서 K3보다는 높아졌다고 밝혔습니다.

관련: [GeekNews 요약](https://news.hada.io/topic?id=35879) · [AI타임스: AAII 전체 4위](https://www.aitimes.com/news/articleView.html?idxno=216603)

### 6. [DeepSeek, 자사 서비스를 돌리는 추론 프레임워크 DeepInfer 오픈소스 공개](https://github.com/deepseek-ai/DeepInfer)

DeepSeek이 대규모 프로덕션 서비스를 실제로 돌리는 추론 프레임워크 DeepInfer를 공개했습니다. 이번 공개판은 오프라인 추론용으로 DeepSeek-V4.1-Flash를 지원하며, FlashMLA·DeepGEMM·DeepEP 등 자체 커널, Attention DP와 MoE expert parallel, 드래프트 토큰으로 디코딩을 앞당기는 추측 디코딩, CPU 스케줄링과 디바이스 실행을 겹치는 비동기 스케줄러를 담았습니다. 배치 구성과 상관없이 같은 결과를 내는 batch-invariant 추론과 결정적 샘플링도 들어 있습니다.
NVIDIA와 함께 Huawei Ascend용 의존성 파일도 들어 있습니다. 이번 주 HN에서 2,345점으로 가장 높은 점수를 받았습니다.

### 7. [Calif, iPhone 18 Pro 원클릭 해킹과 재부팅 후에도 남는 탈옥 시연](https://blog.calif.io/p/iphone)

보안 회사 Calif가 10월 16일 파리 Hexacon에서 iOS 27.0.1이 도는 iPhone 18 Pro를 공격하는 영상 4개를 공개했습니다. Signal과 iMessage로 받은 PDF를 한 번 여는 것만으로 공격이 시작되고, 이어 SSH로 루트 셸(uid=0)에 접속해 패키지를 설치하는 장면과 재부팅 후 첫 잠금 해제 전에도 변조가 유지되는 장면을 보여 줬습니다.
취약점과 공격 연결 구조는 아직 밝히지 않았고, 때가 되면 모두 공개하겠다고만 했습니다. 이번 주 PHP 취약점을 보고한 곳도 Calif입니다.

관련: [GeekNews 요약](https://news.hada.io/topic?id=35877)

### 8. ['제미나이 4 아르곤', 역할 나눠 27시간 만에 마인크래프트 클리어](https://www.aitimes.com/news/articleView.html?idxno=216379)

Google DeepMind가 Gemini 4 Argon 기반 에이전트 4개가 사람 개입 없이 협력해 마인크래프트 최종 보스 엔더 드래곤을 쓰러뜨린 실험을 10월 15일 arXiv에 공개했습니다. 무작위 세계의 서바이벌 모드에서 시작해 27시간 14분이 걸렸고, 그동안 프로그램 2,783개를 작성·실행했으며 캐릭터는 605번 죽었습니다. 연구진은 목표와 기본 도구 사용법만 주고 역할이나 공략 순서는 정해 주지 않았습니다.
에이전트들은 시작 10분쯤 뒤 채팅으로 식량 수집, 다이아몬드 채굴, 도구 제작, 차원문 건설을 나눠 맡았고, Mineflayer 라이브러리로 게임 상태를 읽어 이동·채굴 프로그램을 직접 짜고 오류를 고쳐 가며 진행했습니다. 한 에이전트가 필요한 아이템 12개를 든 채 익사하자 동료가 사라지기 전에 회수했고, 하지 않은 작업을 끝냈다고 보고하면 다른 에이전트가 모순을 지적하기도 했습니다. 최종 전투에만 약 14시간이 걸렸고, API 비용은 출시 할인 요금 기준 약 520달러로 추산됐습니다.
다만 사람과 같은 조건은 아닙니다. Mineflayer가 벽 뒤 블록과 드래곤 상태까지 알려 주고 길찾기도 지원했으며, 난도는 '쉬움'이었고 프로그램의 22%는 오류로 끝났습니다. 한 번의 실험이라 반복해서 성공할지도 확인되지 않았습니다.

### 9. [Google, Gmail·Photos 데이터를 맞춤 광고에 쓸 수 있도록 개인정보처리방침 변경](https://news.hada.io/topic?id=35889)

Google이 10월 16일 개인정보처리방침에 "Gmail, Drive, Photos 데이터는 맞춤 광고에 쓰지 않는다"는 약속의 예외를 추가했습니다. 사용자가 Personal Intelligence로 이 앱들을 AI Mode 같은 검색 도구에 연결했다면, 그 콘텐츠를 바탕으로 한 광고가 표시될 수 있습니다. Android Authority가 변경을 처음 찾아냈습니다.
광고주가 메일·사진 내용이나 이름, 이메일 주소에 접근할 수는 없고, 인종·성적 지향·종교·건강 같은 민감 범주 광고는 하지 않는다고 밝혔습니다. 원하지 않으면 검색 개인화 설정에서 앱 연결을 끊거나 Personalized Recommendations를 끄면 됩니다.

관련: [Techmeme](https://www.techmeme.com/261023/p28#a261023p28)

### 10. [앤트로픽, '숨은 의도 읽는' 새 모델 준비...구글·오픈AI도 후속작 예고](https://www.aitimes.com/news/articleView.html?idxno=216424)

The Information은 10월 19일 Anthropic, Google, OpenAI가 일제히 새 모델 출시를 준비하고 있다고 보도했습니다. 지난 한 달 동안 세 회사가 12개 넘는 모델을 낸 데 이어 또 한 차례 경쟁이 붙는 셈입니다. Anthropic의 미공개 모델을 써 본 관계자는 사용자가 목표를 분명히 설명하지 않아도 실제로 원하는 것을 파악하는 능력이 뛰어나다고 전했습니다. 버그 하나를 고쳐 달라고 하면 근본 원인이 되는 문제 유형을 찾아 관련 문제를 모두 고칠지 되묻는 식입니다. 이 모델이 Fable과 Opus 중 어느 제품군에 속할지는 알려지지 않았습니다.
Google은 Gemini 4 Argon의 후속인 코드명 Gemini 4 Carbon을 개발 중이고, OpenAI는 몇 주 안에 중간급 제품군 Terra의 새 버전을 GPT-6.1 Sol보다 싼 가격에 낼 것으로 전망됐습니다. OpenAI는 이와 별도로 반복 연산으로 추론 깊이를 늘리는 루프 트랜스포머 계열 구조를 일부 적용한 차세대 모델 Bel도 개발하고 있지만, 안전성 준비 때문에 출시까지는 시간이 더 걸릴 수 있다고 합니다.

---

## 🚀 Indie Radar
{: #indie-radar}

### [Permit Pending](https://permit.petercai.com/) · 웹 게임 · Show HN 936점

"인허가가 있는 SimCity"입니다. 플레이어는 신이 아니라 선출된 시장이라, 아파트 한 동이나 버스 전용 차로도 공청회, 주민 반대, 소송, 항소를 거쳐야 합니다. 소개 페이지의 예시처럼 12층으로 계획한 아파트가 주차 문제로 6층이 되고, 사업성이 떨어져 세금 감면을 요구받다가, 4년 뒤 선거에서 양쪽 모두에게 비난받는 식입니다.
무료로 브라우저에서 바로 할 수 있고, HN 댓글 423개가 붙을 만큼 도시 정책 이야기가 오갔습니다. 미리 써 둔 사건 텍스트가 실제 도시 상황과 안 맞는다는 지적에 개발자가 직접 답을 달았습니다.

### [Sphinx](https://sphinx-six-theta.vercel.app/) · 오픈소스 Git 훅 · Show HN 253점

에이전트가 쓴 코드를 푸시하기 전에, 그 코드가 실패 상황에서 어떻게 동작하는지 질문을 던지는 Git 훅입니다. 대화 맥락을 모르는 리뷰어 모델이 diff만 보고 문제를 내고, 틀리면 이유를 설명한 뒤 다른 시나리오로 다시 묻고, 맞히면 푸시가 진행됩니다.
"생각은 외주를 줄 수 있어도 이해는 외주를 줄 수 없다"는 문구를 내걸었습니다. Codex, Claude Code 등 기존 코딩 에이전트나 OpenRouter, OpenAI 호환 엔드포인트로 돌릴 수 있고 무료입니다. 같은 주 HN의 "이해 못 한 AI 코드를 어떻게 배포하나" 질문 글에도 댓글이 751개 달렸습니다.

### [traxy.ai](https://trustmrr.com/startup/traxy-ai) · B2B 리드 발굴 SaaS · MRR $53.2k (TrustMRR 인증)

소셜 미디어에서 이미 해당 시장에 관심을 보이는 잠재 고객을 찾아 리드 목록으로 만들어 주는 서비스입니다. 2026년 1월에 시작해 외부 투자 없이 2~5명이 운영하며, Stripe로 인증된 MRR은 $53,157, 최근 30일 매출은 $58,701, 누적 매출은 $146,900입니다.
활성 구독은 238개이고 Pro 요금제는 월 $149입니다. 30일 성장률은 48%로, 출시 10개월 만에 이 규모에 오른 B2B 사례입니다.

### [부모님 TV 광고, AI 에이전트로 없앴더니](https://www.reddit.com/r/SideProject/comments/1xbp1be/my_parents_tv_showed_an_ad_before_netflix_so_i/) · r/SideProject 주간 7위

부모님의 Xiaomi TV가 Netflix를 열기도 전에 전체 화면 광고를 띄우자, 작성자는 Claude Code에 모델 번호만 알려 줬습니다. 에이전트가 같은 Wi-Fi에서 TV를 찾아 광고·추적 앱 25개를 껐다는 글이고, 작성자는 공개한 저장소가 나흘 만에 GitHub 스타 1만 6천 개를 받았다고 밝혔습니다.
글이 퍼진 뒤 GitHub에는 "Claude Code 프롬프트 하나로 루팅 없이 Android TV 광고 제거" 같은 비슷한 저장소가 여럿 새로 올라왔습니다. 코딩 에이전트를 집 안 기기 관리에 쓰는 흐름을 보여 줍니다.

### [VoiceStudio](https://github.com/debpalash/VoiceStudio) · 오픈소스 음성 도구 · GitHub 주간 ★1.25만

ElevenLabs를 로컬에서 대신하겠다는 오픈소스 음성 스튜디오입니다. 음성 복제, 음성 디자인, 영상 더빙, 받아쓰기, 전사, 오디오북 제작을 한곳에 모았고 646개 언어를 내세웁니다.
4월에 공개된 저장소인데 이번 주에만 스타 12,526개가 늘어 누적 8만 개를 넘었습니다. 모든 기능이 로컬에서 돌아간다는 점을 내세웁니다.

---

## 🛠️ 엔지니어링 사례 & 강좌
{: #observability}

### [How AI workloads are reshaping Kubernetes autoscaling](https://www.cncf.io/blog/2026/10/19/how-ai-workloads-are-reshaping-kubernetes-autoscaling/) (AI 워크로드가 바꾸고 있는 쿠버네티스 오토스케일링)

쿠버네티스는 두 제어 루프의 분업으로 돌아갑니다. 스케줄러는 이미 있는 노드에 파드를 놓고, 오토스케일러는 파드를 놓을 자리가 없으면 노드를 추가합니다. 컴퓨팅 자원이 서로 바꿔 써도 되던 시절에는 두 루프가 서로를 몰라도 괜찮았지만, GPU 같은 가속기에서는 오토스케일러가 추가한 노드를 스케줄러가 쓰지 않아 파드가 Pending에 머무는 일이 생깁니다. 용량이 없는 게 아니라 두 루프가 "쓸 수 있는 노드"를 다르게 판단하는 것입니다.
글은 가속기가 가져온 문제를 차례로 짚습니다. 미리 예약한 용량을 써야 하는 문제, GPU 개수가 아니라 NIC·NUMA까지 포함한 배치(토폴로지)가 중요해진 문제, GPU 하나를 쪼개 나눠 쓰는 문제입니다. DRA(Dynamic Resource Allocation)는 개수 대신 구조화된 요청으로 이런 조건을 표현하게 해 두 루프에 공통 어휘를 줬지만, 오토스케일러 쪽 지원은 구현마다 다릅니다.
공통 어휘로 풀리지 않는 것이 gang 스케줄링(파드 전체를 함께 놓거나 아예 놓지 않기)입니다. 스케줄러는 Workload·PodGroup API(beta, 기본 꺼짐)로 그룹 단위를 배우는 중이지만 오토스케일러는 여전히 파드 단위로 판단해, 일부 파드 몫의 노드만 늘리고 작업은 시작도 못 하는 낭비가 생깁니다. 지금은 Kueue와 ProvisioningRequest로 그룹 용량을 한 번에 요청하는 식으로 우회하고, SIG-Autoscaling에서는 두 루프를 직접 잇는 API를 제안하고 있습니다. GPU 파드가 Pending이면 용량 부족부터 의심하지 말고 두 루프가 같은 노드 모양을 보고 있는지 확인하라는 것이 실무 교훈입니다.

<details>
<summary>그림으로 한눈에 보기</summary>
<p><img src="/img/2026_10_24/k8s_two_loops.svg" alt="스케줄러와 오토스케일러, 두 루프의 어긋남"></p>
</details>

### [Context Engineering with Deep Agents: How To Remember Without Keeping Everything In Context](https://www.langchain.com/blog/context-engineering-deep-agents-remember) (Deep Agents의 컨텍스트 엔지니어링: 모든 걸 컨텍스트에 두지 않고 기억하는 법)

오래 도는 에이전트는 지시문, 도구 결과, 파일이 쌓일수록 정확도가 떨어집니다(context rot). LangChain의 오픈소스 하네스 Deep Agents가 이를 막는 다섯 가지 방법을 매주 경쟁사 5곳을 조사해 보고서를 쓰는 에이전트 예시로 설명합니다. 핵심은 내용을 지우지 않고 컨텍스트 밖(파일, 요약, 별도 에이전트)으로 옮긴다는 것입니다.
약 2만 토큰이 넘는 도구 결과는 파일로 빼고 앞뒤 몇 줄만 보여 주며(사용자 메시지는 5만 토큰 기준), 사용량이 컨텍스트 창의 85%에 이르면 오래된 메시지를 요약하되 원문은 파일에 남겨 다시 읽을 수 있게 합니다. 스킬은 이름과 설명만 시스템 프롬프트에 두고 필요할 때 본문을 읽고, 시끄러운 조사는 하위 에이전트가 자기 컨텍스트에서 처리해 결과 세 줄만 돌려줍니다. 장기 메모리는 마크다운 파일이라 모델이나 제공사를 바꿔도 그대로 이어집니다.
각 기법이 에이전트 루프의 어느 지점(모델 호출 전, 도구 호출 후 등)에 끼는 미들웨어인지까지 보여 줘서, 다른 하네스를 쓰거나 직접 만들 때도 같은 구조로 옮길 수 있습니다. "잘라 내지 말고 빼 두기, 요약은 되돌릴 수 있게, 메모리는 내가 가진 저장소에"라는 정리가 핵심입니다.

<details>
<summary>그림으로 한눈에 보기</summary>
<p><img src="/img/2026_10_24/agent_context_engineering.svg" alt="에이전트 컨텍스트를 창 밖으로 옮기는 다섯 가지 방법"></p>
</details>

---

## 📚 도서
{: #books}

### 소설

- 베스트 새 진입
  - [항밈학과 같은 건 없습니다](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404810733) · QNTM 지음, XCninety 옮김 · 황금가지 (주간 16위)
  - [세종의 나라 1 (양장)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=386006778) · 김진명 · 이타북스 (주간 18위)
- 주목할 신간
  - [산책과 사후세계에 대한 도서전](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404922129) · 차한비 · 타이피스트
  - [누명](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404846452) · 정진영 · 무블 · '희대의 간신' 유자광의 진짜 이야기

### IT

- 베스트 새 진입
  - [야생 학습](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404995378) · 김창준 · 인사이트 (주간 2위) · 불확실성의 시대, 학습은 왜 더 중요해졌는가
  - [일 잘하는 직장인의 클로드 활용법](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402583287) · 김도경, 이원석 · 디지털북스 (주간 4위)
  - [창작자의 프롬프트 노트](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404926475) · 이은희 · 김영사 (주간 16위) · 결국 내 이야기로 만드는 AI 실험
- 주목할 신간
  - [AI 시대 수학 펀더멘털](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404759483) · 민재식 · 인사이트 · 벡터에서 푸리에 변환까지, 개념이 말해 주는 것들
  - [하네스 엔지니어링으로 완성하는 에이전틱 AI](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404758980) · 고돈호 · 한빛미디어 · 브리핑 에이전트·자기수정 분석가·움직이는 로봇까지, 프로젝트로 배우는 에이전트 엔지니어링

### 인문

- 베스트 새 진입
  - [세네카, 오늘을 빼앗기고 있는 당신에게 (20만 부 기념 리커버 한정판 에디션)](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404259167) · 세네카 지음, 하와이 대저택 편역 · 논픽션 (주간 2위)
  - [사회를 사고하는 법](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=402435037) · 오사와 마사치 지음, 지비원 옮김 · 갈라파고스 (주간 4위) · 사회학적 상상력의 발견
  - [호모 픽투스, 상상하는 인간](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=401692052) · 호르헤 볼피 지음, 엄지영 옮김 · 엘리 (주간 16위) · 인간의 문명을 만든 픽션의 역사
- 주목할 신간
  - [동물, AI, 신](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404737804) · 웹 킨 지음, 김정은 옮김 · 글항아리 · 인류학으로 모험하는 도덕적 상상력
  - [시대횡단](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=404740368) · 김홍중 · 문학동네 · 안티-코나투스의 존재론

<small>도서 정보: 알라딘 주간 베스트셀러 / 주목할 만한 신간 기준</small>
