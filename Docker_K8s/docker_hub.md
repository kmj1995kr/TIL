# 도커 허브에 이미지 업로드 하기

### 사전 준비 사항

1. 도커 허브 아이디
2. 도커 허브에 업로드 할 수 있는 이미지



### 도커 허브에 이미지 푸시

1. 도커에 로그인 해준다

```bash
$ docker login
# username과 password를 각각 입력해준다
username:
password:

```

2. 도커에 푸시할 이미지 확인

```bash
$ docker images
```

3. 도커에 이미지 푸시

```bash
$ docker push <이미지_이름>:<태그명>
```

