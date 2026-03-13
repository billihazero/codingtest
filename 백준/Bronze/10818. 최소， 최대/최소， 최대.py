num = int(input())

v = list(map(int, input().split()))

if len(v) != num:
    raise ValueError('입력 개수가 맞지 않습니다.') 

print(min(v),  max(v))