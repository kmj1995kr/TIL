##### 1. Next.js 프로젝트 생성하기
```bash
$ npx create-next-app@latest .
```

##### 2. 프로젝트 생성 시 기본설정
아래와 같은 설정이 가능하다
- Typescript
- EsLint
- Tailwind
- src
- App Router
- Alias
![[Screenshot 2024-02-06 at 10.14.49 AM.png]]

##### 3. 프로젝트 실행
```bash
$ npm run dev
```

##### 4. 서버 배포
```
$ npm run build
$ npm run start
```

### Next.js의 특징
- Server Side Rendering을 사용한다
	- 브라우저 개발자 도구에서 javascript를 disable해도 서버에서 렌더링 해서 전달해주기 때문에 끊기지 않고 동작한다
	- 서버가 떠 있는 상태여야 한다
- Server Component를 default로 사용한다
	- server component: 정보를 제공해주는, 사용자와의 상호작용이 없는 컴포넌트, 정적인 html만 브라우저로 전송된다 
	- client component: 상호작용이 있는 컴포넌트, js가 브라우저로 전송된다 (js가 반드시 있어야 동작하는 컴포넌트들: useEffect, useState, onSubmit과 같은 이벤트들)
- App Router
	- 라우팅을 위한 특별한 naming convention을 사용한다
		- `page.tsx`: 생성될 컴포넌트
		- `layout.tsx`: 컴포넌트를 감싸고 있는 layout
	- 일반 라우팅 (`/create`) 라는 경로에 페이지를 만들고 싶다면:
		- `/src/app` 하위에 `create`라는 폴더를 만든다
		- `/src/app/create` 하위에 `page.tsx` 파일을 만들고 내용을 추가한다
	- 다이나믹 라우팅
		- `[변수명]`의 경태로 폴더를 만든다
		- 예) `/src/app/read/[id]` 하위에 `page.tsx` 파일을 만들면, `localhost:3000/read/<id>` 경로로 라우팅 되는 페이지를 만들수 있다