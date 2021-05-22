# Java 기본문법: 변수 (Variables)

### 변수의 타입

| 원시 타입 (Primitive Type)                                   | 참조 타입 (Reference Type)                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - byte<br />- short / long<br />- int<br />- double<br />- float<br />- char<br />- boolean<br /> | - String<br />- Scanner<br />- Random<br />- int[]<br />- String[]<br />- object |

### 기본적인 변수 선언 문법

- 지역 변수 (main 함수 안): `<type> <변수_이름> = <값>` 의 형태로 변수를 선언할 수 있다
- 전역 변수 (main 함수 밖): static 키워드를 붙여서 전역 변수를 선언 할 수 있다 

```java
// main 함수 밖에서 변수 선언
static int num1 = 3
  
public static void main(String[] args) {
  // main 함수 안에서 변수 선언
  int num2 = 5;
}
```



### 변수 계산 과정

다른 타입을 가진 변수들이 계산되는 과정에서 자바는 다양한 타입에 형변환을 진행해서 결과값을 계산한다

- left associativity: 왼쪽부터 오른쪽의 순서로 계산
- str + int를 할때는 자동으로 int를 str으로 변환해서 계산한다

```java
public static void main(String[] args) {
  int num1 = 2;
  int num2 = 3;
  
  System.out.println(num1 + num2) // 5
 	System.out.println("Num1 value: " + num1) // Num1 value: 2
  System.out.println("Num1 value: " + num1 + num2) // Num1 value: 25
  System.out.println("Num1 value: " + (num1 + num2)) // Num1 value: 7
}
```



### 변수의 적용 스코프

특정 변수를 어디에서 사용할 수 있는지(적용 범위)를 **스코프**라고 하는데, 변수가 선언된 위치에 따라서 다른 스코프를 가진다.

- 메서드 내부 (블록 안에서) 선언된 변수 --> 해당 메서드 안에서만 사용 가능 (**블록 스코프**)
- 메서드 외부 (클래스 내부)에서 선언된 변수 --> 클래스 내에서 사용 가능 (**전역 스코프**)



### input을 입력받는 방법

변수를 입력해주는 방법도 있지만, 사용자로 부터 input을 받아야 되는 상황이 많이 있다. Java에서는 input을 입력 받기 위해 다양한 방법을 사용할 수 있는데 그 중 가장 간단한 방법 중 하나인 Scanner를 사용해서 input을 받을 수 있다.

어떤 타입의 데이터를 입력받을 지에 따라 다른 메서드를 활용하여 적절하게 데이터를 받아올 수 있다.

**정수 입력 받기**

- `Scanner.nextInt()`

```java
// 스캐너 import 해오기 
import java.util.Scanner
  
public class Code {
  
  public static void main(String[] args) {
    Scanner kb = new Scanner( System.in ); // 새로운 스캐너 생성
    int input = kb.nextInt(); // 입력받은 정수를 변수에 할당
    kb.close(); // 스캐너 사용이 완료되면 스캐너를 종료하기
  }
  
}
```



**문자열 입력 받기**

- `scanner.next()`: 공백을 기준으로 한 단어씩 끊어서 읽어오기

