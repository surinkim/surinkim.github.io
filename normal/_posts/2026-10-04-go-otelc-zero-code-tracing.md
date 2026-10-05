---
layout: post
title: otelc를 사용한 Go 트레이싱
---

트레이스는 어떤 요청이 어디서 얼마나 시간을 소비했는지 알려준다. 하나의 요청이 HTTP 핸들러, 캐시, DB를 거치는 동안 걸린 시간을 구간별로 기록하기 때문에 개별 api의 처리 속도를 확인하고 개선할 수 있다.

Java나 Python은 실행할 때 에이전트를 붙이면 코드를 고치지 않아도 트레이스를 얻을 수 있지만, Go는 정적 바이너리라 그런 방법이 없었다. 핸들러와 DB 호출마다 `otelhttp`, `otelsql` 같은 계측 코드를 직접 넣어야 했다.

[40주차 다이제스트](/normal/2026/10/03/weekly-dev-links-2026w40/)에서 소개한 OpenTelemetry Go 컴파일 타임 계측(`otelc`)이 v1이 됐다. 사용법은 `go build` 대신 `otelc go build`로 빌드하는 것뿐이다. 예제 서비스를 만들어 직접 돌려 봤다.

```bash
go build -o app .           # 평범한 서버
otelc go build -o app .     # 같은 코드, 트레이스를 보내는 서버
```

예제 코드는 [GitHub 저장소](https://github.com/surinkim/otelc-trace-demo)에 있고, Docker만 있으면 `docker compose up`으로 실행할 수 있다.

<br/>

### 동작 방식

`go build`는 패키지마다 컴파일러를 호출하는데, `-toolexec` 옵션을 주면 이 호출이 지정한 프로그램을 거쳐 간다. `otelc`는 여기서 패키지가 계측 규칙에 해당하는지 보고, 해당하면 대상 함수의 시작과 끝에 span을 만드는 코드를 넣은 뒤 컴파일러에 넘긴다. 내 코드뿐 아니라 Gin, go-redis 같은 의존성과 `net/http`, `database/sql` 같은 표준 라이브러리도 이 방식으로 계측된다.

바뀐 코드는 빌드 작업 폴더(`.otelc-build/`)에만 생긴다. 데모를 빌드한 뒤에도 소스와 `go.mod`는 그대로였다.

v1이 지원하는 라이브러리는 `net/http`, gRPC, `database/sql`, Gin, go-redis, segmentio/kafka-go, `log/slog`, MongoDB, AWS SDK 등이다. 전체 목록은 [여기](https://opentelemetry.io/docs/zero-code/go/compile-time/supported-libraries/)서 볼 수 있다.

<br/>

### 데모 구성

예제는 `main.go` 파일 하나짜리 Gin API이고, OpenTelemetry 코드는 넣지 않았다.

| 엔드포인트 | 하는 일 |
|---|---|
| `GET /users/:id` | Redis 캐시 확인 → 없으면 SQLite 조회 → Redis에 저장 |
| `GET /report` | 일부러 느리게 만든 쿼리 (약 0.7초) |
| `GET /users-noctx/:id` | 요청 `ctx`를 넘기지 않는 버전 |

`docker compose up`을 하면 아래 네 컨테이너가 뜬다. `grafana/otel-lgtm`은 트레이스를 받는 OTel Collector, 트레이스 저장소인 Tempo, 조회 화면인 Grafana를 한 컨테이너에 묶은 체험용 이미지다.

- `grafana/otel-lgtm`
- Redis
- `app-otel` (8080): `otelc go build`로 빌드
- `app-plain` (8081): `go build`로 빌드

두 앱은 같은 Dockerfile을 쓰고, 빌드 명령만 다르다.

```dockerfile
# app-otel: otelc를 설치한 뒤 otelc로 빌드
RUN go install go.opentelemetry.io/otelc/tool/cmd/otelc@v1.1.0
RUN CGO_ENABLED=0 otelc go build -o /out/app .

# app-plain
RUN CGO_ENABLED=0 go build -o /out/app .
```

트레이스를 보낼 주소는 실행할 때 환경 변수로 준다.

```yaml
environment:
  OTEL_SERVICE_NAME: otelc-demo
  OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
```

<br/>

### 실행

```bash
git clone https://github.com/surinkim/otelc-trace-demo
cd otelc-trace-demo
docker compose up -d --build
./load.sh 8080    # otelc로 빌드한 서버에 요청
./load.sh 8081    # go build로 빌드한 서버에 요청
```

[http://localhost:3000](http://localhost:3000)에서 Explore를 열고 데이터 소스를 Tempo로 바꾼다. Query type은 TraceQL로 두고 아래 쿼리를 넣은 뒤 Run query를 누른다.

```
{resource.service.name="otelc-demo" && name=~"GET.*"}
```

목록에서 Trace ID를 누르면 요청 하나의 구간별 시간이 나온다. 아래는 캐시에 없는 사용자를 조회한 요청이다. Redis `get`, SQLite `SELECT`, Redis `set` 순서로 실행됐고, span 속성에는 실행한 SQL과 Redis 명령이 들어 있다.

![GET /users/:id 트레이스](/img/2026_10_04/trace_users.png)

`/report`는 1부터 200만까지 더하는 재귀 쿼리로 일부러 느리게 만든 엔드포인트다. 트레이스를 보면 전체 684ms 중 683ms가 이 쿼리에서 걸렸다.

![GET /report 트레이스](/img/2026_10_04/trace_report.png)

8081로 보낸 요청은 Grafana에 남지 않았다.

<br/>

### Grafana 없이 파일로 남기기

`otelc`가 넣는 초기화 코드는 `OTEL_TRACES_EXPORTER=console`을 지원해서, 트레이스를 표준출력으로 받을 수도 있다.

```bash
docker compose up -d redis        # Redis만 띄운다
otelc go build -o bin/otel .      # otelc로 빌드

# 트레이스를 표준출력으로 찍게 하고(console), 그 출력을 traces.jsonl에 저장한다
GIN_MODE=release OTEL_TRACES_EXPORTER=console \
OTEL_METRICS_EXPORTER=none OTEL_LOGS_EXPORTER=none \
./bin/otel > traces.jsonl
```

서버가 떠 있는 동안 다른 터미널에서 `curl localhost:8080/users/3`처럼 요청을 보내면, span이 한 줄에 하나씩 JSON으로 쌓인다. trace ID가 같은 줄이 한 요청이다.

```bash
$ jq -r 'select(.Name) | "\(.SpanContext.TraceID[0:8])  \(.Name)"' traces.jsonl
dd8739a7  get
dd8739a7  GET /users/:id
64241352  get
64241352  GET /users/:id
```

span은 기본 5초 간격으로 모아서 쓰기 때문에, 요청 직후에 프로세스를 끄면 마지막 몇 개가 빠질 수 있다.

<br/>

### 해 보면서 확인한 것

#### ctx를 넘기지 않으면 span이 끊긴다

앞의 `/users/:id` 트레이스에서는 Redis `get`, SQLite `SELECT`, Redis `set`이 `GET /users/:id` 아래에 묶여 있었다. 이렇게 묶이려면 Redis나 DB를 호출할 때 지금 어느 요청을 처리 중인지 알려 줘야 하고, Go에서는 이 정보를 `context.Context`(이하 `ctx`)에 담아 넘긴다.

```go
// /users/:id: 요청의 ctx를 넘긴다
s.rdb.Get(ctx, key)
s.db.QueryRowContext(ctx, "SELECT id, name FROM users WHERE id = ?", id)

// /users-noctx/:id: 요청의 ctx를 넘기지 않는다
s.rdb.Get(context.Background(), key)                       // 빈 ctx
s.db.QueryRow("SELECT id, name FROM users WHERE id = ?", id) // ctx를 받지 않는 함수
```

`/users-noctx/:id`는 요청 하나가 트레이스 세 개로 나뉘었다. `GET /users-noctx/:id` 트레이스에는 HTTP span 하나만 남았고, Redis `get`과 SQLite `SELECT`는 각각 별도 트레이스로 기록됐다.

![GET /users-noctx/:id 트레이스](/img/2026_10_04/trace_noctx.png)

`otelc`는 goroutine마다 trace 정보를 저장하는 필드를 Go 런타임에 추가한다. 그래서 `ctx`를 넘기지 않아도 같은 goroutine 안의 호출은 연결될 수 있겠다고 예상했는데, 실제로는 그렇지 않았다.

#### 빌드 시간과 바이너리 크기

M1 맥, Go 1.26.0, otelc v1.1.0에서 잰 값이다.

| | `go build` | `otelc go build` |
|---|---|---|
| 첫 빌드 | - | 약 49초 (의존성 다운로드 포함) |
| 재빌드 | 1초 미만 | 약 10초 |
| 바이너리 크기 | 29MB | 58MB |

#### 실행 중 부하

otelc README에는 "Zero Runtime Overhead"라고 적혀 있지만, 계측을 안 했을 때와 비교한 말은 아니다. otelc가 따로 더하는 부하가 없다는 뜻이고, span을 만들고 보내는 OpenTelemetry SDK의 부하는 계측 코드를 직접 넣었을 때처럼 그대로 생긴다. 공식 문서에 실행 중 부하에 대한 수치는 없어서 데모의 두 서버에 같은 부하를 주고 비교했다.

M1 맥의 Docker Desktop에서 두 앱 모두 CPU 1개, 메모리 256MB로 제한하고, `ab`로 2만 건(동시 접속 10)씩 7번 보낸 결과의 중앙값이다. 샘플링 없이 모든 트레이스를 로컬 `otel-lgtm`으로 보냈다. 측정 스크립트는 저장소의 `bench.sh`에 있다.

`GET /users/1` (Redis 캐시 hit, 요청당 span 2개)

| | `go build` | `otelc go build` |
|---|---|---|
| 처리량 | 12,694 req/s | 10,191 req/s |
| 평균 응답 시간 | 0.79ms | 0.98ms |
| p99 응답 시간 | 2ms | 4ms |
| 요청당 CPU 시간 | 45µs | 78µs |
| 메모리 | 9MB | 17MB |

요청당 CPU 시간이 약 33µs 늘었고 처리량은 20% 줄었다.

같은 조건에서 0.7초쯤 걸리는 `GET /report`는 평균 응답 시간이 736ms와 732ms로 차이가 없었다. 늘어나는 CPU 시간이 요청당 수십 µs 수준이라, 처리 자체가 가벼운 API일수록 차이가 크게 보인다.

#### 시작할 때 실행한 쿼리

서버 시작 시 테이블 생성과 초기 데이터 INSERT도 쿼리마다 별도 트레이스로 남았다. HTTP 요청 안에서 실행된 게 아니라 부모 span이 없어서다.

#### Redis 명령 인자

Redis span의 `db.query.text`에는 `set user:7 user-7 ex 30`처럼 저장한 값까지 기록된다. 캐시에 민감한 값을 넣는다면 Collector에서 이 속성을 지우는 처리가 필요하다.

#### Go 버전

`otelc`는 Go 1.26 이상이 필요하다. (1.26은 2026년 2월 릴리스)

<br/>

### 운영 환경에서는

데모의 `otel-lgtm`은 체험용이라, 실제로는 Grafana Cloud나 Honeycomb 같은 SaaS로 보내거나 Tempo·Jaeger를 직접 운영한다. 트레이스는 요청마다 생기므로 `OTEL_TRACES_SAMPLER=parentbased_traceidratio`, `OTEL_TRACES_SAMPLER_ARG=0.1`처럼 일부만 보내도록 샘플링을 설정하는 경우가 많다.

참고: [otelc v1 발표](https://opentelemetry.io/blog/2026/go-compile-time-instrumentation-v1/) · [시작 가이드](https://opentelemetry.io/docs/zero-code/go/compile-time/getting-started/) · [otelc GitHub](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation)
