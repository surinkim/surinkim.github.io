---
layout: post
title: 윈도우에서 MinGW 64bit/Code::Blocks 설치
---

#### MinGW 64bit 설치 ####

 1.[MinGW 64bit 셋업 파일](https://sourceforge.net/projects/mingw-w64/?source=typ_redirect)을 다운로드하고 설치를 시작합니다.
 
 
 2.아래 그림처럼 Architecture 항목을 **x86_64**로 설정합니다.
 
 ![MinGW64_1](https://surinkim.github.io/assets/img/2017_10_16/MinGW_1.jpg)
 
 
 3.나머지는 그대로 두고 Next를 눌러 설치를 완료합니다.


#### Code::Blocks 설치 ####

 1.[Code::Blocks 다운로드 페이지](http://www.codeblocks.org/downloads/26)에서 셋업 파일을 다운로드 합니다.
 
 
 - 위에서 MinGW 64bit 버전을 설치했으므로 Code::Blocks만 설치하는 **codeblocks-16.01-setup.exe**를 다운로드 합니다.
 
 
 - 이 글을 쓰는 현재 Code::Blocks의 최신 버전은 16.01입니다.
 
 
 2.기본 설정을 그대로 두고 설치를 완료합니다.
 
 
 3.설치가 완료되면  Code::Blocks를 실행하고 Settings -> Compiler -> Toolchain executables를 차례로 클릭합니다.
 
 
 
 ![CodeBlocks 1](https://surinkim.github.io/assets/img/2017_10_16/codeblocks_1.jpg)
 
 ![CodeBlocks 2](https://surinkim.github.io/assets/img/2017_10_16/codeblocks_2.jpg)
 
 4.아래 그림처럼 컴파일러를 설정합니다. 컴파일러 설치 디렉토리 경로에 bin 폴더가 들어가지 않도록 주의하세요.
  
```
ex)C:\Program Files\mingw-w64\x86_64-7.1.0-posix-seh-rt_v5-rev2\mingw64\
```

![CodeBlocks 3](https://surinkim.github.io/assets/img/2017_10_16/codeblocks_3.jpg)





