# Java 기본 문법: Static Keyword

### Static Keyword란 무엇일까?

자바에서의 모든 코드는 기본적으로 Class로 작성되어있다. Static의 개념과 static이 왜 필요한지를 이해하려면, 일단 class가 무엇인지부터 완전히 이해를 해야한다.

Class란 앞에서도 봤다시피 객체를 만들기 위한 뼈대와도 같다.

예를들어, Dog라는 Class안에 코카, 하늘이, 사랑이라는 Object가 존재한다고 생각해보자. 여기에서 코카, 하늘이, 사랑이는 실제로 존재하는 강아지들이지만, Dog라는 개념 자체는 보고 만질 수 있는 생물체가 아니라 "강아지"라는 개념 자체이다.

> 즉, static keyword를 사용하지 않은 일반 클래스들은, object를 생성하기 전까지는 실체가 존재하지 않는, object class의 멤버이다



하지만, 객체를 만들지 않고도 그 자체만으로도 존재해야 하는 것들이 있다. 이것들을 우리는 static class로 정의할 수 있다. Static keyword를 사용해서 정의한 것들은 해당 클래스를 활용해서 객체를 만들지 않더라도, 클래스로 직접 접근이 가능하다

한 마디로 정리하자면,

> Static은 Class의 멤버이고
>
> 나머지는 Object의 멤버들이다



### Static Keyword 사용법

Static은 Class의 멤버이고 나머지는 Object의 멤버이다 --> 이 부분을 코드로 표현을 해보자면

아래와 같이 정의된 Dog Class가 있을때

```java
public class Dog {
	static int population = 100; 
	int age = 0;
}
```



각각의 변수를 접근할라면 아래와 같이 접근해야 된다

```java
public class Test {

	public static void main(String[] args) {
    // Dog Class에서 바로 접근 가능
		System.out.println(Dog.population);
		
    // Dog Class로 객체를 만들었을때 객체를 통해 접근 가능
		Dog coca = new Dog();
		System.out.println(coca.age);

	}
}

```



### 언제 Static Keyword를 써야될까?

1. Main 메서드
2. 상수 혹은 클래스 당 하나만 유지하고 있으면 되는 값
3. 순수하게 기능만으로 정의되는 메서드 (Ex. 수학 함수)