import random

def binSearch(ary, data) :
    global count
    pos = -1
    start = 0
    end = len(ary) -1
    while (start <= end) :
        count += 1
        mid = (start + end ) // 2
        if (ary[mid] == data) :
            return mid
        elif (ary[mid] < data) :
            start = mid + 1
        else :
            end = mid -1
    return pos

count = 0
dataAry = [ random.randint(100000, 999999) for _ in range(1000000)]
dataAry.sort()

position = binSearch(dataAry, 111111)
print(position, dataAry[position], ' 횟수-->', count)

#print(dataAry[0:10], dataAry[-10:-1])

dataAry = [ random.randint(10000, 99999) for _ in range(1000000) ]
dataAry.sort()

print(binSearch(dataAry, 11111))