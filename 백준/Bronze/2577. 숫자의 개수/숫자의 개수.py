A = int(input())
B = int(input())
C = int(input())

total = A * B * C
lst = list(map(int, str(total)))
cnt = 0 # 각 숫자의 개수
for i in range(10):
    cnt = lst.count(i)
    print(cnt)