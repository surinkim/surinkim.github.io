---
layout: post
title: Telegraf에서 Kafka로 지표 전송
---

시스템의 CPU, 메모리, 네트워크 상태 등을 Telegraf로 수집하여 Kafka로 보낸다.  
전송된 메시지나 브로커 상태는 Kafka UI로 볼 수 있다. 구성은 대략 아래와 같다.

[![](/img/2023_08_27/img1.png)](https://gist.github.com/surinkim/7880b825b70febceba7017be32364b72)



<br/>
<br/>
<br/>
아래는 `docker-compose.yml` 구성이다. 


``` yaml
version: '3.6'
services:

  zookeeper-1:
      image: confluentinc/cp-zookeeper:7.4.0
      ports:
        - "32181:32181"
      environment:
        ZOOKEEPER_CLIENT_PORT: 32181
        ZOOKEEPER_TICK_TIME: 2000
      volumes:
        - zookeeper_data:/var/lib/zookeeper/data
        - zookeeper_logs:/var/lib/zookeeper/logs
      networks:
        - kafka-backend
 
  kafka-1:
    image: confluentinc/cp-kafka:7.4.0
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper-1
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:32181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
      KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka-1:29092,EXTERNAL://localhost:9092
      KAFKA_DEFAULT_REPLICATION_FACTOR: 3
      KAFKA_NUM_PARTITIONS: 3
    networks:
      - kafka-backend
 
 
  kafka-2:
    image: confluentinc/cp-kafka:7.4.0
    ports:
      - "9093:9093"
    depends_on:
      - zookeeper-1
    environment:
      KAFKA_BROKER_ID: 2
      KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:32181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
      KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka-2:29093,EXTERNAL://localhost:9093
      KAFKA_DEFAULT_REPLICATION_FACTOR: 3
      KAFKA_NUM_PARTITIONS: 3
    networks:
      - kafka-backend
 
  kafka-3:
    image: confluentinc/cp-kafka:7.4.0
    ports:
      - "9094:9094"
    depends_on:
      - zookeeper-1
    environment:
      KAFKA_BROKER_ID: 3
      KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:32181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
      KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka-3:29094,EXTERNAL://localhost:9094
      KAFKA_DEFAULT_REPLICATION_FACTOR: 3
      KAFKA_NUM_PARTITIONS: 3
    networks:
      - kafka-backend
 
  kafka-ui:
      image: provectuslabs/kafka-ui
      container_name: kafka-ui
      ports:
        - "8989:8080"
      restart: always
      depends_on:
        - zookeeper-1
        - kafka-1
        - kafka-2
        - kafka-3
      environment:
        - KAFKA_CLUSTERS_0_NAME=local
        - KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=kafka-1:29092,kafka-2:29093,kafka-3:29094
        - KAFKA_CLUSTERS_0_ZOOKEEPER=zookeeper-1:22181
      networks:
        - kafka-backend
 
  telegraf:
    image: telegraf
    container_name: telegraf
    restart: always
    volumes:
    - ./telegraf.conf:/etc/telegraf/telegraf.conf:ro
    networks:
      - kafka-backend

volumes:
  zookeeper_data:
  zookeeper_logs:

networks:
  kafka-backend:
    driver: bridge



```

<br/>
<br/>
<br/>

다음은 `telegraf.conf` 구성이다.  
`brokers` 호스트 이름으로 `kafka-1` 서비스 이름을 써준다.  

``` yaml
[global_tags]

[agent]
  interval = "5s"

[[outputs.kafka]]
  brokers = ["kafka-1:29092"]
  topic = "foo"
  data_format = "json"

[[inputs.cpu]]
  percpu = true
  totalcpu = true
  collect_cpu_time = false
  report_active = false

[[inputs.netstat]]

[[inputs.mem]]

[[inputs.processes]]
```


<br/>
<br/>
<br/>
`doker-compose up`으로 실행한 후에 kafka-ui(http://127.0.0.1:8989)에 접속하면 `telegraf.conf`에 설정한 topic과 메시지 내용을 볼 수 있다.
![02.png](/img/2023_08_27/img2.png)
<br/>
<br/>
<br/>


`docker-compose down`으로 종료한다.
<br/>
<br/>
<br/>



