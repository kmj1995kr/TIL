# Java 기본 문법: 클래스 (Class)

클래스란 쉽게 말해 <u>공통 된 특징을 가진 데이터들을 묶어서 관리하는 것이다</u>. 자바에서는 클래스도 하나의 타입이다 - 자바에서는 클래스를 선언 후 그 클래스를 타입으로 가지는 객채를 만들 수 있다.

이 클래스가 객체 지향 프로그래밍에서 가장 기초가 되는 개념 중 하나이다.

### 클래스 vs. 객체

**클래스:** 공통된 특징을 갖고 있는 데이터들을 하나의 단위로 묶어서 관리하는 것

**필드: **해당 클래스가 가질수 있는 속성들, 해당 클래스의 특징들을 말한다

### 클래스 및 객체 생성하기

1. 클래스를 정의한다
   - 이때까지 봤던 파일들과들 다르게 메인함수(`public static void main(String[] args)`) 에 넣는것이 아닌 일반 클래스 함수에 넣어 정의한다

```java
// Person1.java
package Section1;

public class Person1 {
	public String name; // field, data member
	public String number;
}
```



2. 정의한 클래스를 활용해서 새로운 객체를 생성한다
   - 앞에서 정의한 클래스를 데이터 타입처럼 활용하여 새로운 객체를 생성한다

  ```java
  // Code1.java
  package Section1;
  
  public class Code1 {
  
  	public static void main(String[] args) {
      // first라는 이름의 Person1 객체를 생성한다
      // 1. 생성 후 초기화 하기
      Person1 first; // 생성
      first = new Person1(); // 초기화 - 실제로 새로운 객체가 생성됨
      
      // 2. 생성과 초기화를 동시에 하기
  		Person1 first = new Person1();
  		
      // 생성된 객체의 필드 수정하기
  		first.name = "John";
  		first.number = "010-1234-1234";
  	}
  }
  ```



3. 생성한 객체의 필드를 수정한다

```java
// Code1.java
package Section1;

public class Code1 {

	public static void main(String[] args) {
    ...
    // 이름과 전화번호 수정하기
		first.name = "John";
		first.number = "010-1234-1234";
	}
}
```

