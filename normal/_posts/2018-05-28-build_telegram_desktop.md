---
layout: post
title: Telegram desktop 빌드
---




Telegram은 pc 및 모바일 버전 클라이언트 소스를 github에 공개하고 있다.
Telegram 역시 Qt를 사용하고 있기 때문에 참고할 내용이 많겠다 싶어 pc 버전을 받아서 빌드해봤다.  

대부분은 [Build instructions for Visual Studio 2017](https://github.com/telegramdesktop/tdesktop/blob/dev/docs/building-msvc.md)을 따라하고,
다음 몇 가지만 주의하면 된다.

 - VS2017 설치할 때, '개별 구성 요소'에서 'UWP용 Windows 10 SDK(10.0.16299.0):C++'도 설치한다. 이때, C#, VB, JS 버전도 같이 설치된다.

 - cmake의 현재 버전은 3.11.X다. 그런데, 이 버전을 설치하면 openal 빌드가 실패한다. 이미 [패치](https://github.com/kcat/openal-soft/commit/cae4b1a062b53dd25eba7caa41622be730106749)는 됐지만, 아직 릴리즈가 안됐다. 그래서, cmake를 3.10.3으로 설치했다.

 - nasm 경로도 path에 추가해줘야 ffmpeg 빌드가 성공한다.

 - 솔루션 생성을 하고 vs2017로 빌드하면 3개의 에러가 발생한다. 그런데, C2220(모든 경고를 오류로 처리)에러로 인해 연달아 발생하는 오류들이므로, 이 에러만 잡으면 된다. 제대로 하려면 모든 경고를 잡아야 하지만, 우선은 **빌드 성공이 목적**이므로 옵션에서 '경고를 오류로 처리 안함.(WX-)'으로 다시 빌드했다. 그런데...여전히 동일한 에러가 발생한다. '명령줄 - 모든 옵션'에서도 WX- 플래그가 제대로 설정된 것을 확인했는데 여전히 동일하다. 잠깐 고민하다가..지금은 **빌드 성공이 목적**이므로 `#pragma warning(disable:4566)`으로 처리했다.

`Telegram.exe` 파일은 `$tdesktop\out\debug\` 폴더에 생성된다. 속성-디버깅-명령에 exe를 연결하면 디버깅 모드로 돌려볼 수 있다.