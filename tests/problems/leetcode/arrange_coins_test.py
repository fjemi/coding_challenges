#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')

from arrange_coins import arrange_coins

def test_arrange_coins() -> None:
  '''
  '''
  test_cases = [
    {'n': 0, 'result': 0}, {'n': 1, 'result': 1}, 
    {'n': 5, 'result': 2}, {'n': 8, 'result': 3}
  ]
  
  for test in test_cases:
    AC = arrange_coins(test['n'])
    assert AC == test['result']

  return None