# 패턴 매칭 (Pattern Matching)

### 고지식한 알고리즘 (Brute Force)

문자열을 처음부터 끝까지 순회하면서 패턴 내의 문자들을 일일히 비교

```python
while j < M and i < N:
  if t[i] != p[j]:
    i = i - j
    j = -1
  i = i + 1
  j = j + 1
  if j == M: return i - M
  else: return -1
```

```python
for i in range(N - M + 1):
  cnt = 0
  for j in range(M):
    if t[i + j] == p[j]:
      cnt += 1
    else:
      break
    
    if cnt == M:
      return i
  return -1
```

### KNP 알고리즘

### 보이어 무어 알고리즘

