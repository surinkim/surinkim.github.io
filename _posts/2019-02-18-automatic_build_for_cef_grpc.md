---
layout: post
title: gen-cef-vsproj, gen-grpc-vsproj
---

`cef`를 한 번 빌드하려면, [CEF Prebuilt](http://opensource.spotify.com/cefbuilds/index.html) 사이트에서 다운로드, 압축 해제, CMake 빌드, `libcef_dll_wrapper` 빌드까지 손이 많이 간다.  
그래서, 가져올 Standard Distribution 버전 파일 링크만 입력해주면, 위의 동작을 자동으로 처리하는 배치 파일을 만들었다.

https://github.com/surinkim/gen-cef-vsproj

아래처럼 쓰면 된다.
```bash
.\Start.bat http://opensource.spotify.com/cefbuilds/cef_binary_3.3626.1882.g8926126_windows32.tar.bz2
```

`grpc`도 복잡하다. 아래 배치 파일은 gen-cef-vsproj와 비슷하게 동작한다.

https://github.com/surinkim/gen-grpc-vsproj

[grpc Tags](https://github.com/grpc/grpc/tags)에서 가져올 태그 번호를 확인한 후, 아래와 같이 입력한다.

```bash
.\AllInOne.bat v1.17.2
```

> grpc는 [vcpkg](https://github.com/Microsoft/vcpkg/tree/master/ports)에서 지원하지만, cef는 아직 포함돼있지 않다. 그래서 이렇게 아까운 시간을...