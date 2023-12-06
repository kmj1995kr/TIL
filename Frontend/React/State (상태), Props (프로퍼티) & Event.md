### State (상태)
>  컴포넌트 내의 변경 가능한 데이터 저장소

#### 기본 사용 방법
React의 `useState` 를 사용하여 상태값을 관리할수 있다

**State 선언하기**
> const [<상태명>, <상태변경함수명>] = useState(<기본값>)

**상태 변경하기**
> <상태변경함수명>(<변경할값>)

### 예시

```jsx
import React, { useState } from "react";

const Counter = () => {
	// state 선언
	const [count, setCount] = useState(initialValue);
	
	const onIncrease = () => {
		// setCount 메서드를 활용하여 상태 변경
		setCount(count + 1);
	};
	
	const onDecrease = () => {
		// setCount 메서드를 활용하여 상태 변경
		setCount(count - 1);
	};
	
	return (
		<div>
			<h2>{count}</h2>
			<button onClick={onIncrease}>+</button>
			<button onClick={onDecrease}>-</button>
			<OddEvenResult count={count} />
		</div>
	);
};

export default Counter;
```


### Props (프로퍼티)
> 부모 컴포넌트 -> 자식 컴포넌틑로 전달되어 내려져 오는 데이터
> 부모 컴포넌트에서 내려주는 prop명과 자식 컴포넌트에서 받는 prop명이 동일해야 props을 전달 받을 수 있다

### 사용법 예시
1. 부모 컴포넌트
```jsx
import React from "react";


import Counter from "./Counter";
import Container from "./Container";

  

function App() {

	const counterProps = {
		a: 1,
		b: 2,
		c: 3,
		d: 4,
		e: 5,
		initialValue: 5,
	};

	return (
		<Container>
			<div>
				// 단일값 전달하기
				<Counter a={1} />
				// Spread 연산자를 활용하여 여러 값을 하나의 객체로 묶어 전달하기
				<Counter {...counterProps} />
			</div>
		</Container>
	);
}

export default App;
```

2. 자식 컴포넌트
```jsx
import React, { useState } from "react";

// 단일 값을 전달받는 경우
const Counter = (initialValue) => {
	const initialValue = initialValue
	return (
		<div>
			<h1>{initialValue}</h1>
		</div>
	);
};

// 다중 값을 전달하는 경우
// Spread 연산자로 값을 전달받는 경우
const Counter = ({initialValue}) => {
	const a = initialValue
	return (
		<div>
			<h1>{a}</h1>
		</div>
	);
};

// props로 전달된 값이 없을 경우 default 값 설정
Counter.defaultProps = {
	initialValue: 0,
};


export default Counter;

```

## Event
React에서 기본적으로 데이터는 단방향으로만 움직인다 (부모 -> 자식 컴포넌트)
하지만 자식 컴포넌트에서 전달받은 데이터를 변경하고 싶을때는 어떻게 해야할까?

그럴때 `State를 변경할수 있는 함수 자체를 Props로 내려줌`으로써 `자식 컴포넌트에서 setState 함수를 직접 호출`할수 있고, 이런 형태로 `event를 발생시켜 부모 컴포넌트의 데이터를 변경`시킬 수 있다

### 사용법 예시
1. 부모 컴포넌트에서 State 변경 함수를 만들어 자식 컴포넌트에 Props로 내려준다
```jsx
function App() {
	const [data, setData] = useState([]);
	const onCreate = ({newData}) => {
		// 기존 배열 앞에 새로운 data 1건을 추가한다
		setData([newData, ...data])
	}

	return (
		<div className="App">
			<ChildComponent onCreate={onCreate} />
		</div>
	)
}
```

2. 자식 컴포넌트에서 전달받은 함수를 사용하여 State를 변경하는 Event를 발생시킨다
```jsx
const ChildComponent = ({ onCreate }) => {

	// 저장 버튼을 누를때 객체를 추가하는 onCreate event를 발생시킨다
	const handleSubmit = () => {
		onCreate({"val1", "val2", "val3"});
	}
	
	return (
		<div className="ChildComponent">
			<div>
				<button onClick={handleSubmit}>저장하기</button>	
			</div>
		</div>
	)
}
```

#react #state #props #event
