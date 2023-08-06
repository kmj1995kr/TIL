`jsx` 확장자 파일에서는 for 문법을 지원하지 않는다. React와 같이 `jsx` 확장자 파일을 사용하는 프레임워크에서 for 문법을 사용하고 싶다면 `map` 문법을 사용하면 된다


### Map 문법 사용 방법
> `{list.map((item) => (<함수내용>))}`

```jsx
const MyListPage = ({ myList }) => {
	return (
		<div className="DiaryList">
			<h2>일기 리스트</h2>
			<h4>{myList.length}개의 일기가 있습니다</h4>
			<div>
				{myList.map((item) => (
					<DiaryItem key={item.id} {...item} />	
				))}
			</div>		
		</div>
		);
	};
```