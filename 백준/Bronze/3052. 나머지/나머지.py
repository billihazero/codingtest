nums = []

for _ in range(10):
    s = int(input()) % 42
    if s in nums:
        continue;
    else:
        nums.append(s)

print(len(nums))
