#!/usr/bin/env python3

from typing import List

def summary_ranges(nums: List[int]) -> List[str]:
    ''' Summary Ranges
    
    '''
    if not nums:
        return []
    elif len(nums) == 1:
        return [str(nums[0])]

    group_count = 0
    count = 1
    store = {0: [nums[0]]}
    output = []

    while count < len(nums):
        difference = abs(store[group_count][-1] - nums[count])
        if difference == 0 or difference == 1:
            store[group_count].append(nums[count])
        else:
            group_count = group_count + 1
            store[group_count] = [nums[count]]
        count += 1

    for key in store.keys():
        if len(store[key]) > 1:
            output.append(f'{store[key][0]}->{store[key][-1]}')
        else:
            output.append(str(store[key][0]))

    return output
  
if __name__ == '__main__':
  nums = [0,1,2,3,4,5,7]
  sr = summary_ranges(nums)
  print(sr)
