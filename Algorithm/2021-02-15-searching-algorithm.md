# Searching Algorithm

### 완전 검색 (Exhaustive Search)

- 모든 경우의 수를 나열해보고 확인하는 방법
- 일반적으로 경우의 수가 작을 때 유용

### 순차 검색 (Sequential Search)

- 완전 검색의 한 종류

**정렬되어 있지 않은 경우**

- 하나씩 돌아가며 비교해보고 찾는 키값이랑 동일한지 확인
- 시간 복잡도: O(n)

```python
i = 0
while i < n:
  i += 1
	if a[i] == key:
    return i
return -1
```

**정렬되어 있는 경우**

- 자료를 순차적으로 검색하면서 키 값을 비교하여 현재 비교하는 값이 키 값보다 크면, 이미 찾으려고 하는 키 값을 넘어섰기 때문에 그 즉시 검색 종료
- 시간 복잡도: O(n) --> 어차피 최악의 경우 모든 경우의 수를 다 봐야함

```python
arr = [2, 3, 4, 7, 9, 11, 23]
key = 10
i = 0

# while문으로 작성하기
while i < len(arr) and arr[i] < key:
  if a[i] == key:
    return i
  i += 1
return -i

# for문으로 작성하기
for i in range(len(arr)):
  if i == key:
    return i
return -i
```



### 이진 검색 (Binary Search)

- 정렬이 되어 있어야됨

- 중앙을 기준으로 key 값이 더 크다면, 오른쪽만 탐색, 더 작다면 왼쪽만 탐색



### 셀렉션 알고리즘 (Selection Algorithm)

- k번째로 작은/큰 원소를 찾는 알고리즘



