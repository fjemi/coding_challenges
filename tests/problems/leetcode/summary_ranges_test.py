#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')

from summary_ranges import summary_ranges

def test_summary_ranges() -> None:
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
    SR = summary_ranges(test['range'])
    assert SR == test['result']

  return None
