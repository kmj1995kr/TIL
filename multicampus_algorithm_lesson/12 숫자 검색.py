import random

def seqSearch(ary, data):
    pos = -1

    for i in range(len(ary)):
        if (ary[i] == data):
            pos = i
            break
    
    return pos

def seqSearchMulti(ary, data):
    pAry = []
    for i in range(len(ary)):
        if(ary[i] == data):
            pAry.append(i)
    return pAry


dataAry = [ random.randint(11,99) for _ in range(50) ]
print(dataAry)

position = seqSearch(dataAry, 99)
print(position)

postAry = seqSearchMulti(dataAry, 50)
print(posAry)

import random

# 중복된 데이터가 없다고 가정
# (1) 1개만 찾는 값이 있다
# (2) 1개만 찾으면 된다.
def seqSearch(ary, data) :
    pos = -1
    for i in range(len(ary)) :
        if (ary[i] == data) :
            pos = i
            break
    return  pos

def seqSearchMulti(ary, data) :
    pAry = []
    for i in range(len(ary)) :
        if (ary[i] == data) :
            pAry.append(i)
    return  pAry

dataAry = [ random.randint(11,50)  for _ in range(50)]
print(dataAry)

position = seqSearch(dataAry, 50)
print(position)

posAry = seqSearchMulti(dataAry, 50)
print(posAry)
​