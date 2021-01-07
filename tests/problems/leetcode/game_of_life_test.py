#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')


from game_of_life import game_of_life

def game_of_life() -> None:
  '''
  '''
  test_cases = [
    {
      'input': [[0,1,0],[0,0,1],[1,1,1],[0,0,0]], 
      'result': [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    },
    {
      'input': [[1,1],[1,0]], 
      'result': [[1,1],[1,1]]
    }
  ]
  
  for test in test_cases:
    GoL = game_of_life(test['input'])
    assert GoL == test['result']

  return None