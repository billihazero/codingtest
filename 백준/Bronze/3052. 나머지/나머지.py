nums = []
for i in range(10):
    a = int(input())
    nums.append(a%42)
numsSet = set(nums)
print(len(numsSet))