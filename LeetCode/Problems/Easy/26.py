#Remove Duplicates from Sorted Array
nums = [1]

slow=0
fast=1

while fast < len(nums):
  if nums[fast] != nums[slow]:
    slow +=1
    nums[slow] = nums[fast]

  fast +=1

print(slow+1, nums)

