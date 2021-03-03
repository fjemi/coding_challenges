#!usr/bin/env python3

from dataclasses import dataclass
from typing import List
from random import choice

@dataclass
class Solution:
  w: List[int]
  
  def pickIndex(self) -> int:
    if len(self.w) == 1:
      return 0
    
    store = []
    dupe_count = 0 
    weighted = ''
      
    for i in range(len(self.w)):
      value = str(self.w[i])
      if value in store:
        value = f'{value}_{dupe_count}'
        dupe_count += 1
      store.append(value)
      nums = f'{value}/' * self.w[i]
      weighted = weighted + nums
    weighted_choices = weighted[:-1].split('/')

    pick = choice(weighted_choices)
    pick_index = store.index(pick)
    print({'weights': self.w, 'random_pick': pick, 'pick_index': 
store.index(pick)})
    return store.index(pick)
  
if __name__ == '__main__':
  w = [10,7,8,10]
  solution = Solution(w)
  print(solution.pickIndex())
  
    



