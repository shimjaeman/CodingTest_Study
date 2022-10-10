import sys

def push(x):
    stack.append(x)

def pop(): 
    return stack.pop() if stack else -1

def top(): 
    return stack[-1] if stack else -1

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

a = int(sys.stdin.readline())
stack = []

for _ in range(a):
    order_input = sys.stdin.readline().split()
    order = order_input[0]

    if order == "push" : push(order_input[1])
    elif order == "pop" : print(pop())
    elif order == "top" : print(top())
    elif order == "size" : print(size())
    elif order == "empty" : print(empty())
