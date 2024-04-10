def count_evens(nums):
  n = 0
  for el in nums:
    if(el%2==0):
      n += 1
  return n