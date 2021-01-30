#!/usr/bin/env python

from typing import List
from dataclasses import dataclass, field


@dataclass
class MedianFinder:
  array: List[int] = field(default_factory=lambda: [])
  
  def __post_init__(self) -> None:
    '''sort the array if class intialized with data'''
    self.array.sort()
   
  def addNum(self, num: int) -> None:
    '''adds a number to a list in sorted order'''
    # non-empty array
    if len(self.array) == 0:
      self.array.append(num)
    else:
      # insert the num into a sorted array
      for i in range(len(self.array)):
        if self.array[i] >= num:
          self.array.insert(i, num)
          break  
        elif num >= self.array[len(self.array) - 1]:
          self.array.insert((len(self.array) - 1) + 1, num)
          break

  def findMedian(self) -> int:
    '''returns the median of numbers withing a list'''
    median = 0
    array_length = len(self.array)

    # array has no elements
    if not array_length:
      return median
    
    # copy array to wotrk around dataclass immutability
    array = self.array[:]
    
    # array has one element
    if array_length == 1:
      median = array[0]
    # array with 2 
    elif array_length == 2:
      median = sum(array) / 2
    # array with 3 or more elements
    else:
      # odd number of array elements
      if array_length % 2 != 0:
        middle = int(array_length / 2)
        median = array[middle]
      # even number of array elements
      else:
        middle = int(array_length / 2)
        left = middle
        right = middle + 1
        median = (array[left - 1] + array[right - 1]) / 2
        
    return median

 
if __name__ == '__main__':
  data = MedianFinder([-1])
  data.addNum(-2)
  data.addNum(-3)
  data.addNum(-4)
  data.addNum(-5)
  print(data)
  print({'median': data.findMedian()})
  
  data = MedianFinder([3, 2, 1])
  print(data)
  print({'median': data.findMedian()})
