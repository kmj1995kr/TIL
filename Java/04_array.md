# Java 기본문법: 배열 선언 및 초기화

#### 배열(Array) 이란?

가장 많이 쓰이고 다양하게 활용될 수 있는 자료구조 중 하나인 배열! Java에서는 **동일한 타입의 데이터**들을 묶어서 저장하기 위해 배열 (Array)을 활용한다.

자바에서는 배열을 **선언, 생성, 초기화** 하는 과정을 거쳐 비로소 배열이 만들어진다

#### 배열 선언

생성된 배열을 다루게 될 참조 변수를 설정 - 이때 실제로 배열이 저장될 메모리나 주소가 할당되는것은 아니다!

```java
// 배열 선언
int[] arr1;
int arr2[];
```



#### 배열 생성

배열의 크기를 직접 지정해 줌으로써 실제로 값을 저장할 공간 생성

- long, double, integer, Long, Double, String등의 타입을 사용할 수 있음
- 사용되는 타입에 따라 배열의 값이 특정 값으로 초기화 됨

```java
// 배열 생성
arr1 = new int[5];
  
// 배열 선언 + 생성
int[] arr3 = new int[5];
```



#### 배열의 값을 초기화

```java
// 이미 선언 + 생성된 배열의 값 초기화
for (int i=0, i<5, i++)
  arr1[i] = i

// 배열 선언 + 생성 + 초기화
int[] arr4 = {1, 2, 3, 4, 5};
int[] arr5 = new int[] {1, 3, 5, 7, 9};
```



출처:

https://m.blog.naver.com/alcmskfl17/221731876315

https://ifuwanna.tistory.com/231

https://joy-baek.tistory.com/47

