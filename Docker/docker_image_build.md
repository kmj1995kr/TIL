# 도커 이미지 빌드하기

1. 실행될 파일 작성
2. 도커파일(dockefile) 작성
3. 도커 이미지 빌드하기



### 도커파일 작성

```dockerfile
FROM python:3.7

RUN mkdir /echo
COPY test_server.py /echo

CMD ["python", "/echo/test_server.py"]
```



### 도커 이미지 작성하기

```bash
# dockerfile이 있는 디렉토리에서 해당 명령어 실행
# .은 현재 디렉토리를 의미
$ docker build -t echo_test .
```

