---
layout: post
title: windows proxy
---

일반적으로 윈도우 애플리케이션은 아래 3가지 방법으로 프록시 서버를 사용한다.

1. WinInet 사용  
WinInet 라이브러리를 사용하는 애플리케이션은 Internet Explorer에서 구성한 것과 동일한 프록시 설정을 사용한다.  
다른 애플리케이션에서도 WinInet으로 이 설정을 구해서 사용할 수 있다.

2. WinHttp 사용  
WinHttp는 윈도우 서비스처럼, 백그라운드에서 사용자 개입이 필요 없는 애플리케이션에 적합하며, WinInet에 비해 속도면에서 빠르다.  
WinHttp의 프록시 설정과 WinInet의 프록시 설정은 서로 다르며, WinHttp는 default로 WinInet의 프록시 설정을 사용하지 않는다.


3. 애플리케이션 자체에 프록시 셋팅을 포함  
애플리케이션 자체에서 Winsock 라이브러리를 사용해서 직접 프록시 설정을 구성한다.  

`따라서, 아래와 같이 WinHttp를 사용한 프록시 설정은, WinInet의 프록시 설정(=Internet Explorer)과 서로 무관`하다.

![01.png](/img/2020_10_18/proxy_show.png)


한편, [WinHttpGetIEProxyConfigForCurrentUser](https://docs.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser)를 이용하면 IE의 프록시 설정을 얻어 올 수 있다.  
 - [예시 코드](https://chromium.googlesource.com/external/libjingle/chrome-sandbox/+/60598307c80be80da28e5ae7921352bd874fb05b/talk/base/proxydetect.cc#675)

만약, IE 설정에서 '자동으로 설정 검색'이 켜져 있다면 [WinHttpGetProxyForUrl](https://docs.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurl)을 추가로 사용해야 한다.  
 - ![02.png](/img/2020_10_18/IE_OPT_01.png)
 - [예시 코드 1](https://chromium.googlesource.com/external/libjingle/chrome-sandbox/+/60598307c80be80da28e5ae7921352bd874fb05b/talk/base/proxydetect.cc#1246): WinHttpGetProxyForUrl을 호출해야 할 지 판단  
 - [예시 코드 2](https://chromium.googlesource.com/external/libjingle/chrome-sandbox/+/60598307c80be80da28e5ae7921352bd874fb05b/talk/base/proxydetect.cc#712): WinHttpGetProxyForUrl 사용  

 
 참고로, Fiddler는 IE 프록시 설정을 통해 WinInet 세션을 캡처한다. Fiddler를 실행하고 `Capture Traffic`을 켰다면 아래처럼 IE 프록시가 설정된다.  
 ![03.png](/img/2020_10_18/IE_OPT_02.png)  

 WinInet이 아닌 WinHttp, cURL을 사용하는 애플리케이션은, 위 IE 설정을 `WinHttpGetIEProxyConfigForCurrentUser` 등으로 구해서 프록시 설정을 해줘야 Fiddler에서 트래픽을 캡처할 수 있다.  
 그렇지 않은 애플리케이션이라면, WinHttp는 수동으로 아래 명령을,
 ```bash
 netsh winhttp set proxy 127.0.0.1:8888
 ```

cURL은 아래 명령을 수동으로 실행하면 Fiddler에서 트래픽 캡처가 가능하다.
```bash
curl --proxy 127.0.0.1:8888
```

> 참고 1: [Windows proxy settings explained](https://securelink.net/en-be/insights/windows-proxy-settings-explained/)  
> 참고 2: [Manages proxy settings for WinHTTP](https://docs.ansible.com/ansible/latest/collections/community/windows/win_http_proxy_module.html)  
> 참고 3: [Configure a WinHTTP Application to Use Fiddler](https://docs.telerik.com/fiddler/configure-fiddler/tasks/ConfigureWinHTTPApp)  
> 참고 4: [Configure a PHP/cURL Application to Use Fiddler](https://docs.telerik.com/fiddler/configure-fiddler/tasks/ConfigurePHPcURL)  



