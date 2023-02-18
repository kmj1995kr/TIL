# Java 기본문법: 조건문과 반복문 (Control Statement)

거의 대부분의 언어에서 가장 기초가 되는, 프로그램의 흐름을 통제하는 명령어를 제어문(Control Statement)라고 부른다.

그 중에서도 크게 **조건문(Conditional)**과 **반복문(loop)**이 자바에도 존재한다.

### 조건문 (Conditional)


#### If ~ Else
`if (condition) ~ else if (condition) ~ else (condition)`의 형태로 작성할 수 있다.

**간단한 조건문 예시**

```java
int age = 20;
  
if (n < 20) {
	System.out.println("Underage");
} else if (n == 20) {
  System.out.println("Congrats! You just became legal");
} else {
  System.out.println("Adult");
}
```

#### Switch ~ Case
`switch (Expression) ~ case (value)`의 형태로도 작성이 가능하다
- `Expression`의 값이 `value` 와 정확히 일치하는지만 비교 가능
	- `if ~ else` 와는 다르게 비교 연산자를 사용하여 범위안에 있는지 확인은 불가능
- `break`를 사용하여 `case` 문을 빠져나올수 있고, 사용하지 않을경우, `switch` 내부에 있는 다음 코드 라인들이 순차적으로 실행된다
- `default`를 사용하여 모든 다른 케이스에 대한 조건을 작성할 수 있다 (`else`)

**간단한 조건문 예시**
```java
int grade = 4;
int price = 7000;

switch(grade) {  
	case 1:  
        price += 1000;  
    case 2:  
        price += 1000;  
    case 3:
    case 4:
        price += 1000;  
        break;
	default:
		price += 500;
}

// grade = 1 => 10000원  
// grade = 2 => 9000원  
// grade = 3 or 4 => 8000원
// 기타 => 7500원
```


### 반복문 (Loop)

**For Loop 예시**

```java
for (int i = 0; i < grades.length; i++) {
			System.out.println("Grade " + (i+1) + ": " + grades[i]);
}
```

**While Loop 예시**

```java
while (i < grades.length) {
			System.out.println("Grade " + (i+1) + ": " + grades[i]);
			i++;
}
```




