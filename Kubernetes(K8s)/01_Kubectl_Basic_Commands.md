# Kubectl Basic Commands

전체 노드 목록 보기

```shell
$ kubectl get nodes
```



서비스 배포하기

```shell
$ kubectl create deploy nx --image=nginx
$ kubectl expose deploy nx --type=LoadBalancer --port=80 --target-port=80
```



배포중인 pod 확인하기

```shell
$ kubectl get pod,svc
```

