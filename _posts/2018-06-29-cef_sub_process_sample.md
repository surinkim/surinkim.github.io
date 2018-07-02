---
layout: post
title: CEF sub process 샘플
---





cef는 chrome과 동일하게 멀티 프로세스로 동작한다. 만약, all.exe를 만들어 실행하더라도, 보통 3개의 all.exe 프로세스가 생성되며 각각 browser(**main**), renderer/gpu(**sub**) 프로세스 역할을 담당한다.   
배틀넷 런처, LOL 클라이언트 등 대부분의 cef 애플리케이션은 main 프로세스 전용의 exe(예를 들어, host.exe)와 renderer/gpu 전용의 exe(예를 들어, sub.exe)를 만들어 사용한다.   
이렇게 하면, host에 주요 로직을 두고, sub에 메시지 라우터 같은, 자바스크립트와의 연동 처리를 둬서 코드를 분리할 수 있다.  

[이 페이지](https://bitbucket.org/chromiumembedded/cef/wiki/GeneralUsage#markdown-header-entry-point-function)를 참고해서 간단히 샘플을 만들었는데, [여기서](https://github.com/surinkim/cef_sub_process) 확인할 수 있다. vs2015 솔루션이 들어있고 빌드 환경은 x64/debug만 설정했다.

디버그 버전 libcef.dll 크기가 100M가 넘기 때문에 clone 할 때, 조금 기다려야 한다.  

 > github에는 50M가 넘어가는 파일은 올릴 수 없는데, [Git LFS](https://git-lfs.github.com/)를 사용하면 소스 코드처럼 빈번하게 변경되는 파일들과 구분해서, 덩치 큰 바이너리 파일도 올릴 수 있다.

 > sub.exe 빌드 후, post build event로 manifest를 추가하는 과정이 있는데, 이 과정을 skip 하면 윈도우 10에서는 웹 페이지가 보이지 않는다. 윈도우 7에서는 제대로 보인다.