## 함수 선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False
    pass


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() == True:
        return ("Queue is Full")
    else:
        rear += 1
        queue[rear] = data 
    return queue

## 전역 변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인 코드부
print(enQueue('a'))
print(enQueue('a'))
print(enQueue('a'))
print(enQueue('a'))
print(enQueue('a'))