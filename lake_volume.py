'''
  Find the Volume of Each Lake Created by Rainwater
  https://techdevguide.withgoogle.com/resources/volume-of-water/#code-challenge
'''

# Data analysis
#import pandas as pd
#import numpy as np
# Data visualizaton
#import matplotlib.pyplot as plt
#from matplotlib import rc
#import seaborn as sns
# Data modeling
from dataclasses import dataclass, field
import json
# Type hinting
from typing import List

@dataclass
class LakeVolume:
  '''
  Determine the amount of rainwater collected in a lake with areas of various 
sizes
  '''
  heights: List[int]
  volumes: List[int] = field(default_factory=lambda: [])
  total_volume: int = None
  visited: List[int] = field(default_factory=lambda: []) # Add visted indices to a list to skip later
  
  def __post_init__(self):
    '''
      Execute after initializing the class
    '''
    # Add a zero to the beginning/end of the array
    self.heights.append(0)
    self.heights.insert(0, 0)
    
    # Create dictionary to store data
    json_data = {}
    for i in range(len(self.heights)):
      json_data[i] = []
    print(json_data, '\n')
    
    # # Determine the lake volumes
    for i in range(len(self.heights) - 1):
      #print('\n', i, self.heights[i])
      count = i
      while count < len(self.heights) - 1:
        count = count + 1
        try:
          # Exit loop under the conditions that
          # count exceeds heights size or current and visited are equal
          if self.heights[i] < self.heights[count] and self.heights[i] != self.heights[count]:
            break
          
          # Add index/value data to JSON
          if i not in self.visited:
            json_data[i].append({
              'current_value': self.heights[i], 
              'visted_value': self.heights[count], 
              'visited_index': count,
              'current_visited_diff': self.heights[count] - self.heights[i]
            })

          # Added visited indices to skip them
          self.visited.append(count)

        except:
          pass 
        
    print(json.dumps(json_data, indent=2))
    print(self.visited)
    

if __name__ == '__main__':
  heights = [
    1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2
  ]
  lv = LakeVolume(heights)
  print(lv)

