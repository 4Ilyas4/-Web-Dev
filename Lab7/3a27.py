def big_diff(nums):
  min = nums[0]
  max = nums[0]
  for i in nums:
    if(i<min):
      min = i
    if(i>max):
      max = i
  return max - min
