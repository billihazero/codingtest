N = int(input())

class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == 0:
            return -1
        else: 
            #맨 앞 제거
            self.front_index+=1

            #그 다음 값 저장
            x = self.items[self.front_index]
            self.front_index+=1
            
            #뒤에 붙이기
            self.items.append(x)
    def len(self):
        return len(self.items) - self.front_index
    def front(self):
        return self.items[self.front_index]

queue = Queue()
for i in range(N):
    queue.push(i+1)

while queue.len() > 1 :
    queue.pop()

print(queue.front())