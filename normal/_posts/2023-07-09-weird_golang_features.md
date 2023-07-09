---
layout: post
title: go의 낯선 특징들
---


처음 golang을 배울때 어색한 특징들...


### 1. 단축 할당문(Short Assignment Statement)
```go
areYouAString := "yes, i am string!!"
```
함수 내에서는 위와 같이 var를 생략하고 변수 선언과 값 할당을 동시에 할 수 있다.

<br>
### 2. 가져온 패키지는 반드시 사용해야 함.


```go
import (
	"fmt"
	"os" // 사용하지 않는 패키지
)
 
func main(){
	fmt.Println("Hello")
}
```

os 패키지를 사용하지 않았기 때문에 컴파일 에러가 발생한다.

```
imported and not used: "os"
```


<br>
### 3. 컬렉션 반복에 사용하는 range 함수의 반환 값은 2개

```go
import "fmt"

func main(){
	x := [4]string{"a", "b", "c", "d"}
	for i, value := range x {
		fmt.Printf("%d -> %s\n", i, value)
	}
}
```
위 코드에서 i에 index, value에 값이 반환된다. i를 사용할 일이 없다면 대신 `_`를 쓴다.


```bash
0 -> a
1 -> b
2 -> c
3 -> d
```

<br>
### 4. 변수명 첫 글자가 대문자면 public, 아니면 private
```go
type Message struct {
 Text string // public
 text string // private
}
```
Text는 현재 패키지 밖에서도 사용할 수 있다.

<br>
### 5. 함수의 반환값 위치
```go
func SumAndDiff(a int, b int) (int, int) { // int형 리턴값이 두 개인 함수 정의
	return a + b, a - b
}
```

위 함수의 반환값은 2개의 int로, 함수 이름 앞에 쓰지 않고 맨 뒤에 적는다.


<br>
### 6. 리시버
go는 `class`가 없으므로 메서드 정의를 할때 Receiver Parameter를 명시해서 별도로 선언하고, 메서드를 호출할 때 `리시버.메서드 이름()` 형태를 사용한다.
```go
type MyType string

// 리시버 매개변수 m MyType이 있기 때문에 
// sayHi는 MyType에 대한 메서드다.
func (m MyType) sayHi() {
	fmt.Println("Hi")
}
```

<br>
### 7. 타입 단언
인터페이스 타입에서 실제(concrete) 타입을 가져온다. 
다른 언어의 캐스팅 연산과 같은데 go에서는 타입을 맨 뒤에 표시하다보니 타입 단언 표기 역시 낯설다.

```go
package main

import "fmt"

func main() {
	var i interface{} = "hello"

	s := i.(string) // 타입 단언 - 성공
	fmt.Println(s)

	s, ok := i.(string) // 타입 단언 - 성공
	fmt.Println(s, ok)

	f, ok := i.(float64) // 타입 단언 - 실패
	fmt.Println(f, ok)

	f = i.(float64) // // 타입 단언 - 실패(panic)
	fmt.Println(f)
}

```


출력 결과  
```bash
hello
hello true
0 false
panic: interface conversion: interface {} is string, not float64

goroutine 1 [running]:
main.main()
	/tmp/sandbox2825551196/prog.go:17 +0x14a

Program exited.
```





> 참고 1: [7 Golang Features You Might Find Weird](https://betterprogramming.pub/7-golang-features-newbies-and-not-so-newbies-may-find-weird-e0542d079097)  
> 참고 2: [Type assertions](https://go.dev/tour/methods/15)



