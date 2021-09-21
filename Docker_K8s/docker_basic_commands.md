# 도커 이미지 / 컨테이너 생성, 실행 및 삭제 명령어

#### 도커 이미지 검색

```bash
$ docker search <keyword>
```



#### 도커 이미지 다운로드 / 삭제

```bash
$ docker pull <image_name>
```



#### 도커 이미지 확인

```bash
# 이미지 전체 리스트 조회
$ docker images
# 특정 이미지에 대한 정보 확인
$ docker inspect <image_name>
# 이미지 저장소 위치 확인
$ docker info
# 사용중인 디스크 공간 확인
$ du -sh <directory>
```

`docker inspect` 명령어를 사용했을 때 확인 할 수 있는 정보

- id: image를 고유 식별하기 위한 id
- env: 환경 변수
- cmd: 컨테이너가 실행될 때 실행되는 프로세스
- RootFS: 레이어 구성을 설명한 부분

`docker info` 명령어를 사용했을 때 확인 할 수 있는 정보

- Docker Root: Docker와 관련된 파일들이 저장되어 있는 루트 디렉토리 주소 (image, container 등등)
  - 실제 데이터가 저장되는 경로 `<Docker Root>/overlay2`
  - imagedb에 대한 정보 --> layerdb에 저장 --> layerdb에 대한 정보 --> overlay2에 저장 --> 실제 변경 사항은 `/var/lib/docker/overlay2/l`에 저장
- Storage Driver: storage가 설치되어 있는 위치
- Exposed Ports: 내부적으로 사용하는 포트 



#### 도커 이미지 생성 / 실행

자주 쓰이는 옵션

- `-d`: 백그라운드에서 실행
- `-p`: 포트 지정
- `--name`: 이름 지정
- `-e`: 환경 변수 설정

```bash
# 1. 생성과 실행을 따로 하는 방법
# 1-1. 컨테이너 생성
$ docker create -p <host_port>:<container_port> --name <name> <image_name>

# 1-2. 컨테이너 실행
$ docker start -d <container_name or id>

# 2. 생성과 실행을 동시에 하는 방법
$ docker run -d -p 80:80 --name tc tomcat

# 2-1. 임시 컨테이너 생성 (컨테이너를 내렸을때 자동 삭제)
# -rm 옵션 사용
$ docker run -d -p <port> -rm --name <name> <image_name>
```



#### 실행중인 컨테이너 확인

```bash
$ docker ps
$ docker container ls

# 컨테이너 이름만 id만 확인
$ docker ps -a -q
```



#### 모든 컨테이너 확인

```bash
$ docker ps -a
$ docker container ls -a
```



#### 컨테이너 중지 / 삭제

컨테이너를 중지해야지만 삭제가 가능!

**컨테이너를 지우고 동일한 포트로 다른 컨테이너를 만들었을 경우 캐시 때문에 이전 컨테이너가 보일 수 있음 --> 반드시 캐시를 지우고 확인해 보자

```bash
$ docker stop <container_name or id>
$ docker rm <container_name or id>

# 실행중인 컨테이너 일괄 중지 및 삭제
$ docker stop `docker ps -a -q`
$ docker rm `docker ps -a -q`
```

#### 

#### 이미지 삭제

컨테이너가 실행되고 있는 상황에서도 이미지는 삭제 가능 - 이런 경우 `-f` 옵션을 사용해서 삭제

```bash
$ docker rmi -f <image_name>

# 저장된 이미지 일괄 삭제
$ docker rmi `docker images -q`
```

