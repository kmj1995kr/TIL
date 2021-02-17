# stack is not a inifitely sized list
stack = [None, None, None, None, None]
top = -1

# Push = inserting an element
top += 1
stack[top] = 'A'

top += 1
stack[top] = 'B'

top += 1
stack[top] = 'C'

print(stack)

# Pop = extracting an element
data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)

print(stack)