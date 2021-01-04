'''https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/
'''

import string
# Type hints
from typing import List, Dict, Any
# Data modeling
from dataclasses import dataclass, field, asdict
import json
# List computations
from functools import reduce


@dataclass
class Model:
  '''Yahtzee upper section scoring
  '''
  dice: List[int]
  n: int = None
  roll: Dict = field(default_factory=lambda: {})
  max_score: int = 0
  
  def __post_init__(self):
    '''Score the roll by multiply the numbers 1-6 by their
    corresponding dice in the roll
    '''
    
    # Set the max dice in the list
    self.n = max(self.dice)
    
    for i in range(1, self.n):
      # Store counte/scores
      self.roll[i] = {} 
      
      # Count number of dice that match numbers 1 - n
      self.roll[i]['matching_dice'] = list(filter(lambda x: x == i, self.dice))
      
      # Multiply dice count by number (1-n)
      if len(self.roll[i]['matching_dice']) > 0:
        self.roll[i]['score'] = len(self.roll[i]['matching_dice']) * i
      else:
        self.roll[i]['score'] = 0
      
      # Set the max score
      if self.roll[i]['score'] > self.max_score:
        self.max_score = self.roll[i]['score']
        
    
if __name__ == '__main__':
  dice_roll = [
    [2, 3, 5, 5, 6]
    ]
  for roll in dice_roll:
    M = Model(roll)
    print(json.dumps(asdict(M), indent=2))
    
