katok = ['다현', '정연', '쯔위', '사나', '지효']

def  insert_data(position, friend) :
    katok.append(None) # 빈칸 추가
    kLen = len(katok)

    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend
    
    

# insert_data(2, '솔라')
# print(katok)
# insert_data(5, '재남')
# print(katok)


def delete_data(position):
    katok[position] = None
    kLen = len(katok)

    for i in range(position, kLen-1):
        katok[i] = katok[i+1]
        katok[i+1] = None

    katok.pop(len(katok)-1)


delete_data(2)
print(katok)