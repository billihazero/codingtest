M =int(input())
nums =  list(map(float, input().split(" ")))
score = max(nums)
total = 0

for i in range(M):
        nums[i] = nums[i] / score * 100
        total +=nums[i]

print(total / M)

