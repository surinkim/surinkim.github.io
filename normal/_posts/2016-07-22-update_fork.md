---
layout: post
title: github에서 repository fork후, 업데이트
---

fork 저장소가 아닌 원래의 프로젝트 저장소를 upstream으로 등록. 
```bash
git remote add --track master upstream git://*git_repository_url*
```

원래의 프로젝트 저장소로부터 최신 내용을 받음.
```bash
git fetch upstream
```

master 브랜치
```bash
git checkout master
```

Rebase
```bash
git rebase upstream/master
```

fork 저장소에 push
```bash
git push origin master
```



