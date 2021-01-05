#!/usr/bin/env python3

from typing import List

def top_k_elements(nums, k):
    ''' # 347. Top K Frequent Elements
    https://leetcode.com/problems/top-k-frequent-elements/
    ---
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    '''
    
    
    occurance = {}
    output = {}
    output1 = []
    nums = sorted(nums)
    
    # count the occurances of nums in the list and store in dictionary
    for num in nums:
        if num in occurance.keys():
            occurance[num] += 1
        else:
            occurance[num] = 1
    
    for key in occurance.keys():
        if occurance[key] in output.keys():
            output[occurance[key]].append(key)
        else:
            output[occurance[key]] = [key]
            
    keys = list(sorted(output.keys(), reverse=True))[:k]
    for key in keys:
        output1 = output1 + output[key]
        if len(output1) >= k:
            break
    
    return output1

    if __name__ == '__main__':
        print('TODO: add function call to main block')
