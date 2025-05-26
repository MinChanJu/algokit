def binary_search(nums, target):
  s = 0
  e = len(nums) - 1
  
  while s <= e:
    mid = (s + e) // 2
    if target < nums[mid]: e = mid - 1
    elif target > nums[mid]: s = mid + 1
    else: return mid
  
  return None