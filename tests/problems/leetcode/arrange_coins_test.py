#!/usr/bin/env python3

from get_problems_dir import get_problems_dir
PROBLEMS_DIR = get_problems_dir()

from arrange_coins import arrange_coins

def test_arrange_coins():
  '''
  '''
  test_cases = [
    {'n': 0, 'result': 0}, {'n': 1, 'result': 1}, 
    {'n': 5, 'result': 2}, {'n': 8, 'result': 3}
  ]
  
  for test in test_cases:
    AC = arrange_coins(test['n'])
    assert AC == test['result']
