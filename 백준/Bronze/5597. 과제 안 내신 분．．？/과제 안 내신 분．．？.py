nums = [0] * 30
for i in range(30-2):
    a = int(input())
    nums[a-1] = 1

b = nums.index(0,0,30)+1
print(b)
c = nums.index(0,b+1,30) +1
print(c)