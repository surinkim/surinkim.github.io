---
layout: post
title: code sign 인증서 만료
---

아래처럼 -t 옵션을 주고 code sign을 했다면, 인증서 만료 시간이 도래한다고 해서, 이미 배포한 바이너리를 새로 sign하고 다시 배포할 필요는 없다.  
그러니까, code sign했던 시점에 유효한 인증서였다면, 인증서 기간이 만료되어도 계속 유효한 게시자로 표시된다.
 
```bash
-t http://timestamp.verisign.com/scripts/timstamp.dl
```

#### 참고:
  
> VeriSign Code Signing Certificates include an optional timestamp to extend the life of your digital signatures.
> Your code will remain valid even if your code signing certificate expires, because the validity of the code signing certificate at the time of the digital signature can be verified
> http://www.symantec.com/theme.jsp?themeid=code-signing-information-center
  
> Timestamping ensures that code will not expire when certificate expires.
> If your code is timestamped the digital signature is valid even though the certificate has expired.
> A new certificate is only necessary if you want to sign additional code. If you did not use the timestamping option during the signing, you must re-sign your code and re-send it out to your customers.
> http://www.instantssl.com/code-signing/code-signing-faq.html

  
> Timestamping ensures that code will not expire when the certificate expires because the browser validates the timestamp.
> The timestamping service is provided courtesy of VeriSign. If you use the timestamping service when signing code, a hash of your code is sent to VeriSign’s server to record a timestamp for your code.
> https://search.thawte.com/support/ssl-digital-certificates/index?page=content&id=AR1119