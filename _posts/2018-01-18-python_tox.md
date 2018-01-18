---
layout: post
title: 파이썬 Tox
---


Tox는 파이썬의 테스트 자동화, 표준화를 위한 도구다.  Tox를 사용하면,

- **다양한 파이썬 버전에서 패키지가 제대로 설치되는지 확인**
- **선택한 테스트 툴과 설정을 사용해서 자동으로 테스트 실행**
- **CI와 통합**

이런 것들을 할 수 있다.  

여기서는 Tox에서 pytest 실행 방법을 정리한다.
pytest 확장인 pytest-cov, pytest-flake8도 사용해본다.

### hello_flask.py
먼저, virtualenv로 dev_tox 환경을 만들고, hello_flask.py 플라스크 소스를 추가했다.

{% highlight python linenos %}
# hello_flask.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api')
def my_microservice():
    return jsonify({'Hello': 'World!'})


if __name__ == '__main__':
    app.run()

{% endhighlight %}


/api 엔드포인트를 호출하면, json으로 Hello World를 반환하는 심플한 서버다.

```bash
$ curl localhost:5000/api 
{                         
  "Hello": "World!"       
}                         
```

### test_hello_flask.py
이제, hello_flask를 테스트 하기 위한 모듈, test_hello_flask.py를 만든다.

{% highlight python linenos %}
# -*- coding: utf-8 -*-
# test_hello_flask.py
import unittest
import json
import sys
from hello_flask import app as _app


class TestApp(unittest.TestCase):
    def test_help(self):

        app = _app.test_client()
        hello = app.get('/api')

        if (sys.version_info > (3, 0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode("utf8"))

        self.assertEqual(body['Hello'], 'World!')


if __name__ == '__main__':
    unittest.main()

{% endhighlight %}

15 ~ 열여덟 라인은 2.X과 3.X 버전의 str() 함수 원형이 다르기 때문에 추가했다.
(아래에서 Tox로 테스트할 때, 2.7과 3.6 버전을 사용한다.)

pytest로 테스트가 성공하는지 먼저 확인해 보자.
```bash
(dev_tox) $ pytest
============================= test session starts =============================
platform win32 -- Python 3.6.3, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: D:\Code\python_dev\dev_tox\flask, inifile:
plugins: flake8-0.9.1, cov-2.5.1
collected 1 item

test_functional_01.py .                                                  [100%]

========================== 1 passed in 0.22 seconds ===========================
```

### Tox
이제 Tox를 사용할 차례다. `pip install tox`로 패키지를 설치하자.  
Tox를 실행하려면, tox.ini와 setup.py가 필요하다. setup.py의 내용은, 여기서 중요하지 않으므로, 아래처럼 최소한으로 했다.

{% highlight python linenos %}
from setuptools import setup


setup(name='hello_flask',
      version='0.1')

{% endhighlight %}

tox.ini에는 테스트를 실행할 파이썬 버전, 의존성, 테스트 명령 등을 적어둔다.

```ini
[tox]
envlist=py27,py36
[testenv]
deps=flask
     pytest
commands=pytest
```

위와 같이, envlist에 파이썬 버전, deps에 의존성, commands에 테스트 명령을 적어준다. envlist에 기술한 파이썬 버전 2.7과 3.6은 시스템에 미리 설치해둬야 한다.

작성이 완료됐으면 tox 명령으로 실행한다.

```console
(dev_tox) $ tox
GLOB sdist-make: D:\Code\python_dev\dev_tox\flask\setup.py
py27 recreate: D:\Code\python_dev\dev_tox\flask\.tox\py27
py27 installdeps: flask, pytest
py27 inst: D:\Code\python_dev\dev_tox\flask\.tox\dist\hello_flask-0.1.zip
py27 installed: attrs==17.4.0,click==6.7,colorama==0.3.9,Flask==0.12.2,funcsigs==1.0.2,hello-flask==0.1,
itsdangerous==0.24,Jinja2==2.10,MarkupSafe==1.0,pluggy==0.6.0,py==1.5.2,pytest==3.3.2,six==1.11.0,Werkze
ug==0.14.1
py27 runtests: PYTHONHASHSEED='435'
py27 runtests: commands[0] | pytest
============================= test session starts =============================
platform win32 -- Python 2.7.14, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: D:\Code\python_dev\dev_tox\flask, inifile:
collected 1 item

test_functional_01.py .                                                  [100%]

========================== 1 passed in 0.16 seconds ===========================
py36 recreate: D:\Code\python_dev\dev_tox\flask\.tox\py36
py36 installdeps: flask, pytest
py36 inst: D:\Code\python_dev\dev_tox\flask\.tox\dist\hello_flask-0.1.zip
py36 installed: attrs==17.4.0,click==6.7,colorama==0.3.9,Flask==0.12.2,hello-flask==0.1,itsdangerous==0.
24,Jinja2==2.10,MarkupSafe==1.0,pluggy==0.6.0,py==1.5.2,pytest==3.3.2,six==1.11.0,Werkzeug==0.14.1
py36 runtests: PYTHONHASHSEED='435'
py36 runtests: commands[0] | pytest
============================= test session starts =============================
platform win32 -- Python 3.6.3, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: D:\Code\python_dev\dev_tox\flask, inifile:
collected 1 item

test_functional_01.py .                                                  [100%]

========================== 1 passed in 0.24 seconds ===========================
___________________________________ summary ___________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)

D:\Code\python_dev\dev_tox\flask
(dev_tox) $
```
결과와 같이, 각 파이썬 버전 별 환경에 의존성을 설치하고 배포 파일을 생성한 다음, 테스트를 실행해준다.

### pytest-cov, pytest-flake8
이번에는 테스트에 pytest-cov, pytest-flake8도 추가해 보자.

- **pytest-cov**: pytest의 coverage 플러그인. 코드 커버리지 검사.
- **pytest-flake8**: pytest의 flake8 플러그인. 컨벤션이 PEP8을 준수하는지 검사.

tox.ini의 의존성과 명령에 해당 도구를 추가한다.
```ini
[tox]
envlist=py27,py36
[testenv]
deps=flask
    pytest
    pytest-cov
    pytest-flake8
commands=pytest -v --cov --flake8
```
커버리지 측정과 컨벤션 검사가 추가된 테스트 결과를 볼 수 있다.

```console
(dev_tox) $ tox
...
hello_flask.py SKIPPED                                                   [ 25%]
setup.py SKIPPED                                                         [ 50%]
test_hello_flask.py PASSED                                               [ 75%]
test_hello_flask.py::TestApp::test_help PASSED                           [100%]

---------- coverage: platform win32, python 2.7.14-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
hello_flask.py            6      1    83%
test_hello_flask.py      15      3    80%
-----------------------------------------
TOTAL                    21      4    81%


===================== 2 passed, 2 skipped in 0.32 seconds =====================
...

hello_flask.py SKIPPED                                                   [ 25%]
setup.py SKIPPED                                                         [ 50%]
test_hello_flask.py SKIPPED                                              [ 75%]
test_hello_flask.py::TestApp::test_help PASSED                           [100%]

----------- coverage: platform win32, python 3.6.3-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
hello_flask.py            6      1    83%
test_hello_flask.py      15      2    87%
-----------------------------------------
TOTAL                    21      3    86%


===================== 1 passed, 3 skipped in 0.33 seconds =====================
___________________________________ summary ___________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)

```


> **참고**  
pytest-flake8은 디폴트 로그 레벨이 DEBUG라서 warning 하나만 발생해도 어마무시한 로그가 출력된다. 뭔가 이상하다 싶으면, `flake8` 명령만 실행해서 warning을 먼저 해결한 다음,pytest-flake8을 실행하는게 좋다. [디폴트 로그 레벨을 WARN으로 설정한 PR](https://github.com/tholo/pytest-flake8/pull/43/files)이 5일전에 올라왔으니 조만간 해결되지 싶다.


<hr>
