---
layout: post
title: QLatin1String vs QStringLiteral
---

## QLatin1String
Qt 함수가 매개 변수로, QString 이외에  QLatin1String도 받는다면, QLatin1String을 사용하는 것이 빠르다.

```c++
s.startsWith("Now")                  // 1)

s.startsWith(QLatin1String("Now"))   // 2) better
```

QString의 [startsWith 함수](https://doc.qt.io/qt-5/qstring.html#startsWith-3)는 const QString&, **`QLatin1String`** 등의 형식을 매개 변수로 받도록 오버로딩 되어있다. const char*를 받는 오버로딩은 없다.  

따라서, 1)번 코드에서는 const char* 에서 QString 으로 암시적 변환이 발생한다. QString의 내부 데이터 멤버인 QStringData가, *"Now"* 문자열을 담을 수 있을 만큼 충분한 크기로, malloc으로 할당되고 문자열 리터럴이 복사된다. 그리고, Qt에서 char*는 UTF-8, QString은 UTF-16으로 저장되므로, UTF-8에서 UTF-16 으로 변환도 발생한다.

2)번에서는 **`QLatin1String`** 형식을 인수로 넘긴다. 위에서 말했듯이, Qt에서 char* 는 UTF-8로 저장되는데, 대부분의 알고리즘은 UTF-8보다, ASCII나 latin1에서 훨씬 빠르다. **`QLatin1String`** 은 char*를 감싸면서 인코딩 형식만 지정된 얇은 래퍼다. 그래서, startsWith 처럼,  **`QLatin1String`**을 매개변수로 받는 함수에서는 변환 과정 없이, 원래 latin1 데이터 그대로 빠르게 처리가 가능하다.



## QStringLiteral
그런데, [setObjectName 함수](https://doc.qt.io/qt-5/qobject.html#objectName-prop)나 [QUrl 클래스 생성자](https://doc.qt.io/qt-5/qurl.html#QUrl-2)는 QString만 받는다.  
이럴 때는, **`QStringLiteral`** 을 사용할 수 있다. **`QStringLiteral`**을 사용하면 런타임이 아닌, 컴파일 타임에 QString을 생성한다. 따라서, 런타임 성능을 향상 시킬 수 있지만, 반대로 바이너리 크기와 메모리 오버헤드가 증가한다.  

이런 이유로, 함수에 과부하가 있는 경우, QString만 받는 함수에 **`QStringLiteral`** 대신, **`QLatin1String`** 타입을 넘겨서, 컴파일 타임이 아니라 런타임에 **`QLatin1String`**에서 QString의 암시적 변환이 발생하도록 하는 경우도 있다. 



### 결론은,  

- **`QLatin1String`** 을 먼저 떠올리자. **`QLatin1String`**을 쓰면 QString 객체 생성 및 문자열 복사/인코딩 변환 과정을 피할 수 있다.
- QString 타입만 허용하는 함수라면, 런타임 오버헤드가 없는 **`QStringLiteral`**을 생각하자.



#### 참고:  
[Qt Weekly #13: QStringLiteral](https://blog.qt.io/blog/2014/06/13/qt-weekly-13-qstringliteral/)  
[QStringLiteral explained - woboq](https://woboq.com/blog/qstringliteral.html)


