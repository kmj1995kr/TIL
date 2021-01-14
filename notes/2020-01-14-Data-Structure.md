# 2021-01-14 Data Structure

### 기본적인 데이터 타입 (Basic Data Type)

데이터 타입에는 크게 **1) 숫자, 2) 문자, 3) Boolean**이 있음

데이터 타입을 체크하려면 `type()` 함수를 사용해서 확인할수 있다

```python
# 숫자
number = 3 
print(type(number))

# 문자
string = '문자열'
print(type(string))

# boolean
boolean = True
print(type(boolean))
```



### 리스트 (List)

```python
# python_list.py
# python_list.py

# 리스트 선언
my_list = ['java', 'django']

# 리스트 원소 접근
print(my_list[0])

# 리스트 원소 변경
my_list[0] = 'python'

# 리스트 원소 접근
print(my_list[0])
print(my_list[0][1]) # y

# 리스트 길이
print(len(my_list))
```



### 딕셔너리 (Dictionary)

```python
# 딕셔너리 선언
my_home = {
    "location": "seoul",
    "area-code": "02",
}

# 딕셔너리 원소 접근
print(my_home['location'])
print(my_home['name'])
print(my_home.get('location'))
print(my_home.get('name')) # .get('name', 'justin') key 값이 없을 경우 디폴트 값 지정

# 딕셔너리 원소 변경
my_home['location'] = 'gumi'
print(my_home['location'])
```





