N = int(input())
for _ in range(N): 
    a, str = input().split()
    a=int(a)
    print(''.join(ch * a for ch in str))