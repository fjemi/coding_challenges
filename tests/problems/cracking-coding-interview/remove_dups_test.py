#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')
get_modules_dir('utils/')
from remove_dups import remove_dups
from array_to_linked_list import array_to_linked_list

def remove_dups_test() -> None:
  '''
  '''
  test_cases = [
    {
      'input': array_to_linked_list([2, 3, 3, 2, 2, 3, 1, 3, 3, 3]), 
      'result': array_to_linked_list([2, 3, 1])
    }
  ]
  
  for test in test_cases:
    RD = remove_dups(test['input'])
    assert RD == test['result']

  return None