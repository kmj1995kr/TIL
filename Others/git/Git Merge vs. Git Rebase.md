출처: https://www.atlassian.com/git/tutorials/merging-vs-rebasing

Merge와 Rebase는 둘다 서로 다른 커밋 히스토리를 가진 두 branch를 합칠때 사용할 수 있다.
우선 아래와 같이 `Main` branch로 부터 파생되어 나온 `Feature` branch가 있다고 가정해보자

![A forked commit history](https://wac-cdn.atlassian.com/dam/jcr:1523084b-d05a-4f5a-bd1a-01866ec09ca3/01%20A%20forked%20commit%20history.svg?cdnVersion=1401)

`Feature`의 기능 개발이 완료되어 `Main`의 기능과 다시 합치려고 할때 사용이 가능한 두가지 방법이 `Merge`와 `Rebase`이다

### Merge
두 branch간의 변경 사항을 합친 하나의 새로운 merge commit을 만들어 target branch에 해당 변경 사항을 반영하는 방법
이 경우 Main과 Feature에서 각각 일어난 변경 사항들은 변경되지 않은채 history에 전부 기록되고, 합쳐지는 과정까지도 merge commit으로 기록되기 때문에 히스토리의 누락이나 변경없이 안전하게 merge를 할수 있다는 장점이 있다


![Merging main into feature branch](https://wac-cdn.atlassian.com/dam/jcr:4639eeb8-e417-434a-a3f8-a972277fc66a/02%20Merging%20main%20into%20the%20feature%20branh.svg?cdnVersion=1401)
#### 기본 문법
```bash
$ git merge <merge하려는 source-branch>
```
#### 사용 예시
``` bash
# feature branch를 checkout 한다
$ git checkout feature

# main branch의 변경사항들을 feature branch로 merge 한다
$ git merge main
```


### Rebase
어떤 특정 브랜치를 기준으로 커밋을 일어난 순서대로 재 정렬하는 방법
이 방법의 경우, 변경 사항을 합치기 위한 별도의 커밋이 생성되는것이 아닌 히스토리를 일렬 형태로 쭉 볼수 있다는 것이 장점이다



![Rebasing feature branch into main](https://wac-cdn.atlassian.com/dam/jcr:3bafddf5-fd55-4320-9310-3d28f4fca3af/03%20Rebasing%20the%20feature%20branch%20into%20main.svg?cdnVersion=1401)

#### 기본 문법
```bash
$ git rebase <기준이 될 branch>
```

#### 사용 예시
```bash
# feature branch를 checkout 한다
$ git checkout feature

# main을 기준으로 feature branch의 변경사항들을 신규 커밋으로 재정렬하여 추가한다
$ git rebase main
```

> **주의사항!**
> main(master) branch에서 rebase 명령어는 사용하지 말기
> 
> Rebase 사용시에는, main이 아닌 다른 branch로 먼저 이동한 다음 `git rebase main` 명령어를 통해 `main`을 기준 브랜치로 설정하여 rebase를 하자
> `main`은 이때까지의 모든 커밋 히스토리를 다 가지고 있는 브랜치인데, `main`에서 다른 branch로 rebase를 하게 되면 모든 `main`의 커밋 히스토리가 재정렬되는 참사가 일어난다....

### 실무에서 쓸수있는 방법

####  1. Merge (Pull)
`git pull` 명령어를 통해서도 merge를 수행할 수 있는데, git에서는 `pull` 명령어 수행시의 default behavior가 `merge`이다

``` bash
$ git fetch

$ git checkout feature

$ git pull origin main

#### resolve any conflicts

$ git add <things to add>

$ git commit -m "message"

$ git push origin feature

```

#### 2. Rebase
```bash
$ git fetch

$ git checkout feature

$ git rebase main

#### resolve any conflicts

$ git add <things to add>

$ git commit -m "message"

$ git push origin feature
```