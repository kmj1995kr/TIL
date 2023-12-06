# Javascript Manipulation (DOM 조작)

### DOM 조작으로 할 수 있는 것들

1. DOM 만들기
2. Child 추가하기
3. DOM 안에 있는 text 바꾸기
4. DOM의 attribute 바꾸기
5. DOM 삭제하기



### Manipulation 예제 코드

##### 1. DOM 만들기

```javascript
const ul = document.createElement('ul')
const li1 = document.createElement('li')
const li2 = document.createElement('li')
```

##### 2. Child 추가하기

```javascript
body.appendChild(ul)
ul.append(li1, li2)
```

##### 3. DOM 안에 있는 text 바꾸기

```javascript
li1.innerText = 'Hello'
li2.innerHTML = '<strong>Hello</strong>'
```

##### 4. DOM의 attribute 바꾸기

```javascript
li1.style.color = 'blue'
li2.setAttribute('id', 'myId')
```

##### 5. DOM 삭제하기

```javascript
li1.remove()
```

