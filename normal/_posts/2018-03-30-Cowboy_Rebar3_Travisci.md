---
layout: post
title: Cowboy, Rebar3, Travis CI
---

얼랭 Cowboy, Rebar3(+ hex)로 간단한 웹 서버를 만들어 Travis CI를 연동했다.

Rebar3를 사용하면, 얼랭 프로젝트의 의존성 관리, 구성, 배포 파일 생성 등을 쉽게 할 수 있다. [hex](https://hex.pm)은 파이썬의 PyPI와 같은, 얼랭 패키지 관리자다.

Rebar3 설치와 실행 및 hex 사용법은 아래 글을 참고하면 어려울 건 없다.

 - [Building Your First Erlang App Using Rebar3](https://medium.com/erlang-central/building-your-first-erlang-app-using-rebar3-25f40b109aad)
 - [A rebar3 Cowboy REST app and a template](http://davekuhlman.org/rebar3-cowboy-rest-template.html)


몇 가지 문제가 있었는데, 우선

#### hex 사용을 위해 `rebar.config`에 아래 설정을 추가하면,
```config
{plugins, [rebar3_hex]}.
```
아래 에러가 발생했다.

```bash
$ rebar3 update
===> Fetching rebar3_hex ({pkg,<<"rebar3_hex">>,<<"4.1.0">>})
===> Downloaded package, caching at /home/hyun/.cache/rebar3/hex/default/packages/rebar3_hex-4.1.0.tar
===> Compiling rebar3_hex
===> Compiling _build/default/plugins/rebar3_hex/src/rebar3_hex_http.erl failed
_build/default/plugins/rebar3_hex/src/rebar3_hex_http.erl:14: can't find include lib "public_key/include/OTP-PUB-KEY.hrl"

===> Plugin rebar3_hex not available. It will not be used.

```

[이때는 `erlang-dev` 패키지를 추가로 설치해줘야 한다.](https://github.com/edgurgel/httpoison/issues/46)


#### 다음 문제는 hex로 cowboy를 설치하고 컴파일 했을 때다.
```bash
$ rebar3 compile
===> Verifying dependencies...
===> Fetching cowboy ({pkg,<<"cowboy">>,<<"2.2.2">>})
===> Downloaded package, caching at /home/hyun/.cache/rebar3/hex/default/packages/cowboy-2.2.2.tar
===> Fetching meck ({pkg,<<"meck">>,<<"0.8.9">>})
===> Downloaded package, caching at /home/hyun/.cache/rebar3/hex/default/packages/meck-0.8.9.tar
===> Fetching cowlib ({pkg,<<"cowlib">>,<<"2.1.0">>})
===> Downloaded package, caching at /home/hyun/.cache/rebar3/hex/default/packages/cowlib-2.1.0.tar
===> Fetching ranch ({pkg,<<"ranch">>,<<"1.4.0">>})
===> Downloaded package, caching at /home/hyun/.cache/rebar3/hex/default/packages/ranch-1.4.0.tar
===> Compiling cowlib
===> Compiling _build/default/lib/cowlib/src/cow_sse.erl failed
_build/default/lib/cowlib/src/cow_sse.erl:32: syntax error before: ':='

_build/default/lib/cowlib/src/cow_sse.erl:44: type event() undefined
```

hex로 cowboy 최신 버전인 2.2.2를 설치했는데, 2.0 부터는 Erlang/OTP 19 이상만 지원한다.
그래서, 시스템에 설치된 얼랭을 업그레이드 해야 한다.
[Erlang Solutions 저장소를 시스템에 추가해서 설치하면 쉽게 할 수 있다.](https://www.erlang-solutions.com/resources/download.html)


#### 마지막으로, 애플리케이션을 시작할 때 cowboy도 실행되도록 해야 한다.
자동으로 추가되지 않기 때문에, 런타임 에러가 발생한다.
프로젝트명.app.src 파일에 cowboy를 추가한다.
```bash
{application, cowboy_rebar_travis,
 [{description, "An OTP application"},
  {vsn, "0.1.0"},
  {registered, []},
  {mod, { cowboy_rebar_travis_app, []}},
  {applications,
   [kernel,
    stdlib,
    cowboy
   ]},
  {env,[]},
  {modules, []},

  {maintainers, []},
  {licenses, ["Apache 2.0"]},
  {links, []}
 ]}.

```


Travis-CI 실행은 별다를 게 없다.
유닛테스트 들어가고, 빌드 옵션 등도 포함되면 얘기가 다르겠지만,
지금 예제 정도는 아래 몇 줄로 끝이다.
```yml
language: erlang
otp_release:
  - 20.0
  - 19.2
```

[완성된 예제는 여기서 확인.](https://github.com/surinkim/cowboy_rebar_travis)


