*** 해당 글은 Effective Java 아이템1의 내용을 발췌하여 정리하고 저자(본인)의 의견을 덧붙인 내용입니다*

### 생성자란?
> 특정 클래스에 해당하는 객체 인스턴스를 생성함과 동시에, 인스턴스 변수를 원하는 값을 초기화 할 수 있도록 해주는 메서드
> 자바에서는 생성자(constructor)의 이름은 해당 클래스의 이름과 같아야 한다
> *(출처: https://www.tcpschool.com/java/java_methodConstructor_constructor)*

생성자가 받는 인자의 갯수 또는 타입에 따라 여러 생성자를 만들어 사용할수 있으며, 생성자를 지정하지 않을 경우 자바에서는 아무 변수도 초기화 하지 않는 기본 생성자를 만들어준다.


#### 예제
```java
public Integer(int value) {
	this.value = value;
}
```

### 정적 팩터리 메서드란?

> 특정 클래스 내부에 선언되어 있는 메서드로, 해당 클래스의 인스턴스를 반환하는 메서드이다
> 예) Integer class 안에 선언되어 있는 정적 팩터리 메서드는 Integer type의 객체를 반환한다

### 예제
```java
public static Integer valueOf(int i) {
	if (i >= IntegerCache.low && i <= IntegerCache.high)
		return IntegerCache.cache[i + (-IntegerCache.low)];
	return new Integer(i);
}
```

### 생성자 vs. 정적 팩터리 메서드
위의 두 에제 모두 `int` 타입의 값을 받아 `Integer` 타입의 값을 리턴해주지만, 두 방식 모두 각각의 장단점이 존재한다. 그 중, 자바를 사용할때 흔히 사용하는 생성자를 사용하는 것 외에 정적 팩터리 메서드를 사용하는 것의 장점 5가지에 대해 알아보자

#### 1. 이름을 가질 수 있다
생성자는 무조건 클래스 자체와 같은 이름을 가지고 있어야 하지만, 정적 팩터리 메서드는 목적에 맞는 이름을 부여할 수 있다.

#### 2. 호출될 때마다 인스턴스를 새로 생성하지는 않아도 된다

#### 3. 반환 타입의 하위 타입 객체를 반환할 수 있는 능력이 있다

#### 4. 입력 매개변수에 따라 매번 다른 클래스의 객체를 반환할 수 있다