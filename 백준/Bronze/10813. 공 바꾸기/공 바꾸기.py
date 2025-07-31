N,M = map(int, input().split(" "))
basket = list(x for x in range(1,N+1))
for l in range(M):
    i,j =  map(int, input().split(" "))
    m = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = m
print(*basket, sep=' ')