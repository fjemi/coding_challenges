#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
UTILS_DIR = abspath('..') + '/utils'
sys.path.insert(0, UTILS_DIR)

from merge_two_arrays import merge_two_arrays

def test_merge_two_arrays():
  '''
  '''
  
  test_cases = [
    {'a': [], 'b': [], 'result': []},
    {'a': [], 'b': [0], 'result': [0]},
    {'a': [1, 2, 3], 'b': [1, 2, 4], 'result': [1, 1, 2, 2, 3, 4]}
  ]
  
  for test in test_cases:
    mta = merge_two_arrays(test['a'], test['b'])
    assert mta == test['result']
  
