import sys
input = sys.stdin.readline
class Queue:
    def __init__(self):
        self.items=[]
        self.front_index = 0
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == self.front_index:
            return -1
        else:
            x = self.items[self.front_index]
            self.front_index+=1
            return x
    def size(self):
        return len(self.items[self.front_index:])
    def empty(self):
        if len(self.items) == self.front_index:
            return 1
        else:
            return 0
    def front(self):
        if len(self.items) == self.front_index:
            return -1
        return self.items[self.front_index]
    def back(self):
        if len(self.items) == self.front_index:
            return -1
        return self.items[-1]

num = int(input())

queue = Queue()
for _ in range(num):
    order = input().split()
    
    match order[0]:
        case 'push':
            x = order[1]
            queue.push(x)
        case 'pop':
            print(queue.pop())
        case 'size':
            print(queue.size())
        case 'empty':
            print(queue.empty())
        case 'front':
            print(queue.front())
        case 'back':
            print(queue.back())