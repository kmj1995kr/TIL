# Vue Router

**Routing**: 네트워크의 한 지점에서 다른 지점으로 경로를 이동시켜주는 것

**Vue Router**

- 라우트 뷰 매핑
- 모듈화된, 컴포넌트 기반의 라우터 설정: 라우팅을 했을때 그것에 알맞는 컴포넌트를 로딩해서 보여준다
  - 실제로 페이지 새로고침이 일어나지는 않고, 새로운 컴포넌트만 로딩된다 (비동기 처리)

1. vue 프로젝트에 라우터 추가

```bash
$ vue add router
```

2. 라우터 설정

```
```

History API

- HTML5에서 처음 등장
- 이전에는 `#` 을 URI에 포함시켜 페이지내에서 새로고침 없이 이동할 수 있었다
- URI에서 `#`을 사용하지 않고도 새로고침없이 페이지내에서 로딩을 할 수 있게 만든것이 History Mode

### 라우터 정의

`src/router/index.js`에서 라우터 경로를 정의할 수 있다

views

- router에 매핑되는 컴포넌트를 모아두는 폴더
- root element는 반드시 하나 있어야된다

components

- router에 매핑된 컴포넌트안에 내부에 들어가는 컴포넌트들을 모아두는 폴더
- Naming Convention
  - 

