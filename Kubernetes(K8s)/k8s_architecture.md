# 쿠버네티스 클러스터 아키텍처

### 쿠버네티스 구조

<img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F998670455B140DE22B">

- Master Node: 관리 역할을 하는 관리자 노드
  - etcd: DB
  - kube-apiserver: etcd에 중요한 데이터들을 저장하고 관리하는 역할, etcd에 접근 권한을 가지고 있음 (인증, 통신, 권한 관리)
  - kube-schedule: 어떤 워커노드에 어떤 컨테이너가 배치 될지 결정하는 역할
  - Controller-manager: 리소스를 관리 / 제어 하는지 결정하는 -> CPU 역할을 하는 부분
- Worker Node
  - Kubelet: 워커 노드의 대장 같은 역할
  - Kube-proxy: 내부에서 컨테이너간의 통신 혹은 노드간의 통신을 위해 노드를 이어주는 역할
  - Container runtime: 실제 컨테이너를 실행하는 도커
    

### 쿠버네티스의 동작 과정

1. image를 도커 레지스트리로 푸쉬
2. 앱 디스크립터 (yaml 파일 또는 json 파일로 작성)
   1. 컨테이너 이미지에 대한 정보 포함
   2. 컴포넌트 간 관련성 및 노드 배치 (동일 노드 / 다른 노드) 정보 포함
   3. 컴포넌의 실행 복제본 수 지정 
3. 컨트롤 플레인 (마스터)로 앱 디스크립터 전달
4. 각각의 워커노드로 몇개의 이미지를 어떻게 배치해서 실행시킬지 결정

