'''Find the Volume of Each Lake Created by Rainwater
https://techdevguide.withgoogle.com/resources/volume-of-water/#code-challenge
'''

# Data visualizaton
#import matplotlib.pyplot as plt
#from matplotlib import rc
#import seaborn as sns
# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hinting
from typing import List, Dict

@dataclass
class Model:
  '''Determine the amount of rainwater that can be collected 
  between various mountain range heights
  '''
  heights: List[int]
  data: Dict = field(default_factory=lambda: {})
  volume: List = field(default_factory=lambda: [])
  
  def __post_init__(self):
    '''Execute after initializing the class
    '''
    
    # Set store keys
    self.data = {}
    for i in range(len(self.heights)):
      self.data[i] = []
      
    # Indices to ignore in inner loop
    ignore_index = []
    
    for i in range(len(self.heights)):
      index_visited = []
      height_visited = []
      volume = []
      max_height = 0
      
      for j in range(i, len(self.heights)):
        # Skip ignored indices
        if j not in ignore_index and i != j:
          index_visited.append(j)
          height_visited.append(self.heights[j])
          # Set max range height/index. Exclude the first index in range
          if self.heights[j] > max_height and j != i:
            max_height = self.heights[j]
          
          # Store possible volume
          volume.append(self.heights[i] - self.heights[j])
          
          ignore_index.append(j)
          
        # Exit inner loop
        if self.heights[j] > self.heights[i]:
          break
        
      # Set the max heights
      if height_visited != []:
        max_height = max(height_visited)
        
        if max_height > self.heights[i]:
          max_height = self.heights[i]
      
      data = {
        'index': i,
        'indices_visited': index_visited,
        'height': self.heights[i],
        'heights_visited': height_visited,
        'volume': volume,
        'max_height': max_height
      }
      
      for k in reversed(range(len(data['volume']))):
        if data['volume'][k] <= 0:
          for key in data:
            if type(data[key]) is list:
              data[key] = data[key][:k]
      
      # Reset the max heights
      if data['max_height'] < data['height']:
        if len(data['heights_visited']) > 0:
          data['max_height'] = max(data['heights_visited'])
      
      # Slice lists in the data object at max range height
      for k in reversed(range(len(data['heights_visited']))):
        if data['heights_visited'][k] == data['max_height']:
          for key in data:
            # Check if key/value is a list
            if type(data[key]) is list:
              data[key] = data[key][:k]
              
      # Reset volume
      if len(data['volume']):
        for k in range(len(data['volume'])):
          data['volume'][k] = data['max_height'] - data['heights_visited'][k]
          self.volume.append(data['volume'][k])
        
      self.data[i].append(data)


if __name__ == '__main__':
  HEIGHTS = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
  M = Model(HEIGHTS)
  print(json.dumps(asdict(M), indent=2))
