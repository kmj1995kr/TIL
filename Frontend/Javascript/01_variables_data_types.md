# Javascript 기초 문법 1: 변수 , 데이터 타입, 연산자

### 변수 선언하기

#### 변수를 선언하는 다양한 문법

Javascript에는 변수를 선언하는 문법이 여러가지가 존재하는데, 그 이유 중 하나가 변수를 1) 선언하고 2) 할당하는 행위가 나눠져서 처리되기 때문이다.

- **Declaration** (선언): 변수 (껍데기) 생성하는 것
- **Assignment** (할당): 선언된 변수에 실제 값을 저장하는 것
- **Initialization** (초기화): 변수에 처음에 값을 저장하는 시점 또는 행위

```javascript
// 선언과 할당을 개별적으로 하는 코드
// 1. 선언
let a
// 2. 할당
a = 1 // 초기화 시점

// 선언과 할당을 동시에 하는 코드
let b = 2 // 초기화 시점
```



#### var vs. const vs. let

`var`: ES6 이전에 쓰였던 유일한 변수 선언법으로 ES6 이후로는 사용이 권장되지 않고 있다

`const`: constant의 줄임말로, 변하지 않는 값을 저장할때 주로 사용되므로 재선언, 재할당이 둘다 허용되지 않는다

`let`: 재선언은 불가능하지만 재할당은 가능하다

|                 | const                              | let                              | var                            |
| --------------- | ---------------------------------- | -------------------------------- | ------------------------------ |
| 재선언 / 재할당 | 재선언: 불가능<br />재할당: 불가능 | 재선언: 불가능<br />재할당: 가능 | 재선언: 가능<br />재할당: 가능 |
| 스코프**        | 블럭 스코프                        | 블럭 스코프                      | 함수 스코프                    |



위와 같은 차이점을 코드로 봤을때는 이런 형태이다

```javascript
const a = 1
const a = 2 // 재선언: 에러
a = 3 // 재할당: 에러

let b = 1
let b = 2 // 재선언: 에러
b = 3 // 재할당: 가능

var c = 1
var c = 2 // 재선언: 가능
c = 3 // 재할당: 가능
```



### 데이터 타입

Javascript의 데이터 타입은 크게 **Primitive Type**과 **Reference Type** 두가지로 나뉜다

|          | Primitive Type                                               | Reference Type                                               |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **특징** | - Object가 아닌 기본 타입<br />- 실제 값 자체가 담긴다<br />- 복사시 실제 값이 담긴다 | - Object 형태<br />- 값의 주소가 저장된다<br />- 복사시 참조 값이 복사된다 |
| **예시** | 숫자, 문자열, undefined, null, Boolean                       | 객체(object), 함수(function), 배열(array)                    |



코드상에서는 `typeof` 함수를 통해 데이터의 정확한 타입을 알 수 있다.

```javascript
let myNum1 = 100
let myNum2 = "100"

console.log( typeof myNum1 ) // number
console.log( typeof myNum1 ) // string
```



### 형 변환 (문자열, 숫자, Boolean...)

##### 1. 문자열 (String)으로 변환하기

String으로 변환하는 방법은 간단하게 `String()` 함수를 써서 변환하면 된다. 몇가지 예외적인 상황과 함께 String의 결과값을 살펴보자면..

```javascript
console.log(String(123)) // 123
console.log(String(true)) // true
console.log(String(NaN)) // NaN
console.log(String(undefined)) // undefined
console.log(String(null)) // null
console.log(String(['apple', 'banana'])) // apple, banana
console.log(String({'fruit': 'apple'})) // [object Object]
```

- primitive type은 123, true, NaN, undefined, null(object로 분류되지만 설계상 오류이고 사실상 primitive type으로 간주)과 같은 그 값에 상관없이 값 그대로가 String 형태로 출력되는것을 알 수 있다
- 배열과 object같은 reference type은 해당 부모 클래스의 toString() 메서드에 명시되어 있는대로 출력이 되는것을 알 수 있다. 우리가 직접 이 클래스들을 작성한 것은 아니지만, 자바스크립트 내부적으로 배열, 객체와 같은 클래스의 toString 메서드는 위와같이 설정이 되어있기때문에 다음과 같이 출력된다.



##### 2. 숫자 (Number)로 변환하기


### Truthy / Falsy
Boolean 값 과는 별개로 "참"으로 인식되는 값, "거짓"으로 인식되는 값을 뜻한다

#### Falsy 한 값들의 예제
```
null, undefined, 0, -0, NaN, ""
```

#### Truthy / Falsy 속성을 활용하여 null 체크를 하는 방법