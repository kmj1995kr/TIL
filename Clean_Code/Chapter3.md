# Clean Code Chapter 3: 함수

### 생각해 볼 것들

(Pg.57) 오류 코드보다 예외를 사용하라: 하지만 항상 try ~ catch로 예외 처리하는것이 좋을까?

### Java

##### try ~ catch와 if ~ else의 차이점

1. `try ~ catch` 는 블록이고, `if ~ else` 는 구문이다
   블록에서는 예외가 발생하면 그 즉시 종료되고 catch 블록으로 이동한다.
2. `try ~ catch` 에서는 try 와 catch문이 다른 스코프에 있지만 (catch문에서는 try문의 변수를 사용할 수 없음)
   `if ~ else` 에서는 예외 처리가 같은 스코프에서 진행된다
   => `try ~ catch` 에서는 지역 변수가 자동 소멸 되지 때문에 리소스 누수를 막을 수 있다
3.  `try ~ catch` 는 유지해야 할 정보가 많아 오류 처리 속도가 더 느리다

##### 언제 각각의 예외 처리 방법을 활용해야 할까?

- 정상적인 프로그램 흐름이 아닌 경우 (예) 서버가 다운 됨 => try ~ catch
- 예측할 수 있는, 로직상 처리해야하는 예외인 경우 (예) 필수 입력값이 누락되었다 => if ~ else





### Python

**if ~ else를 활용한 예**

```python
if key in mydict:
    mydict[key] += 1
else:
    continue
```

**try ~ except를 활용한 예**

```python
try:
    mydict[key] += 1
except KeyError:
    continue
```

**에러 상황을 만나지 않았을때**: try ~ except가 더 빠름

**에러 상황을 만났을때**: if ~ else가 더 빠름

### 왜 그럴까?

C나 다른 언어들과는 다르게 파이썬은 ***허락보다 용서가 쉬운 언어*** 이기 때문 (EAFP: easier to ask for forgiveness than permission)

파이썬은 코드가 실행될것이라는 전제로 먼저 코드를 실행하고, 실패 했을 경우에 예외처리를 하기 때문에, try문에서 예외가 발생하지 않을경우, 코드가 그냥 실행되는것과 같은 속도로 코드가 처리된다!

### 그러면 두개 중에 어떤걸 쓰면 좋을까?

기본적으로 try ~ except가 더 빠르지만, try ~ except는 예외 상황이 더 적을수록 빛을 발한다 :star:

- **예외 상황이 비교적 적은** 경우 --> try ~ except

- **예외 상황이 전체 케이스의 50% 이상 또는 예측 가능한 (분기점을 생성해야 하는) 에러**라고 생각될 경우 --> if ~ else