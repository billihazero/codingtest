nums = []
i = 9
while i !=0 :
    nums.append(int(input()))
    i -= 1
a = max(nums)
print(a)
print(nums.index(a)+1)