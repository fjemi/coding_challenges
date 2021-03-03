#class MovingAverage:

    #def __init__(self, size: int):
        #"""
        #Initialize your data structure here.
        #"""
        

    #def next(self, val: int) -> float:
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


#!usr/bin/env python3

from dataclasses import dataclass, field
from typing import List

@dataclass
class MovingAverage:
  size: int
  nums: List[int] = field(default_factory=lambda: [])
  average: float = 0

  def next(self, val: int):
    ''''''
    self.nums.append(val)
    if len(self.nums) <= self.size:
      self.average = sum(self.nums) / len(self.nums)
    else:
      self.average = sum(
        self.nums[len(self.nums) - self.size:]) / self.size
      
    #print(self)
    return self.average
  
if __name__ == '__main__':
  mv = MovingAverage(3)
  mv.next(1)
  mv.next(10)
  mv.next(3)
  mv.next(5)
