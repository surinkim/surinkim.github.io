---
layout: post
title: cocos2dx 설치 및 프로젝트 생성하기
---

Cocos2d-x 설치 및 프로젝트 생성 절차를 정리한다.

### 1. 파이썬 2.7.X 버전 설치

- cocos2dx는 현재도, 앞으로도 [파이썬 3.X 버전의 지원 계획이 없다.](https://github.com/cocos2d/cocos2d-x/issues/11210)
- 따라서, 다른 파이썬 버전이 이미 설치돼 있더라도, 2.7.X 버전을 반드시 설치해야 한다.
- path에 파이썬 2.7.X와 다른 버전이 이미 설정돼 있다면, 아래 `2. cocos2dx 설치` 하기 전에 2.7 경로로 잠깐 바꾸고, 프로젝트 생성한 뒤에 원래 버전으로 원복하는 건 괜찮다.
![01.png](/img/2020_08_24/01.png)

### 2. Cocos2d-x 설치
- https://cocos2d-x.org/download 에서 3.17.2 다운로드(4.0 버전도 있지만, 참고할 레퍼런스는 대부분 ver 3.X 기준이라 제외함.)
- 가능한 드라이브 루트 경로에 압축 해제
- 압축 해제 후에, 폴더 내의 setup.py를 cmd 창에서 실행한다.
> `setup.py`는 cocos2d-x에서 사용하는 환경 변수를 자동으로 등록해 준다.
- 환경 변수 등록시에 `NDK_ROOT, ANDROID_SDK_ROOT, ANT_ROOT` 등은 windows 개발할 때 필요없으므로 Enter 쳐서 skip해도 된다.
- 등록이 끝나고, cmd 창에서 `cocos` 명령을 실행했을 때 아래와 같이 나오면 정상이다.       
![02.png](/img/2020_08_24/02.png)


### 3. cocos2dx 샘플 프로젝트 생성
- cocos 명령으로 프로젝트 생성
- cocos new [프로젝트명] –p [패키지명] –l [사용할 언어] –d [생성할 경로]
> ex )cocos new hello -p com.cocos2dx.hello -l cpp -d e:\cocos2d-x-3.17.2\projects
- 프로젝트 생성이 완료되면, 아래 경로에 비주얼 스튜디오 솔루션 파일이 생성된다.
![03.png](/img/2020_08_24/02.png)

### 기타
- Windows에서는 기본으로 x86 플랫폼만 지원한다. Cocos2d-x의 종속성 라이브러리들을 x64로 빌드해주는 별도의 프로젝트가 있으니, x64 플랫폼이 필요하면 이걸 쓰라는 답변이 있다.
- StackOverflow에서, [Cocos2d-x는 모든 플랫폼에서 OpenGL을 사용한다](https://stackoverflow.com/questions/24859556/is-cocos2d-x-always-uses-opengl), [WP8은 OpenGL을 지원하지 않으므로 Angle을 사용한다](https://github.com/cocos2d/cocos2d-x/pull/5924)'는 글이 보이는데, 워낙 옛날 글이고 3.0 업데이트 이전 글이라 지금은 어떻게 달라졌는지 모르겠다. 
> [4.0 버전부터 애플 플랫폼에서는 Metal을 렌더링 엔진으로 사용한다.](https://docs.cocos2d-x.org/cocos2d-x/v4/en/upgradeGuide/)

