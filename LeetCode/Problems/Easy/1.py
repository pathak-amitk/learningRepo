# Two Sum
nums = [2,7,11,15]
#nums = [3,3]
nums = [3,2,3]

target=6

a = {}

for i,num in enumerate(nums):
    if target-num in a:
        print(i, a[target-num])
    else:
        a[num] = i