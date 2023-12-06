```jsx
import { useRef } from "react";

const DiaryEditor = () => {
	const authorInput = useRef();
	const contentsInput = useRef();
	const handleSubmit = () => {
		if (state.author.length < 1) {
			authorInput.current.focus();
			return;
		}
		if (state.contents.length < 5) {
			contentsInput.current.focus();
			return;
		}
	return (
		<div>
			...
			<input
				ref={authorInput}
				name="author"
				value={state.author}
				onChange={handleChangeState}
			/>
			<input
				ref={contentsInput}
				name="author"
				value={state.contents}
				onChange={handleChangeState}
			/>
			<div>
				<button onClick={handleSubmit}>일기 저장하기</button>
			</div>
			...
		</div>
	);
};
```

#react #useref #dom