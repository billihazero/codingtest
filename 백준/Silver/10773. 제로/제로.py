import sys

input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.items = []
    def push(self, value):
        self.items.append(value)
    def pop(self):
        self.items.pop()
    def sum(self):
        return sum(self.items)
    
num = int(input())

stack = Stack()
for _ in range(num):
    score = int(input())
    if score != 0:
        stack.push(score)
    else:
        stack.pop()

print(stack.sum())