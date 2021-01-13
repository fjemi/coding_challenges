#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')
get_modules_dir('utils/')
from return_kth_to_last import return_kth_to_last
from array_to_linked_list import array_to_linked_list

def return_kth_to_last_test() -> None:
  '''
  '''
  test_cases = [
    {
      'input': array_to_linked_list([2, 3, 3, 2, 2, 5, 1, 3, 3, 3]), 
      'k': 5,
      'result': 5
    }
  ]
  
  for test in test_cases:
    RKtL = return_kth_to_last(test['input'], test['k'])
    assert RKtL == test['result']

  return None