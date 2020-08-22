---
layout: post
title: 루비/jekyll 설치, bundle update
---

새 PC에서 jekyll로 만든 이 사이트([surinkim.github.io](https://github.com/surinkim/surinkim.github.io))를 clone하고 로컬에서 띄울 때 필요한 절차를 기록했다.


### 1.ruby 설치   
[RubyInstaller](https://rubyinstaller.org/downloads/)를 내려받아 설치한다. 오른쪽에 추천하는 버전이 소개돼있다. Ruby+Devkit 2.6.X(x64)를 설치했다.

### 2.jekyll 설치  
[여기를](http://jekyllrb-ko.github.io/) 참고해서 jekyll을 설치한다.

```bash
gem install bundler jekyll
```

해당 페이지에 따로 나오지 않았지만, jekyll 설치 후에는 `bundle update`를 실행해줘야 아래 2-2) 패키지 버전 문제가 발생하지 않는다.

#### 2-1) 패키지 수동 설치
아래처럼 `GemNotFound`에러가 나면 해당 패키지를 수동 설치해 준다.

```bash
PS D:\work\github_surinkim\surinkim.github.io> jekyll serve .
Traceback (most recent call last):
        12: from d:/Ruby26-x64/bin/jekyll:23:in `<main>'
        11: from d:/Ruby26-x64/bin/jekyll:23:in `load'
        ...
         2: from D:/Ruby26-x64/lib/ruby/2.6.0/bundler/spec_set.rb:85:in `materialize'
         1: from D:/Ruby26-x64/lib/ruby/2.6.0/bundler/spec_set.rb:85:in `map!'
D:/Ruby26-x64/lib/ruby/2.6.0/bundler/spec_set.rb:91:in `block in materialize': Could not find public_suffix-3.0.1 in any of the sources (Bundler::GemNotFound)

PS D:\work\github_surinkim\surinkim.github.io> gem install public_suffix -v 3.0.1
Fetching public_suffix-3.0.1.gem
Successfully installed public_suffix-3.0.1
Parsing documentation for public_suffix-3.0.1
Done installing documentation for public_suffix after 0 seconds
1 gem installed
```
#### 2-2) 패키지 버전 문제
다른 패키지들은 위처럼 수동 설치로 해결됐는데, `ffi` 같은 경우는 필요한 패키지 버전을, 로컬에 설치된 루비 버전에는 설치할 수 없다고 나온다.  이런;;
```bash
PS D:\work\github_surinkim\surinkim.github.io> jekyll serve .
        12: from d:/Ruby26-x64/bin/jekyll:23:in `<main>'
        ...
         1: from D:/Ruby26-x64/lib/ruby/2.6.0/bundler/spec_set.rb:85:in `map!'
D:/Ruby26-x64/lib/ruby/2.6.0/bundler/spec_set.rb:91:in `block in materialize': Could not find ffi-1.9.18-x64-mingw32 in any of the sources (Bundler::GemNotFound)
PS D:\work\github_surinkim\surinkim.github.io> gem install ffi -v 1.9.18
Fetching ffi-1.9.18-x64-mingw32.gem
ERROR:  Error installing ffi:
        The last version of ffi (= 1.9.18) to support your Ruby & RubyGems was 1.9.18. Try installing it with `gem install ffi -v 1.9.18`
        ffi requires Ruby version >= 2.0, < 2.5. The current ruby version is 2.6.6.146.
```
다행히 [bundle update](https://stackoverflow.com/questions/49485905/jekyll-install-with-ruby-2-5)로 해결할 수 있다는 글을 보고 실행했더니,
```bash
PS D:\work\github_surinkim\surinkim.github.io> bundle update
Fetching gem metadata from https://rubygems.org/..........
Fetching gem metadata from https://rubygems.org/.
Resolving dependencies...
Using public_suffix 4.0.5 (was 3.0.1)
Using addressable 2.7.0 (was 2.5.2)
...
Using ffi 1.13.1 (x64-mingw32) (was 1.9.18)
...
```
패키지들이 모두 업데이트 되면서 `ffi`도, 로컬에 설치된 루비 버전에 맞는 1.13.1로 업데이트가 됐다.

헌데, 지금까지는 `jekyll serve .` 명령만으로 실행이 됐는데, 이번에는 아래 에러가 뜬다.

```bash
PS D:\work\github_surinkim\surinkim.github.io> jekyll serve .
Traceback (most recent call last):
        10: from d:/Ruby26-x64/bin/jekyll:23:in `<main>'
		...
         1: from D:/Ruby26-x64/lib/ruby/2.6.0/bundler/runtime.rb:31:in `block in setup'
D:/Ruby26-x64/lib/ruby/2.6.0/bundler/runtime.rb:319:in `check_for_activated_spec!': You have already activated jekyll-sass-converter 2.1.0, but your Gemfile requires jekyll-sass-converter 1.5.2. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)
```

에러 메시지에 나와있는 대로 `bundle exec jekyll serve .`으로 실행하니 사이트가 잘 뜬다.  Gemfile을 수정하는 등의 방법으로 1.5.2를 명시해서 쓰면 해결이 되지 않을까 하는데.. 뭐, 단어 2개 더 타이핑하는 게 힘든 일도 아니고.. 이 정도면 됐다.