N= int(input())
for i in range (N):
    a,b =input().split()
    a = int(a)
    s = len(b) # b의 길이
    total = []
    for x in range(s):
        total += b[x] * a
    print(''.join(total))