#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

@dataclass
class SparseVector:
  '''1570. Dot Product of Two Sparse Vectors
  https://leetcode.com/problems/dot-product-of-two-sparse-vectors/submissions/
  '''
  nums: List[int] = None
  store: int = 0    

  def dot_product(self, vector: 'SparseVector') -> int:
    '''Return the dotProduct of two sparse vectors
    '''

    for i in range(len(self.nums)):
      self.store += self.nums[i] * vector.nums[i]

    return self.store
  
if __name__ == '__main__':
  v1 = SparseVector([1,2,3])
  v2 = SparseVector([1,2,3])
  DP = v1.dot_product(v2)
  print(v1, v2, DP)
