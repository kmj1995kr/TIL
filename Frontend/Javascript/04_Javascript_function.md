### 함수 선언 방법 1: 함수 선언식
함수 자체에 이름을 부여하여 선언하는 방식

```javascript
function getArea(width, height) {
	let area = width * height
	return area
}
```

### 함수 선언 방법 2: 함수 표현식
함수에 이름을 부여하지 않고, 함수를 변수에 담아 저장하는 방식

```javascript
let hello = function () {
	return "hello"
}
```

### 함수 선언 방법 3: 화살표 함수 (Arrow Function)
함수 표현식의 또 다른 표현 방식으로, 함수 표현식을 더 간단한 문법으로 작성 가능하다
```javascript
let helloB = () => {
	return "안녕하세요"
}

// return 값이 한줄일 경우 아래와 같이 사용도 가능하다
let helloC = () => "안녕하세요"
```

### 함수 선언식과 함수 표현식의 차이
> 함수 선언식과 함수 표현식의 가장 큰 차이는 **Hoisting** 이다.
> 함수 선언식으로 생성된 함수는 hoisting이 되어 자바스크립트 파일이 로딩될때 가장 먼저 렌더링 되기 때문에, 함수 선언보다 윗줄에서 해당 함수를 호출하더라도 함수를 호출하여 사용할 수 있다

```javascript
// 함수가 선언되기도 전에 console.log를 했는데도 함수가 정상적으로 호출이 되는것을 볼수 있다
console.log(hoistedFunc())

function hoistedFunc() {
	return "hoist"
}

```


### 콜백 함수

```javascript
function checkMood(mood, goodCallback, badCallback) {
	if (mood === "good") {
		goodCallback();
	} else {
		badCallback();
	}
}

function cry() {
	console.log("T.T")
}

function dance() {
	consoloe.log("DANCE")
}

```