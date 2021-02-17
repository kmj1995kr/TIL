# Sorting Algorithm

### 버블 정렬

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 한 라운드가 끝날때 마다 맨 오른쪽에 가장 큰 원소가 정렬되서 배치된다
- 그 다음 라운드부터는 정렬된 오른쪽 원소를 제외한 나머지 구역에서 정렬을 진행한다
- **시간 복잡도:**  O(n**2)

```python
arr = [64, 25, 10, 22, 11]
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        print(i, j)
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
```



### 카운팅 정렬

- 각 항목이 몇 개씩 있는지 세는 작업을 해서 오름/내림차순으로 항목의 갯수만큼 출력
- 정수로 표현할 수 있는 자료에 대해서만 적용 가능
- 카운트 하기 위해 집합 내의 가장 큰 정수를 알아야 한다
- **시간 복잡도:** O(n)

```python
# 나올수 있는 최대값은 9이다
lst = [0, 4, 1, 3, 1, 4, 1, 9, 9, 8]
counts_arr = [0] * 10
arr = []

for num in lst:
    counts_arr[num] += 1

for i in range(len(counts_arr)):
    arr += [i] * counts_arr[i]
```



### 선택 정렬

- 주어진 자료중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 셀렉션 알고리즘을 전체 자료에 적용한 것이다

```python
arr = [64, 25, 10, 22, 11]

for i in range(len(arr)-1):
  min_idx = arr[i]
  
  for j in range(i+1, len(arr)):
    if a[j] < a[min_idx]:
      min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
```

