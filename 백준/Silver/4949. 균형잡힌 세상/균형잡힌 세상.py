class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
    def len(self):
        return len(self.items)

while True:
    s = input()
    if s == '.':
        break

    stack = Stack()
    is_valid = True

    for i in range(len(s)):
        if s[i] == '(' or s[i] =='[':
            stack.push(s[i])
        elif s[i] == ')':
            top = stack.pop()
            if top != '(':
                print('no')
                is_valid = False
                break
        elif s[i] == ']':
            top = stack.pop()
            if top!= '[':
                print('no')
                is_valid = False
                break

    if is_valid == True :
            if stack.len() == 0:
                print('yes')
            else:
                print('no')
        
        
    
