# GitHub Token Authentication으로 바꾸기

Github을 사용하면서 작년부터 많이 받기 시작했던 이메일이 있었다.

![Screen Shot 2021-08-01 at 3.49.20 PM](/Users/minji/Desktop/Screen Shot 2021-08-01 at 3.49.20 PM.png)



대충 작년 2020년 12월 15일부로 이메일과 비밀번호로 인증하는 방식을 바꾸려고 하는중이고 곧 deprecate 될 예정이라는 이메일이었다. 매번 바꿔야겠다는 생각은 있었지만, 계속 까먹기도하고..ㅎㅎ Git의 기본적인 기능말고는 사용해본적이 많이 없었던터라 미루고 미루던 끝에 드디어 바꿔보기로했다!

끝내고 보니 너무 쉬운 작업이었어서 이걸 왜 이때까지 미루고 있었지 생각이 들었다..



#### 1. 토큰 발급받기 (Generate Token)

Github 공식 홈페이지에서 제공하는 <a href="https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token">해당 링크</a>에 스크린샷과 함께 자세한 설명이 나와있어서 토큰을 발급받는 부분은 전혀 어렵지 않게 할 수 있었다!

>  홈페이지 우측 상단에 프로필 아이콘 > Settings > Developer settings > Personal access tokens > Generate new token

순서로 클릭해 토큰을 받급받는 페이지로 이동할 수 있다. 이 페이지에서는 해당 토큰을 사용하는 사람이 얼만큼의 권한을 가질 수 있는지에 대한 scope을 지정할 수 있는데 직접 써보지 않은 것들이 많아서 내가 필요한 기능들을 수행하기 위해서는 어떤 권한들이 필요할지에 대한 궁금증이 생겼다.



#### 1-1. Scope 설정하기

Github <a href="https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps">공식 문서</a>를 통해 다양한 권한들에 대한 설명을 볼 수 있었다. 그 중 내가 필요로 하는 주요로 하는 기능들은:

- `repo`: repository에 대한 접근 / 통제 권한 - 이 카테고리에 있는 기능들만 포함해도 일상적인 git으로 활용하는 기능들은 거의 전부 수행할 수 있다
  - `repo:status`: public / private repo에 대한 커밋 기록을 볼 수 있는 권한 부여
  - `public_repo`: public repo에 대한 모든 권한 부여 (push, pull, fetch 등등..)
- `admin:org`: Organization에 대한 권한 부여
  - `write:org`: organization의 멤버 관리, 프로젝트 관리등의 권한 부여
  - `read:org`: organization에 있는 멤버, 프로젝트를 볼 수 있는 권한 부여
- `delete_repo`: 레포지토리 삭제 권한 부여



여기서 신기했던건 token access를 통해서는 내가 할 수 있는 액션만 제한할 수 있을 뿐, **어떤 repository에 대한 권한을 부여할지 선택적으로 제한할 수는 없다는 것이었다**. 이런 기능을 활용하려면 `deploy key` 라는걸 활용해야된다는데 이건 다음번에 기회가 있으면 활용해 보는걸로..

나는 나 혼자만 활용할 내 repository들에 대한 권한이 필요했기 때문에 모든 권한을 부여했다!



#### 1-2. 발급 받은 토큰 저장하기

`Generate token` 버튼을 누르면 방금 발급받은 토큰을 볼 수 있는데, **이번 한번만 볼수 있으니 꼭 저장해놓아야된다!**



#### 2. 기존 remote 연결 삭제하기

터미널 창을 켜서 git repository와 연결되어 있는 가장 상단 폴더로 이동해준다

여기에서 `git remote -v`라는 명령어를 입력하면 현재 연결되어 있는 remote repository의 정보를 보여준다. 현재는 다음과 같은 형태로 url이 설정되있다.

```bash
$ git remote -v

origin https://github.com/<유저 또는 org 이름>/<repo 이름> (fetch)
origin https://github.com/<유저 또는 org 이름>/<repo 이름> (push)
```



아래 명령어를 사용해 현재 remote 연결을 삭제한다 (앞 단계에서 url 앞에 적혀있는 키워드가 remote의 이름이다 - 이름이 origin이 아니라면 remote의 현재 이름을 사용)

```bash
$ git remote remove origin
```



#### 3. Token을 활용해 remote repository를 다시 연결하기

터미널 창에서 아래 명령어를 입력한다

```bash
$ git remote add origin https://<토큰>/<유저 또는 org 이름>/<repo 이름>
```

- 여기서 토큰 뒷부분을 어떻게 적어야할지 확실히 잘 모르겠다면, 원하는 repository의 github 페이지로 들어가서 url의 `https://github.com/` 뒷부분을 복사해서 쓰면 된다.

다시 `git remote -v` 명령어를 사용했을때 아까랑은 다르게 토큰이 포함된 url이 설정된 것을 볼 수 있다.

