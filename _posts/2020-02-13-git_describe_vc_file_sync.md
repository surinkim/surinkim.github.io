---
layout: post
title: git describe로, git 소스 버전을 VC++에서 빌드한 파일 버전으로 자동 연동하기
---


[git describe](https://git-scm.com/docs/git-describe)는  태그와  커밋  횟수, 축약된  커밋  이름으로  사람이  읽고  구분할  수  있는  버전  정보를  알려준다.

```bash
$ git describe
v1.0.9-8-gbab53f6
```
`v1.0.9-8-gbab53f6`에서 `v1.0.9`은 현재 태그, `8-gbab53f6`은 해당 태그부터 8번째 commit이며, 축약된 commit 이름이 `bab53f6`이라는 뜻이다. 접두사 `g`는 `git`을 뜻하며 어떤 SCM을 사용하느냐에 따라 다르다. 이 명령을 이용하면 git 저장소의 소스 버전을 VC++ 프로젝트에서 빌드한 파일 버전으로 자동 연동할 수 있다.

이렇게 하려면, git describe 결과를 얻고 적당한 파일에 버전 정보를 써주는 과정이 필요하다. 이런 역할을 해주는 스크립트는 쉽게 구할 수 있는데 여기서는 [이곳의 배치 파일](https://github.com/Thell/git-vs-versioninfo-gen/blob/master/GIT-VS-VERSION-GEN.bat)을 사용한다.

로컬의 git 저장소 폴더에서 아래와 같이 실행하면
```bash
.\git-vs-version-get.bat .\versioninfo.h
```
`versioninfo.h` 파일을 생성해 준다.
```c++
//GIT-VS-VERSION-GEN.bat generated resource header.
#define  GEN_VER_VERSION_STRING  "1.0.9.8.gbab53\0"
#define  GEN_VER_DIGITAL_VERSION  1,0,9,8
#define  GEN_VER_VERSION_HEX  0x0001000000090008
#define  GEN_VER_COMMENT_STRING  "Major Version Release\0"
#define  GEN_VER_PRIVATE_FLAG VS_FF_PRIVATEBUILD
#define  GEN_VER_PRIVATE_STRING  "\0"
#define  GEN_VER_PATCHED_FLAG VS_FF_PATCHED
#define  GEN_VER_PRERELEASE_FLAG  0
```

VC++ 프로젝트에서 이 파일을 사용하도록 설정한다.
`.rc`파일에 `versioninfo.h`를 include하고, `FILEVERSION`, `PRODUCTION`의 값을 `GEN_VER_DIGITAL_VERSION` 매크로 변수로 대체한다.
```rc
/////////////////////////////////////////////////////////////////////////////
//
// Version
//

VS_VERSION_INFO VERSIONINFO
 FILEVERSION GEN_VER_DIGITAL_VERSION
 PRODUCTVERSION GEN_VER_DIGITAL_VERSION
..
..
```
문자열 값이 필요한 곳은 `GEN_VER_VERSION_STRING`을 사용한다.
```rc
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "041204b0"
        BEGIN
            ...
            VALUE "FileVersion", GEN_VER_VERSION_STRING
            ...
            VALUE "ProductVersion", GEN_VER_VERSION_STRING
        END
...
...
```
이제 VC++의 `빌드 전 이벤트`에, `git-vs-version-get.bat`으로 `versioninfo.h`를 생성하는 과정을 추가해주면, git 저장소의 소스 버전이 VC++ 빌드 파일 버전에 자동 연동된다.




