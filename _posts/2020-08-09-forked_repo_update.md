---
layout: post
title: fork한 저장소 업데이트(in git bash)
---


자주 쓰지 않다보니 매번 까먹는 명령..  

fork한 저장소에서 아래 명령으로 remote 저장소를 확인한다.
```bash
$ git remote -v
origin  https://github.com/surinkim/libsourcey.git (fetch)
origin  https://github.com/surinkim/libsourcey.git (push)
upstream        https://github.com/sourcey/libsourcey.git (fetch)
upstream        https://github.com/sourcey/libsourcey.git (push)
```

지금은 upstream에, fork한 원본 repo가 이미 추가돼있는데, 만약 아직 추가하지 않았다면 `git add`로 추가한다.
```bash
$ git remote -v
origin  https://github.com/surinkim/libsourcey.git (fetch)
origin  https://github.com/surinkim/libsourcey.git (push)

$ git remote add upstream https://github.com/sourcey/libsourcey.git

$ git remote -v
origin  https://github.com/surinkim/libsourcey.git (fetch)
origin  https://github.com/surinkim/libsourcey.git (push)
upstream        https://github.com/sourcey/libsourcey.git (fetch)
upstream        https://github.com/sourcey/libsourcey.git (push)
```

`fetch`로 upstream repo의 최신 내용을 가져온다.
```bash
hyun@hyun-PC MINGW64 /d/Code/libsourcey (master)
$ git fetch upstream
remote: Enumerating objects: 158, done.
remote: Counting objects: 100% (158/158), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 306 (delta 155), reused 158 (delta 155), pack-reused 148
Receiving objects: 100% (306/306), 112.74 KiB | 378.00 KiB/s, done.
Resolving deltas: 100% (188/188), completed with 111 local objects.
From https://github.com/sourcey/libsourcey
 * [new branch]        bugfix/libuv -> upstream/bugfix/libuv
 ... 
```

upstream의 master branch를 로컬 master branch에 merge한다.
```bash
hyun@hyun-PC MINGW64 /d/Code/libsourcey (master)
$ git merge upstream/master
Updating 48b06a1c..98df3c31
Fast-forward
 .gitattributes                                     |    16 +
 BUILD.md                                           |     9 +-
 Dockerfile                                         |    11 +-
 LibSourcey.cmake                                   |   804 +-
 Makefile                                           |    24 +
 README.md                                          |    30 +-
 ...

```

이제, origin에도 `push`해주면 끝이다.  
```bash
$ git push origin master
```


다음으로, [gitflow](https://danielkummer.github.io/git-flow-cheatsheet/)에서 release할 때인데,  
```bash
$ git flow releae start 1.2.0
$ git flow release publish 1.2.0
$ git flow release finish 1.2.0
$ git push origin master
$ git push origin develop
$ git push origin --tags
```

이건.. [fork한 gist](https://gist.github.com/surinkim/66242959c18ce9b63836e04dc9679ef7)를 보는 게 나을거 같고, 요즘은 리눅스 쓸 일도 거의 없으니까, 계속 CLI 고집하지 말고 [Fork](https://git-fork.com/)나 [SmartGit](https://www.syntevo.com/smartgit/), [GitHub Desktop](https://desktop.github.com/) 같은 GUI 툴도 써보고 익숙해져야겠다.  







