#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
UTILS_DIR = abspath('../..') + '/utils'
sys.path.insert(0, UTILS_DIR)

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
  
