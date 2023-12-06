# Authentication System

### Authentication System

**Authentication(인증)**: 누군가의 신원을 확인하는 것 (ex.로그인)

**Authorization(권한)**: 가고 싶은 곳으로 가도록, 혹은 원하는 정보를 얻도록 허용하는 과정 (ex. 회원 정보 수정)

- 장고에서는 Authentication System이라고 칭하며, 두개의 기능이 어느정도 결합되어 있음

- 장고에서는 기본적으로 인증에 관련된 built-in form들을 제공

- User에 관한 정보들은 별도의 앱에서 관리 (**accounts**라고 보통 칭함)

**Http(Hypter Text Transfer Protocol)**: HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜 (규칙, 약속)

- **Connectionless (비연결지향)**: 서버는 응답 후 접속을 끊음
- **Stateless (무상태)**: 접속이 끊어지면 클라이언트와 서버 간의 통신이 끝나며 상태를 저장하지 않음
  - http는 상태 정보를 유지하지 않기 때문에 로그인 된 유저의 정보를 계속 유지 시킬 수 있는 도구가 필요

**Session**: 사이트와 특정 브라우저 사이의 상태(state)를 유지 시키는 것, 현재 사용자에 대한 상태 정보를 담고 있음

- django에서는 django_sessions 테이블에 `sessionid` 라는 이름으로 저장 

**Cookie:** 사용자의 브라우저(클라이언트)에 저장되어 있는 데이터; 쿠키는 상태가 있는 세션을 만들도록 해준다, Metadata

- 세션 관리, 개인화, 트래킹 등등에 사용 가능
- session cookie / permanent cookie



#### **Session의 동작 원리**

1. 클라이언트: 서버 접속 (로그인)
2. 서버: 유저 DB에서 유저가 등록되어 있는지 체크
3. 서버: session id를 발급
4. 클라이언트: session id를 쿠키에 저장
5. 클라이언트: 다음번 요청 때 session id가 담긴 쿠키와 요청을 함께 보냄
6. 서버: 동일한 session인지 체크 후 로그인 상태 유지한채로 응답을 보냄



### Djanago's Authentication in Web Requests

- 사용자를 나타내는 모든 요청에 `request.user`를 제공

  - User 또는 Anonymous User 두가지로 나눌 수 있다

- **로그인**: `login` 함수를 통해 구현 가능, session을 create하는 로직과 같음

  - `auth_login`
  - Request 와 User 객체를 통해 구현 가능
  - 로그인되어 있지 않은 사용자: `AnonymousUser`
  - 로그인 된 사용자: `User` 클래스의 인스턴스

  - AuthenticationForm으로 구현: ModelForm이 아닌 일반 Form으로 구현
    - request와 request.POST를 인자로 받음
  - `'next'` 파라미터를 사용해 원래 가려고 했던 곳으로 돌려보내줄 수 있다 

- **로그아웃**: `logout` 함수를 통해 구현 가능, session을 delete하는 로직과 같음

  - `auth_logout`
  - request 객체를 받으며 return이 없음

- **로그인에 관련된 함수**

  - `is_authenticated`: 사용자 인증 여부를 알 수 있는 함수 (인증)
  - `@login_required`: 로그인을 한 유저에게만 실행 권한을 부여해주는 함수 (권한)
  - `@login_required` 로직을 `is_authenticated` 로도 구현할 수 있지만, 사용 목적에 차이가 있음: `is_authenticated`는 

- `AuthenticationForm`: 로그인 기능을 담당하는 폼
  - 유저 테이블을 직접 수정하는 것이 아닌 sessionid를 만들고 삭제하는 역할을 수행한다
- `context_processor`: django에 존재하는 context를 저장해주는 기능
  - user 정보가 담겨있기 때문에 `request.user`가 아닌 `user`로 바로 불러올 수 있다

#### templates와 view에서의 로그인 분기처리

예를들어, 로그인이 되어있지 않은 사용자는 글을 쓰지 못하게 막고 싶다

1. template에서 `if user.is_authenticated`를 사용해 로그인된 유저에게만 글쓰기 버튼이 보이게 처리
2. url로 직접 접근을 막기위해 views의 create 함수에 `@login_required` 데코레이터를 사용해준다

#### 쿠키 확인 방법

개발자 도구 --> Application Tab --> Storage --> Cookies

