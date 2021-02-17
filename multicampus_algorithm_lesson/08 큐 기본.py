## enQueue - entering a queue
queue = [None] * 3
front = rear = -1

rear += 1
queue[rear] = 'A'
rear += 1
queue[rear] = 'B'
rear += 1
queue[rear] = 'C'

## deQueue - exiting a queue
front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)

rear += 1
queue[rear] = 'D'

print(queue)
