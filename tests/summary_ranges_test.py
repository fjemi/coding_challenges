#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
PROBLEMS_DIR = abspath('..') + '/problems/leetcode'
sys.path.insert(0, PROBLEMS_DIR)

from summary_ranges import summary_ranges

def test_summary_ranges():
  '''
  '''
  
  test_cases = [
      {
        'range': [-3,-2,0,2,3,4,6,8,9], 
        'result': ['-3->-2', '0', '2->4', '6', '8->9']
      },
      {
        'range': [-2147483648,-2147483647,2147483647], 
        'result': ['-2147483648->-2147483647', '2147483647']
      },
      {'range': [0], 'result': ['0']},
      {'range': [-1], 'result': ['-1']},
      {'range': [0,1,2,3,4,5,7], 'result': ['0->5', '7']}
  ]

  for test in test_cases:
    sr = summary_ranges(test['range'])
    assert sr == test['result']
  
  
