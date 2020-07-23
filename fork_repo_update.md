---

layout: post

title: git_fork_reposity_update

---

  
  
 git 명령어를 까먹지 않으려고 일부러 git bash를 쓰고 있는데, 이렇게 하더라도 결국은 자주 쓰는 패턴이 아니면 까먹고 검색하고, 다시 까먹고 검색하는 일이 잦다.

그 중에 하나가 fork한 repository를 업데이트 할 때다. 그래도 이제는 `git remote -v`로 origin, upstream 정보 확인하고 추가해야 된다는 건 어렴풋이... 떠오르기는 한다. 다행이다..

먼저, 현재 저장소의 remote 정보를 확인한다.

```bash
$ git remote -v
origin  https://github.com/MY_FORKED_REPO.git (fetch)
origin  https://github.com/MY_FORKED_REPO.git (push)
``` 

여기에 원본 저장소를 upstream으로 추가한다. 

다음으로... 

 

 

`vcpkg`는 **리눅스도 지원하는 c++ 전용 패키지 매니저**라는 큰 의의가 있고, 편리한 점도 많다. 하지만, NuGet처럼 비주얼 스튜디오에 통합되지 않았고, 특정 버전을 지정해서 설치하기 어렵다는 몇 가지 약점도 있다. 개인적으로, 실무에서 vcpkg 쓰는 걸 주저했던 큰 이유는 '의존성 설명의 어려움' 때문이었다.

  

예로, 파이썬은 [venv](https://docs.python.org/ko/3/tutorial/venv.html)로 프로젝트별 독립 환경을 구성하고, 필요한 패키지를 설치한 다음,

```bash

pip freeze > requirements.txt

```

  

위 명령으로 이 프로젝트에 필요한 의존성만 뽑아낼 수 있다.

이제 이 파일만 git에 올려두면, 빌드 pc나 동료 자리에서는

```bash

pip install -r requirements.txt

```

이렇게 필요한 의존성을 설치할 수 있다.

  

vcpkg로는 마땅한 방법을 찾지 못했다.

[작년 7월에 해당 feature에 대한 요청](https://github.com/microsoft/vcpkg/issues/4935)이 올라왔는데, 마지막 댓글을 봐서는 금방 추가될 것 같진 않다.

> We have Plans for this, but we need to do quite a bit of design and engineering work, so it's unlikely to come soon.

  

그렇다고, 대안이 아주 없는 건 아닌데...

```bash

vcpkg integrate project

```

  

위 명령을 쓰면 현재 설치되어 있는 패키지 정보를 아래와 같이 NuGet 참조 파일로 만들어 주기는 한다.

```bash

C:\Users\hukim

> vcpkg integrate project

Created nupkg: E:\vcpkg\scripts\buildsystems\vcpkg.E.vcpkg.1.0.0.nupkg

  

With a project open, go to Tools->NuGet Package Manager->Package Manager Console and paste:

Install-Package vcpkg.E.vcpkg -Source "E:\vcpkg\scripts\buildsystems"

```

  

그렇지만, 이건 특정 프로젝트의 의존성이 아니라 로컬에 설치된 모든 패키지 정보이므로, 수정하지 않으면, 프로젝트에 불필요한 패키지마저 설치할 수 있다.

  

그래서, [vcpkg 문서](https://docs.microsoft.com/ko-kr/cpp/build/vcpkg?view=vs-2019)에 아래와 같이 설명한다.

  

> ### 프로젝트 단위

> 활성 vcpkg 인스턴스에서 버전과 다른 라이브러리의 특정 버전을 사용해야 하는 경우 다음 단계를 따르세요.

>1. vcpkg의 새 클론을 생성합니다.

>2. 필요한 버전을 가져오도록 라이브러리의 프로필을 수정합니다.

>3.  **vcpkg install [library]**를 실행합니다.

>4.  **vcpkg integrate project**를 사용하여 프로젝트 단위로 해당 라이브러리를 참조하는 NuGet 패키지를 만듭니다.

  

결국, 패키지의 특정 버전이나 프로젝트에 필요한 패키지만 기술하려면, vcpkg를 하나 더 클론하고 기존 vcpkg의 `portfile`(한글 문서를 보면 '프로필'이라고 되어 있는데, [원문](https://docs.microsoft.com/en-us/cpp/build/vcpkg?view=vs-2019)은 `portfile`이다.)을 수정해서 `vcpkg integrate project` 명령으로 NuGet 패키지를 뽑아내야 한다. 이게 잘되더라도 다른 위치의 pc와 공유하려면 어딘가에 NuGet 패키지도 올려둬야 한다;;

  

이쯤되면, *'난 vcpkg 아니면 안 할래'* 같은 아집이 아니라면, 그리고 사용하려는 라이브러리가 [NuGet 갤러리](https://www.nuget.org/)에 이미 올라가 있다면(설사 없더라도, 직접 빌드가 가능하다면 private Nuget 저장소를 운영해도 된다.), 당분간은 고민 없이 NuGet을 쓰는 게 몸과 마음이 편할 것 같다.