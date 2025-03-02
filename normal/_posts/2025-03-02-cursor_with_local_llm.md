---
layout: post
title: Cursor에서 로컬 LLM 사용하기
---



cursor는 어떤 LLM을 사용할 지 설정이 가능하다. 그래서 LM studio, ngrok을 활용하면 무료로 로컬 LLM을 사용할 수 있다.
대략 이런 식이다.


[![](/img/2025_03_02/img1.png)](https://gist.github.com/surinkim/627706fa97d6f3fcb1dbc54b7aec0790)

먼저, LM Studio에서 사용할 모델을 로딩하고 설정한다. 그리고 ngrok을 통해 cursor에서 접속할 수 있도록 한다.
cursor에서는 앞서 LM Studio에서 로딩한 모델과 ngrok의 서버 주소를 입력한다.


<br/>
<br/>

1. LM Studio에서 모델 로딩 & 설정  
![LM Studio 설정](/img/2025_03_02/img2.png)


2. ngrok 설치 & 실행   
ngrok을 설치하고 실행한다. 포트 번호는 LM Studio에서 설정한 포트 번호를 입력한다.
```bash
ngrok http 1234
```
그러면 아래 화면처럼 나오는데, 여기서 서비스 되는 url을 확인하고 복사한다.
![ngrok](/img/2025_03_02/img3.png)


3. cursor 설정  
![cursor 설정](/img/2025_03_02/img4.png)
OpenAI API KEY에는 아무 키나 입력하고 OpenAI Base URL에 위 2번의 서비스 url + /v1을 입력하고 save & verify 한다.
verify할 때 에러가 없어야 한다.


무료로 LLM을 사용하고 코드 유출 위험을 줄이는 장점은 있지만, 깃허브 코파일럿이나 claude 같은 유료 모델에 비하면 성능은 아쉬울 수 밖에 없다. 

<br/>
<br/>

참고: [Run Cursor AI for Free with Open-Source LLM](https://medium.com/@hyperfox_/run-cursor-ai-for-free-with-open-source-llm-55396c1411b1)