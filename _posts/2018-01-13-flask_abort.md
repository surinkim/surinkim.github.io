---
layout: post
title: 플라스크 abort 변경 내용
---

Flask 0.12 이전에는 flask.abort.mapping 딕셔너리를 사용할 수 있었다.

사실 **abort**는 werkzeug의 Aborter 클래스 인스턴스다. 그런데, werkzeug 0.12에 abort()함수가 추가되면서, Aborter 클래스의 인스턴스 이름이 **_aborter**가 돼버렸다..(<a href="https://github.com/pallets/werkzeug/commit/9ab649fdc225037162a9d29be08648249c4588ab#diff-43a63db82587e91732eda181306d76c7" target="_blank">compare 링크 </a>)


또, 새로 추가된 abort() 함수는 고정 인수로 status를 사용한다.

```python
    def abort(status, *args, **kwargs):
```

그래서, 아래처럼 사용한 기존 코드도 수정이 필요한데, 이미 문서에서 status를 사용하는 것으로 명시한 상황이라 어쩔 수 없었던 것 같다.(<a href="https://github.com/pallets/werkzeug/pull/1003/files#diff-43a63db82587e91732eda181306d76c7R668" target="_blank">merge 링크 </a>)

```python
abort(code=400, description="Invalid destination name")
```

어쨌든, description을 얻거나 custom 핸들러 등을 등록하기 위해 **mapping** 딕셔너리가 필요하다면 이제 **_aborter**를 써야 한다.

다음은 /api 엔드 포인트를 호출하면 고의로 TypeError를 발생시키고, 커스텀 핸들러에서 500 에러를 json 형식으로 반환한다.

<script src="https://gist.github.com/surinkim/b9ffb01a395405ea601cc927085d7e4c.js"></script>


<hr>