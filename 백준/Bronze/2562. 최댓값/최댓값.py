v = []
for _ in range(9):
    v.append(int(input()))

max_here = v.index(max(v))
print(v[max_here])
print(max_here+1)