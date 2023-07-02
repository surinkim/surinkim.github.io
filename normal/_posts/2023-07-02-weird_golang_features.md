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

### 4. 변수명 첫 글자가 대문자면 public, 아니면 private
```go
type Message struct {
 Text string // public
 text string // private
}
```
Text는 현재 패키지 밖에서도 사용할 수 있다.

### 5. 함수의 반환값 위치
```go
func SumAndDiff(a int, b int) (int, int) { // int형 리턴값이 두 개인 함수 정의
	return a + b, a - b
}
```

위 함수의 반환값은 2개의 int로, 함수 이름 앞에 쓰지 않고 맨 뒤에 적는다.




> 참고 1: [7 Golang Features You Might Find Weird](https://betterprogramming.pub/7-golang-features-newbies-and-not-so-newbies-may-find-weird-e0542d079097)  
> 참고 2: [Weird Things About GOLANG [Part 1]](https://hackernoon.com/weird-things-about-golang-part-1-ob4z3y84)  



