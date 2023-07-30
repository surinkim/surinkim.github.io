---
layout: post
title: 오픈메트릭스(OpenMetrics)
---


오픈메트릭스(OpenMetrics)는 클라우드 네이티브 앱의 메트릭 노출 표준화를 목표로 하는 CNCF 프로젝트다.  
오픈메트릭스의 사양은 아래에 공개되어 있다.  
https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md


오픈메트릭스는 프로메테우스(Prometheus) 메트릭 형식을 기반으로 한다. 프로메테우스 메트릭 형식은 간단한 텍스트 기반의 사람이 읽을 수 있는 데이터 형식이다.  
InfluxDB, OpenTSDB, Graphite를 비롯한 다른 모니터링 시스템에서도 채택하고 있다. 많은 CNCF 프로젝트가 프로메테우스 메트릭 형식을 사용하여 메트릭을 노출한다. 또한 API 서버, etcd, CoreDNS 등과 같은 핵심 쿠버네티스 구성 요소에서도 찾을 수 있다.  
프로메테우스 메트릭 형식이 많이 채용되면서 독립적인 프로젝트가 되었고, 이 메트릭 형식을 업계 표준으로 만들기 위한 프로젝트가 바로 오픈메트릭스다.


### 데이터 모델
아래는 오픈메트릭스의 메트릭 데이터 예시다.

``` bash
# TYPE acme_http_router_request_seconds summary
# UNIT acme_http_router_request_seconds seconds
# HELP acme_http_router_request_seconds Latency though all of ACME's HTTP request router.
acme_http_router_request_seconds_sum{path="/api/v1",method="GET"} 9036.32
acme_http_router_request_seconds_count{path="/api/v1",method="GET"} 807283.0
acme_http_router_request_seconds_created{path="/api/v1",method="GET"} 1605281325.0
acme_http_router_request_seconds_sum{path="/api/v2",method="POST"} 479.3
acme_http_router_request_seconds_count{path="/api/v2",method="POST"} 34.0
acme_http_router_request_seconds_created{path="/api/v2",method="POST"} 1605281325.0
# TYPE go_goroutines gauge
# HELP go_goroutines Number of goroutines that currently exist.
go_goroutines 69
# TYPE process_cpu_seconds counter
# UNIT process_cpu_seconds seconds
# HELP process_cpu_seconds Total user and system CPU time spent in seconds.
process_cpu_seconds_total 4.20072246e+06
# EOF

```



### 메트릭스 엔드포인트
이 표준을 구현하려면 문서화된 엔드포인트에 대한 HTTP Get 요청의 응답으로 오픈메트릭스 형식의 메트릭을 노출한다. 엔드포인트의 이름은 /metrics다.  



sysdig에서 제공하는 샘플 앱으로 실제 메트릭 형식을 살펴보자.

```bash
$ git clone https://github.com/sysdiglabs/custom-metrics-examples
$ docker build custom-metrics-examples/prometheus/golang -t prometheus-golang
$ docker run -d --rm --name prometheus-golang -p 8080:8080 prometheus-golang
```

브라우저에서 localhost:8080/metrics로 이동한다.


### 클라이언트 라이브러리
프로메테우스 메트릭 형식을 구현한 클라이언트 라이브러러 목록은 아래에서 볼 수 있다.
이 클라이언트를 사용해서 오픈메트릭스의 매트릭 형식도 노출 가능한지는 더 확인해봐야겠다.  
https://prometheus.io/docs/instrumenting/clientlibs/

<br/>

> 참고 1: [OpenMetrics and Prometheus Exposition Format](https://baris.io/blog/prometheus-exposition-format-openmetrics)  
> 참고 2: [Prometheus metrics / OpenMetrics code instrumentation](https://sysdig.com/blog/prometheus-metrics/)

<br/>
<br/>


