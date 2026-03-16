import sys
input = sys.stdin.readline

num = int(input()) # 명령 수

class Stack:
    def __init__(self):
        self.items =[]
    
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        if(len(self.items) == 0):
            return 1
        else:
            return 0
    def top(self):
        if (len(self.items) == 0):
            return -1
        else:
            return self.items[-1]
        

stack = Stack()
for _ in range(num):
    order = input().split()

    match order[0]:
        case 'push':
            x = int(order[1])
            stack.push(x)
        case 'pop':
            print(stack.pop())
        case 'size':
            print(stack.size())
        case 'empty':
            print(stack.empty())
        case 'top':
            print(stack.top())
