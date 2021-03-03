#!usr/bin/env python3

from typing import List

def find_smallest(array: List[int]) -> int:
  '''returns the smallest number in an array'''
  return min(array)

def second_smallest(array: List[int]) -> int:
  '''returns the second smallest number in an array'''
  smallest = float('inf')
  second_smallest = float('inf')
  
  for i in range(0, len(array)):
    if array[i] < smallest:
      second_smallest = smallest
      smallest = array[i]
    elif array[i] < second_smallest:
      second_smallest = array[i] 
  return second_smallest
  
def nth_order_statistic(array: List[int], n: int) -> int:
  '''returns the nth (1-n) element of a sorted list'''
  array.sort()
  return array[n - 1]
  

if __name__ == '__main__':
  array = [1,6,3,9,2,5]
  n = 2
  smallest = find_smallest(array)
  second_smallest = second_smallest(array)
  nth_order = nth_order_statistic(array, n)
  print({
    'array': array,
    'n': n,
    'smallest_element': smallest,
    'second_smallest': second_smallest,
    'nth_order_statistic': nth_order
  })
