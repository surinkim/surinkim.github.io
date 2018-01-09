---
layout: post
title: ELK 요약
---

# 1. ELK summary

* What

![Will-Migrating-to-the-Cloud-Save-Money-5.png](/img/2017_03_01/ELK1.png)

> *The ELK Stack is “made up for it”, ie specialized. Our role becomes customize: **Collect the data in the best way**, **automate demand** (or do batch collection) and **creating good reports** for presentation of results or evidence to meet our need.*

![General-ELK-Stack.png](/img/2017_03_01/ELK2.png)

# 2. Logstash
![스크린샷_2015-09-26_오후_9.31.47.png](/img/2017_03_01/ELK3.png)

https://www.elastic.co/kr/products/logstash

## logstash demo(console input/output, grok filter)

  
 - 기본 예제

```logstash
## 아래 콘솔 입력을 필터링해서 콘솔로 출력할 때의 예제
## 2016-12-19 00:00:05.908 [error] <127.0.0.1> sample data

input {
  
    stdin {}

}

filter {

    grok {
        match => { "message" => "%{TIMESTAMP_ISO8601:time} \[%{LOGLEVEL:level}\] \<%{IP:ip}\> %{GREEDYDATA:contents}" }
    }
}

output {

    stdout { codec => rubydebug }

}

```

 - 다른 예제

<script src="https://gist.github.com/surinkim/afea0d01e7583a5229c45bb73d62e163.js"></script>
 

 - Demo : https://asciinema.org/a/4ubbukjn4x5qpu44t7zhg1s7j
 - Grok Debugger : https://grokdebug.herokuapp.com/ 

# 3. Beats

- https://github.com/elastic/beats

- [What is the difference between Logstash and Beats?](https://www.elastic.co/guide/en/beats/filebeat/1.1/diff-logstash-beats.html)

- Demo (FileBeat, HttpBeat)

# 4. Elasticsearch
https://www.elastic.co/kr/products/elasticsearch

 - SQL plugin

  https://github.com/NLPchina/elasticsearch-sql

- shard & replica

  http://guruble.com/?p=85


# 5. Kibana
https://www.elastic.co/kr/products/kibana

 - Demo : http://demo.elastic.co/beats/app/kibana

# 6. Demo