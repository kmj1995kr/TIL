import random
## 함수 선언부
def findMinIdx(ary) :
    retIdx = 0
    for i in range(len(ary)) :
        if (ary[retIdx] > ary[i]) :
            retIdx = i
    return retIdx

## 전역 변수부
before = [ random.randint(10, 99) for _ in range(20) ]
after = []
## 메인 코드부
print('정렬전-->',  before)
for i in range(len(before)) :
    minIdx = findMinIdx(before)
    after.append(before[minIdx])
    del(before[minIdx])
print('정렬후-->',  after)
​