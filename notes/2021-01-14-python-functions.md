## 2021-01-14 Python Functions

### Main Objectives

- 내장함수 사용해보기
- 외장함수 사용해보기
- Python으로 함수를 생성하고 사용해보기
  

### 내장함수 사용하기 (Built in Fuctions)

> 파이썬 안에 내장되어 있는 (따로 불러올 필요가 없는) 함수

- 파이썬 내장함수 예제: https://docs.python.org/3/library/functions.html

- Ex) Range - immutable sequence, can be turned into a form of a list or a tuple

  

### 외장함수 사용하기 (Module)

>  외부에서 불러와 쓸 수 있는 함수
>
> Module은 공구박스와 같다 --> 이미 만들어놓은 공구박스에서 원하는 도구를 빼서 쓸수 있음

1. `import` 문을 사용해서 Library를 불러온다

   Ex ) `import random`

2. 원하는 Method를 골라서 쓸수 있다

   Ex ) `random.choice([list])`

> 주의사항: Module 이름과 충돌이 날 수 있는 폴더 / 파일 이름은 만들지 않기!

Ex) Random

```python
import random

numbers = range(1, 10)
lotto = random.sample(numbers, 6) # 중복 X
print(lotto)

lotto2 = random.choices(numbers, k = 6) # 중복 O
```



Ex) Datetime

```python
import datetime as dt

print(dt.datetime.now())
print(dt.datetime(2020, 1, 13))
```



