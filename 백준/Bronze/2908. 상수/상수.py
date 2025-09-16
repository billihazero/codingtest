a,b = map(int, input().split())
reversed_a = int(str(a)[::-1])
reversed_b = int(str(b)[::-1])

print(reversed_a) if reversed_a > reversed_b else print(reversed_b)