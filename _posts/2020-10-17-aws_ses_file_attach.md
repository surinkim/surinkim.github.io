---
layout: post
title: aws ses(simple email service)를 이용한 파일 첨부 메일 전송
---

제목과 내용만 채워 이메일을 보낸다면 aws ses의 `send-email` 명령으로 아래처럼 보낼 수 있다.  
```bash
aws ses send-email --region us-west-2 --from abc@abc.com --to abc@abc.com --subject "Hello" --html "Hello, there"
```

메일에 파일을 첨부하려면 `send-raw-email` 명령을 사용한다.  
`send-raw-email`은 CLI에서 처리하기 까다롭다. 파이썬을 쓸 수 있는 환경이라면 파이썬 AWS SDK인 [boto3](https://aws.amazon.com/ko/sdk-for-python/)를 써서 쉽게 처리할 수 있다.  

아래 코드 snippet은 `send-raw-email`을 사용하는 boto3 샘플 코드에서 '제목'을 실행 parameter로 전달할 수 있게 하고, '여러 수신인'을 설정할 수 있도록 조금 손 댄 코드다.  

<script src="https://gist.github.com/surinkim/5190f14bc8724179550c7e337b21d759.js"></script>

> 참고 1)  
> 보내는 메일 주소와 받는 메일 주소는 모두 aws ses 콘솔에서 '인증'된 주소여야 한다.
> ![01.png](/img/2020_10_17/aws_ses_console.png)

> 참고 2)  
> 샘플 코드의 `CONFIGURATION_SET`을 사용하려면 aws ses 콘솔에서 `ConfigSet`을 만들어줘야 한다. 사용하지 않으려면 주석 설명처럼, 샘플 코드의 20, 97 line 두 군데를 주석 처리해 준다.


