

## 2021-01-14 Web Programming Introduction

### Web Programming 기초

웹은 매우 기본적인 레벨에서 **요청(Requests)** 과 **응답(Response)** 으로 이루어져있다

![req_res](2020-01-14-Web-Programming-Intro.assets/req_res.png)

#### 요청 (Request)

- Client에서 정보를 요청하는 일

#### 응답 (Response)

- Server에서 요청받은 정보를 반환하는 일
- Requests가 valid한지 아닌지에 따라서 status code로 나타내서 같이 반환한다 (200, 201, 404, 502...)
  - 20X - 정상요청
  - 40X - 잘못된 리퀘스트
  - 50X - 서버에러



### Requests를 사용해서 정보 요청하기 (웹 크롤링)

1. 요청을 보내서 **HTML 형태로 된 응답** 받아오기

```python
import requests

# url의 본문 가져오기
response = requests.get('url').text

# status code 가져오기
status = requests.get('url').status_code
```

2. **Selector**를 사용해서 원하는 정보를 뽑아온다

   웹 브라우저 상에서 selector 찾는 법: 개발자 도구 --> 우클릭 --> 다음과 같이 선택

![copy_selector](2020-01-14-Web-Programming-Intro.assets/copy_selector.png)



3. 뽑아온 selector를 활용해 정보를 가져온다

```python

```



Requests를 사용한 크롤링 예제

```python
import requests

# url의 본문 가져오기
requests.get('https://finance.naver.com/main/main.nhn').text

# status code 가져오기
requests.get('url').status_code

```









### Requests를 사용해서 정보 요청하기 (API)