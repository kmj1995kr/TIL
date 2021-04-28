# Javascript DOM Selector (선택자)

### DOM이란?

**HTML** 요소들을 **구조화해서 표현한 인터페이스**, 프로그래밍 언어를 통해 DOM 구조에 쉽게 접근할 수 있는 방법을 제공하여 문서의 구조, 스타일, 내용등을 변경할 수 있도록 돕는다.

대표적으로 Javascript를 활용해 DOM의 각 object에 접근하여 선택, 수정할 수 있다.



### querySelector / querySelectorAll

- Class, Id, TagName 등등 **다양한 속성을 통해 DOM**을 가져올 수 있다
- querySelector는 **단일 Object** (여러개가 있다면 그 중 첫번째 조건에 부합하는 object)를 가져온다
- querySelectorAll은 조건에 맞는 **모든 Object**를 **NodeList**의 형태로 가져온다

```javascript
// 첫 번째 일치하는 요소 가져오기
const selectOneByClass = document.querySelector('.myclass')
const selectOneById = document.querySelector('#myid')
const selectOneByTag = document.querySelector('body > h1')

// 모든 요소 가져오기
const selectAllByClass = document.querySelectorAll('.myclass')
const selectAllById = document.querySelectorAll('#myid')
const selectAllByTag = document.querySelectorAll('body > h1')
```



### getElementBy

- Class, Id, TagName 별로 DOM을 가져올 수 있다
- **getElementById**: 해당 아이디를 가진 단일 객체를 가져온다
- **getElementByClass**: 해당 클래스를 가진 객체를 HTMLCollection의 형태로 모두 가져온다
- **getElementByTagName**: 해당 TagName을 가진 객체를 HTMLCollection의 형태로 모두 가져온다

```javascript
const byId = document.querySelector('myid')
const byClass = document.querySelector('myclass')
const byTagName = document.querySelector('h1')
```



### querySelector vs. getElementBy

| querySelector                                                | getElementBy                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - Class, Id, TagName에 상관없이 동일한 querySelector 메서드를 쓸 수 있다<br />- querySelectorAll의 경우 NodeList로 결과 반환 (Static) | - Class, Id, TagName에 따라서 알맞는 메서드를 사용해야한다<br />- 여러 객체 반환시 HTML Collection으로 결과 반환 (Live) |



