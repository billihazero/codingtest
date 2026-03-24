import sys
input = sys.stdin.readline

N = int(input())


lst = []
end = 0

for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        lst.append(order[1])
    elif order[0] == 'pop':
        if(len(lst) == end):
            print(-1)
        else:
            print(lst[end])
            end+=1
    elif order[0] == 'size':
        print(len(lst)-end)
    elif order[0] == 'empty':
        if (len(lst)-end) == 0 :
            print(1)
        else: print(0)
    elif order[0] == 'front':
        if (len(lst)-end) == 0 :
            print(-1)
        else:    
            print(lst[end])
    elif order[0] == 'back': 
        if (len(lst)-end) == 0 :
            print(-1)
        else:    
            print(lst[len(lst)-1])
    else:
        print("잘못된 질문입니다.")