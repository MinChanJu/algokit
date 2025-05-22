def parametric_search_max(nums, target):           # 중복된 target중 최대값
  s = 0
  e = len(nums) - 1
  
  while s <= e:
    mid = (s + e) // 2
    if target >= nums[mid]: s = mid + 1
    else: e = mid - 1
  
  return e


def parametric_search_min(nums, target):           # 중복된 target중 최소값
  s = 0
  e = len(nums) - 1
  
  while s <= e:
    mid = (s + e) // 2
    if target > nums[mid]: s = mid + 1
    else: e = mid - 1
  
  return s

def parametric_search(nums, target):           # 중복된 target중 최소값
  s = 0
  e = len(nums) - 1
  
  while s <= e:
    mid = (s + e) // 2
    if target > nums[mid]: s = mid + 1
    else: e = mid - 1
  
  return s