N, X = map(int, input().split(" "))
list = list(map(int, input().split(" ")))
a = []
for i in list:
    if i < X:
        a.append(i)
print(*a, sep=' ')