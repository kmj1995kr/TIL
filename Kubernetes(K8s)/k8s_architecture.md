# 쿠버네티스 클러스터 아키텍처

<img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F998670455B140DE22B">

- Master Node: 관리 역할을 하는 관리자 노드
  - etcd: DB
  - kube-apiserver: etcd에 중요한 데이터들을 저장하고 관리하는 역할, etcd에 접근 권한을 가지고 있음 (인증, 통신, 권한 관리)
  - kube-schedule: 어떤 워커노드에 어떤 컨테이너가 배치 될지 결정하는 역할
  - Controller-manager: 리소스를 관리 / 제어 하는 방법을
- Worker Node