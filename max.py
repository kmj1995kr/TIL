"""
n = 배열의 크기
k = 연속된 수의 갯수
arr = 베열
-----------------------------
arr = [1, 4, 2, 10, 23, 3, 1 0, 20]
n = 8
k = 4
"""
def find_max(k, arr):
    n = len(arr)
    # 맨 앞 k개 숫자의 합
    temp = maximum = sum(arr[0:k])

    for i in range(0, n-k):
        # 배열에서 맨 왼쪽 숫자를 빼고 맨 오른쪽 숫자를 더하면서 진행
        temp = temp - arr[i] + arr[i+k]
        if temp > maximum:
            maximum = temp
    return maximum

print(find_max(4, [1, 4, 2, 10, 23, 3, 1, 0, 20]))