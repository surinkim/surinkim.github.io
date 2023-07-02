---
layout: post
title: 정규표현식
---



### 정규 표현식으로 C++ 클래스 이름 표현하기

유효한 C++ 클래스 이름을 정규 표현식으로 나타내자면 아래처럼 쓸 수 있다.
  
    ^[A-Za-z_][A-za-z0-9]*

 - **^**(caret): string 시작이 일치해야 함을 뜻한다. 여기서는 대, 소문자 구분없이 a에서 z 사이의 문자 혹은 _(under-score)로 시작하는 것을 매칭한다.
 >[^abc] :  caret이 대괄호 안에 쓰이는 경우는 a, b, c를 제외한 문자를 매칭한다.

- **E***: 검색시에 사용하는 wild-card와 같은 의미로 쓴다. 0번 또는 여러번 매칭되는 것을 의미한다. 자주 오용되는 경우로, '1개 이상의 white-space로 끝나는 문자열'을 매칭시킬 때, `\s*$`를 사용하는데, 이는 결국 '0개 또는 여러 개의 white-space로 끝나는 문자열'을 의미하므로, 모든 문자열이 매칭된다. 올바르게 사용하려면 `\s+$` 처럼 사용해야 한다.



#### c++ sample code
```c++
    std::regex pattern( "^[A-Za-z_][A-Za-z0-9]*" );
    std::cout << "Is Match : " << std::regex_match( "12",  pattern ); //Is Match : 0
    std::cout << "Is Match : " << std::regex_match( "_12", pattern ); //Is Match : 1
    std::cout << "Is Match : " << std::regex_match( "*A",  pattern ); //Is Match : 0
    std::cout << "Is Match : " << std::regex_match( "AB&", pattern ); //Is Match : 0
```

### 0부터 99까지의 수로 시작하고 끝나는 문자열

아래 4개의 정규 표현식은 모두 동일하게 0부터 99까지의 수로 시작해서 끝나는 문자열을 나타낸다.
 
    //method 1
    ^[0-9]{1,2}
    
    //method 2
    ^\d{1,2}$

	//method 3
	^\d\d{0,1}$
    
    //method 4
    ^\d\d?$


- method 1

    **{}**: quantifier, `x{1,2}`는 x가 1번 이상, 2번 이하로 나타나야 매칭되는 것을 의미.

- method 2

    **\d**: [0-9]와 동일 의미.
    **E$**: 문자열의 끝이 E로 끝나야 함을 의미.

- method 3

    시작은 숫자 1개, 끝은 숫자가 없거나 1개.

- method 4
    
    **?**: {0,1}과 같은 의미. 
    문자열 시작은 숫자로 시작하며, 이어서 숫자가 0번 혹은 1번 나오고 종료하는 문자열을 의미한다. 

### 특정 문자열 찾기

 - `letter|mail`

`|`은 or를 의미. 따라서 mail 이나 letter를 포함하는 문자열이 매칭됨.

```c++
//qt
QRegularExpression re("letter|mail");
qDebug() << re.match("email").hasMatch();       // true
qDebug() << re.match("mailbox").hasMatch();     // true
qDebug() << re.match("mail").hasMatch();        // true
qDebug() << re.match("letters").hasMatch();     // true

//c++11
std::regex pattern( "letter|mail" );
std::cout << std::regex_search( "email", pattern ) << std::endl;    // 1
std::cout << std::regex_search( "mailbox", pattern ) << std::endl;  // 1
std::cout << std::regex_search( "mail", pattern ) << std::endl;     // 1
std::cout << std::regex_search( "letters", pattern ) << std::endl;  // 1
```
> **Note**
>
>`std::regex_match`는 전체 입력이 모두 매칭될 때만 true를 반환한다. 
>`std::regex_search`는 입력의 일부분만 매칭되도 true를 반환한다.
>따라서, 위 코드에서 `std::regex_match`를 사용했다면 "mail"과 비교한 경우만 true고, 나머지는 false다.  [StackOverFlow](http://stackoverflow.com/questions/26696250/difference-between-stdregex-match-stdregex-search)


- `\b(letter|mail)\b`

`()`은 capture하려고 하는 부분을 명시.  소괄호로 묶음으로써 더 복잡한 정규 표현식을 사용할 수 있다.
`\b`는 단어의 시작과 끝을 매칭하는 word boundary를 뜻함.
```c++
//qt
QRegularExpression re("\\b(letter|mail)\\b");
qDebug() << re.match("email").hasMatch();       // false
qDebug() << re.match("mailbox").hasMatch();     // false
qDebug() << re.match("mail").hasMatch();        // true
qDebug() << re.match("letters").hasMatch();     // false
qDebug() << re.match("letter").hasMatch();      // true

//c++11
std::regex pattern( "\\b(letter|mail)\\b" );
std::cout << std::regex_search( "email", pattern ) << std::endl;    // 0
std::cout << std::regex_search( "mailbox", pattern ) << std::endl;  // 0
std::cout << std::regex_search( "mail", pattern ) << std::endl;     // 1
std::cout << std::regex_search( "letters", pattern ) << std::endl;  // 0
std::cout << std::regex_search( "letter", pattern ) << std::endl;   // 1
```

- `&(?!amp;)`

    `(?!XX)` :  negative lookahead. XX를 제외한 패턴을 매칭함. `&(?!amp;)`는 &를 찾되, 뒤에 amp;가 없는 패턴을 매칭한다는 의미. 

- Eric과 Eirik을 찾는 경우

    `\b(Eric|Eirik)\b` : Ericsson 같은 문자열을 제외하기 위해서 `\b`(word boundary) 필요.

    `\bEi?ri[ck]\b` : Eric과 Eirik이 매칭되지만, Erik, Eiric 같은 문자열도 매칭된다.



[참고 1) QT QRegExp](http://doc.qt.io/qt-4.8/qregexp.html)  
[참고 2) regex101.com/](https://regex101.com/)
