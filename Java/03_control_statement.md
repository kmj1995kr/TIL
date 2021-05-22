# Java 기본문법: 조건문과 반복문 (Control Statement)

거의 대부분의 언어에서 가장 기초가 되는, 프로그램의 흐름을 통제하는 명령어를 제어문(Control Statement)라고 부른다.

그 중에서도 크게 **조건문(Conditional)**과 **반복문(loop)**이 자바에도 존재한다.

### 조건문 (Conditional)

`if (condition) ~ else if (condition) ~ else (condition)`의 형태로 작성할 수 있다.

**간단한 조건문 예시**

```java
int age = 20
  
if (n < 20) {
	System.out.println("Underage");
} else if (n == 20) {
  System.out.println("Congrats! You just became legal");
} else {
  System.out.println("Adult");
}
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

