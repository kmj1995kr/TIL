# Vue 프로젝트 시작하기

1. vue cli 설치하기

```bash
$ npm install -g @vue/cli
```

2. 버젼 확인하기

```bash
$ node -v
$ vue --version
```

3. vue cli로 프로젝트 생성하기

```bash
$ vue create my-first-vue-app
```

4. 다음과 같이 옵션 선택

![Screen Shot 2021-05-10 at 10.41.51 PM](/Users/minji/Library/Application Support/typora-user-images/Screen Shot 2021-05-10 at 10.41.51 PM.png)

5. 서버 실행하기

```bash
$ cd my-first-vue-app
$ npm run serve
```





### Vue 프로젝트 구조

![Screen Shot 2021-05-10 at 10.50.45 PM](/Users/minji/Library/Application Support/typora-user-images/Screen Shot 2021-05-10 at 10.50.45 PM.png)

`node modules`: pip와 비슷하게 패키지를 관리하는 npm으로 설치된 패키지들을 보관하는 폴더

`src`: 대부분의 소스 코드가 작성되는 폴더

`package-lock.json` / `package.json`: npm을 통해 설치된 패키지들을 나열해 놓은 패키지 의존성 관련 파일 (장고의 requirements.txt와 비슷)



### .vue 파일 구조

- Single file component로 한 파일이 한 컴포넌트를 담당
- Vue Component === Vue Instance
- `template`, `script`, `style` 태그로 구성되어있음
  - template: html
  - script: js
  - style: css
  - scoped를 활용해 현재 스코프 설정 가능
    - Scoped: 현재 파일에만 적용
    - 기본 (아무것도 작성하지 않음): 하위 컴포넌트에도 적용
- App.vue: 메인 부모 컴포넌트
- Components 폴더: 하위 컴포넌트가 저장되는 폴더

