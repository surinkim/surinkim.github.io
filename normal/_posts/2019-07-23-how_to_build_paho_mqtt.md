---
layout: post
title: paho mqtt c/cpp 빌드
---


### paho mqtt c
- 저장소: https://github.com/eclipse/paho.mqtt.c
- 빌드 방법  

``` cpp
# SSL=TRUE
# STATIC=TRUE
# paho.mqtt.c와 동일 레벨에 openssl 폴더가 있다고 가정한다.
mkdir build
cd build
cmake -G "Visual Studio 14 2015" -DOPENSSL_INCLUDE_DIR=../../openssl/include -DOPENSSL_LIB=../../openssl/lib -DOPENSSLCRYPTO_LIB=../../openssl/lib -DPAHO_BUILD_STATIC=TRUE -DPAHO_WINDOWS_BUILD_BIT="x86" -DPAHO_WITH_SSL=TRUE ..

```
`cmake` 빌드를 통해 생성된 솔루션 파일을 열고, `common_ssl_obj`, `pah-mqtt3as-static` 프로젝트를 차례대로 빌드하면 `paho-mqtt3as-static.lib`가 생성된다.


### paho mqtt cpp
- 저장소: https://github.com/eclipse/paho.mqtt.cpp

- 빌드 방법  

``` cpp
# SSL=TRUE
# STATIC=TRUE
mkdir build
cd build
cmake -G "Visual Studio 14 2015" -DPAHO_MQTT_C_INCLUDE_DIRS=../../paho.mqtt.c/src -DPAHO_MQTT_C_LIBRARIES=../../paho.mqtt.c/build/src/Debug/paho-mqtt3as-static.lib -DPATH_WITH_SSL=TRUE ..

```
`cmake` 빌드를 통해 생성된 솔루션 파일을 열고, `paho-cpp-objs`, `paho-mqttpp3-static` 프로젝트를 차례대로 빌드하면 `paho-mqttp3-static.lib`가 생성된다. 이제 필요한 곳에서 링크하고 사용하면 된다.

####  참고
> `openssl`은 1.0.X 버전대와 1.1.X 버전대의 바이너리 이름이 다르다. 
>  - 1.0.X: libeay32XX.dll, ssleay32XX.dll
>  - 1.1.X: libcryptoXX.dll, libsslXX.dll


> [여기서]([https://www.npcglib.org/~stathis/blog/precompiled-openssl/](https://www.npcglib.org/~stathis/blog/precompiled-openssl/)) openssl pre built 바이너리를 받을 수 있다.



