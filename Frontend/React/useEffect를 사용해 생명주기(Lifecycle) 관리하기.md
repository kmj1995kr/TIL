![[Screenshot 2023-08-06 at 5.04.40 PM.png]]

### 생명주기 (Lifecycle) 란?

### React에서의 Lifecycle 관리
Class형 component에서만 사용 가능하고 특정 stage에서 동작되어야 하는 함수들을 실행 시킬 수 있음
- Mount
- Update
- Unmount

### React Hooks
Class component에서 life cycle 관리를 하려면 중복 코드, 가독성등의 문제가 있었음 => 
기존의 Class component에서만 사용 가능한 기능을 함수형 component에서 사용 가능하도록 만들어 주는 기능이 React Hooks이다
(ex) `useState`, `useEffect`, `useRef`

### 사용 방법
1. Mount
```jsx
useEffect(() => {
	console.log("Mounted");
}, []);
```

2. Update
```jsx
// 모든 변경 사항에 대해 발생
useEffect(() => {
	console.log("Updated");
});

// 특정 값이 변경되었을때 발생
const [value, setValue] = useState("");

useEffect(() => {
	console.log("Value Updated")
}, [value])
```

3. Unmount
```jsx
useEffect(() => {
	return () => {
		console.log("Unmounted");
	};
}, []);
```