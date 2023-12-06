### 연산자

#### 할당 연산자

데이터에 연산을 하면서 새로운 값을 할당하는 연산자이다

```javascript
let x = 0

// 파이썬과 동일하게 다음과 같은 연산을 할 수 있다
x += 1
x -= 1
x *= 10
x /= 10

// x의 값을 1씩 증가 또는 감소 시키는 다음과 같은 연산도 할 수 있다
// 주로 for, while loop에서 값을 1씩 증가시키면서 looping을 할때 쓰인다
x++
x--
```



#### 비교 연산자

Javascript에서는 두가지 타입의 비교연산이 존재한다

- **동등 비교 연산자 (==)**: Javascript에서 내부적으로 형변환(암시적 형변환)이 진행되어, 형 변환 된 값이 같은지 다른지를 비교한다

  - Boolean 값과 비교시 각 데이터 타입은 다음과 같이 변환된다 (<a href="https://tc39.es/ecma262/#sec-ecmascript-language-types-boolean-type">출처</a>)

    | Type      | false         | true            |
    | --------- | ------------- | --------------- |
    | Undefined | 항상          | X               |
    | Null      | 항상          | X               |
    | Boolean   | false         | true            |
    | Number    | +0, -0, NaN   | 그 외 모든 경우 |
    | String    | 빈 문자열("") | 그 외 모든 경우 |
    | Symbol    | X             | 항상            |
    | BigInt    | 0             | 그 외 모든 경우 |
    | Object    | X             | 항상            |

- **일치 비교 연산자 (===)**: 형변환을 하지 않고, 엄격한 비교(데이터의 값과 타입을 모두 비교)가 이루어진다

#### 논리 연산자

- `&&`: and 연산자
- `||`: or 연산자
- `!`: not 연산자
- 단축 평가를 지원한다: 비교 대상중 하나만 비교했을때도 그 결과값을 알 수 있을때, 더 이상 비교를 진행하지 않고 바로 결과값을 반환



#### 삼항 연산자

- 세 개의 피연산자를 사용해 true / false 여부에 따라 값을 반환하는 연산자
- `(a ? b : c)`: a의 조건식이 참이라면 b를 반환, 거짓이라면 c를 반환

```javascript
console.log(true ? 1 : 2) // true
```

python 문법에서 다음과 동일하다

```python
a = true
print(1 if a==True else 2)
```

