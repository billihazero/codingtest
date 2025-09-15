N = int(input())
S = input()
nums = list(map(int, S))
total = 0
for i in range (N):
        total += nums[i]
print(total)
