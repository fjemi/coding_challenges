#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
PROBLEMS_DIR = abspath('..') + '/problems/leetcode/'
sys.path.insert(0, PROBLEMS_DIR)

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
