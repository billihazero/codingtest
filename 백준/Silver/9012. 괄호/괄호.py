class Stack:
    def __init__(self):
        self.items =[]
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) != 0:
            self.items.pop()
        else: 
            return print('NO')
    def len(self):
        return len(self.items)

num = int(input())
for _ in range (num):
    ps = list(input())
    stack = Stack()
    is_valid = True
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.push('(')
        else:
            if stack.len() == 0:
                print('NO')
                is_valid = False
                break
            else:
                stack.pop()
    if is_valid == True:
        if stack.len() == 0:
            print('YES')
        else:
            print('NO')
