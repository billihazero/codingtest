n = int(input()) 
case = []

for _ in range(n):
    case = input()
    t = 0
    sum = 0
    for i in range(len(case)):
        if case[i] == 'X':
            t=0
        else:
            t+=1
            sum = sum+t
    print(sum)