#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('utils/')

from list_combinations import list_combinations

def test_list_combinations():
  '''
  '''
  
  test_cases = [
    {'a': [1], 'b': [2], 'result': ['12']},
    {'a': [], 'b': [0], 'result': ['0']},
    {
        'a': [1,2,3], 
        'b': [5,4,6], 
        'result': ['15', '14', '16', '25', '24', '26', '35', '34', '36']
    }
  ]
  
  for test in test_cases:
    lc = list_combinations(test['a'], test['b'])
    assert lc == test['result']
  
