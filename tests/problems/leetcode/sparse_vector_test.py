#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')

from sparse_vector import SparseVector

def test_SparseVector() -> None:
  '''
  '''

  a = [1, 0, 0, 2, 3]
  SV = SparseVector(a)
  assert SV.nums == [1, 0, 0, 2, 3]
  assert SV.store == 0
  
  test_cases = [
    {
      'v1': SparseVector([1,0,0,2,3]), 
      'v2': SparseVector([0,3,0,4,0]), 
      'result': 8
    }
  ]

  for test in test_cases:
    SV = SparseVector.dot_product(test['v1'], test['v2'])
    assert SV == test['result']

  return None
