## 함수 선언부
def isStackFull():
    global stack, top, SIZE
    if (top >= SIZE-1):
        return True
    else:
        return False
    
def push(data) :
    global stack, top, SIZE
    if (isStackFull()):
        print("Stack is Full")
        return
    top += 1
    stack[top] = data
    return stack

def isStackEmpty():
    global stack, top, SIZE
    if top < 0:
        return True
    else:
        return False

def pop():
    global stack, top, SIZE
    if (isStackEmpty()):
        print("Stack is Empty")
        return
    print("Pop Value: ", stack[top])
    stack[top] = None
    top -= 1
    return stack

## 전연 변수부
SIZE = 3
stack = [None for _ in range(SIZE)]
top = -1


## 메인 코드부
if __name__ == "__main__":
    # 스택 사이즈가 3이기 때문에 마지막 push 0일때는 Stack is Full 메세지 리턴
    print(push(5))
    print(push(3))
    print(push(1))
    print(push(0))

    # 4번째 pop에서는 Stack is Empty 메세지 리턴
    print(pop())
    print(pop())
    print(pop())
    print(pop())