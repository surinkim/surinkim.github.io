---
layout: post
title: 로그스태시 date, fingerprint 필터
---

로그스태시로 수집한 데이터가 앨라스틱서치에 쌓일 때, `@timestamp` 값에는 로그가 수집되는 현재 시간이 디폴트로 설정된다.
실시간으로 수집되는 로그라면 별 문제가 없겠지만, 이런 저런 이유로 로그에 포함돼 있는 시간과 실제로 로그스태시가 
수집하는 시간의 차이가 크다면, **date** 필터를 활용해서 현재 시간 대신, 로그에 포함돼 있는 타임스탬프 값이 `@timestamp`에 설정되도록 할 수 있다.

``` logstash
## case 1)로그 형식이 아래와 같을 때(json)
## {"log_time":"2018-07-25 12:22:02"}

filter {
  json {
    source => "message"
  }
  
  date {
    match => ["log_time", "YYYY-MM-dd HH:mm:ss"]
  }

}


## case 2)로그 형식이 아래와 같을 때
## 2016-12-19 00:00:05.908 [error] <127.0.0.1> sample data 

filter {

    ## grok 패턴에서 로그 시간을 time 필드로 매칭 시킨다.
    grok {
        match => { "message" => "%{TIMESTAMP_ISO8601:time} \[%{LOGLEVEL:level}\] \<%{IP:ip}\> %{GREEDYDATA:contents}" }
    }
    
    ## date 필터를 사용해서 @timestamp 값에 time 필드 값이 설정되도록 한다.
    date {
        
        match => ["time", "ISO8601"]     
        
        ## time 필드를 더 이상 사용하지 않는다면 제거한다.
        remove_field => ["time"]
    }

}
```

한편, 여러 복잡한 상황상, 동일 데이터가 여러 로그 파일에 들어가 있다면...엘라스틱서치에도 중복해서 들어가게 된다.
이때는 **fingerprint** 필터를 사용해서 동일 데이터의 중복 적재를 막을 수 있다. 해시값을 생성하기 때문에 사용하지 않을 때보다 수집 시간은 길어진다.

``` logstash

filter {

  ...

 # for remove that duplicate log
    fingerprint {
        method => "SHA1"
        key => "KEY"
    }
}


output {
    elasticsearch {
        hosts => ["localhost:9200"]
        index => "demo_log"
        document_id => "%{fingerprint}"
        
    }
    stdout { codec => rubydebug }
}


```