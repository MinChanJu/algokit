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

def parametric_search(nums, target, min_max='min'):           # 중복된 target중 최소값
  if (min_max == 'min'): return parametric_search_min(nums, target)
  if (min_max == 'max'): return parametric_search_max(nums, target)
  raise ValueError('min_max는 \'min\' 또는 \'max\'여야 합니다.')