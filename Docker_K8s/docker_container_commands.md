# 도커 컨테이너 실행 및 관리 명령어

### 컨테이너 내부 쉘 실행 및 종료

```bash
# 실행
$ docker exec -it <container_name or id> <실행 하고 싶은ㅇ 명령어>
$ docker exec -it jenkins /bin/bash


# 종료
$ exit
```



### 컨테이너 로그 확인

```bash
$ docker logs <container_name or id> # stdout, stderr
```



### 컨테이너 간 파일 복사

```bash
$ docker cp <from_path> <to_path>

# 예제 1: 호스트 --> 컨테이너로 파일 복사
$ docker cp <file_name> <to_container>:/<상세경로>
$ docker cp test.txt tc:/

# 예제 2: 컨테이너 --> 호스트로 파일 복사
$ docker cp <from_container>:/<상세경로>/<file_name> <to_path>
$ docker cp tc:/test.txt ./test2.txt
```



### 복잡한 컨테이너 생성 예제

##### 환경 변수 설정해서 mysql 컨테이너 생성

```bash
$ docker run --name ms -e MYSQL_ROOT_PASSWORD=!qhdkscjfwj@ -d --rm mysql
```

##### 볼륨 마운트 옵션 사용해서 로컬 파일 공유하기

- Access type
  - `ro`: 읽기 전용
  - `rw`: 읽기 및 쓰기

```bash
$ docker run -v <host_path>:<container_path>:<access_type>
```



#### 