 
'''Find the Volume of Each Lake Created by Rainwater
https://techdevguide.withgoogle.com/resources/volume-of-water/#code-challenge
'''

# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hinting
from typing import List, Dict

@dataclass
class Model:
  '''Determine the amount of water collected between mountain range heights
  '''
  heights: List[int]
  data: List = field(default_factory=lambda: [])
  total_volume: int = 0
  
  def __post_init__(self):
    '''Execute after initializing the class
    '''
    
    data = []
    
    # Store indices of heights that produce volumes to prevent
    # them from being counted multiple times
    volume_height_indices = []
    
    # Loop through heights
    for i in range(len(self.heights)):
      # Store for maximum height in the range
      max_range_height = 0
      max_height_index = 0
      
      # Vist other heights
      for j in range(i, len(self.heights)):
        # Set max height
        if self.heights[j] > max_range_height:
          if i != j:
            max_range_height = self.heights[j]
          max_height_index = j
        
        # Possible volume
        volume = self.heights[i] - self.heights[j]
        
        data.append({
            'index': [i, j],
            'height': [self.heights[i], self.heights[j]], 
            'volume': volume, 
            'max_range_height': max_range_height
          })
        
        # Water can be collected between heights a, b. Where b >= a and
        # the number of heights between a, b is greater than 0
        if self.heights[i] >= self.heights[j] and j not in volume_height_indices:
          volume_height_indices.append(j)
          
        else:
          break
        
    
    # Remove negative volumes
    #data = filter(lambda x: x['volume'] > 0, data)
    
    # Store max height in the range
    max_height = {}
    
    # Reset max range heights
    for item in data:
      if item['max_range_height'] > item['height'][0]:
        item['max_range_height'] = item['height'][0]
      # Add max height to store
      max_height[item['index'][0]] = item['max_range_height']
      
    # Set max range heights using store/indices
    for item in data:
      item['max_range_height'] = max_height[item['index'][0]]
    
    # Remove non-positive volumes
    data = filter(lambda x: x['volume'] > 0, data)
    
    # Store indices that will no longer be added to self.data
    skip_index = []
    
    # Reset and store volumes
    for item in data:
      item['volume'] = item['max_range_height'] - item['height'][1]
      if item['index'][0] not in skip_index:
        self.data.append(item)
        # Determine the total volume
        self.total_volume = self.total_volume + item['volume']
      # Skip future indexes of the same kind
      if item['height'][1] == item['max_range_height']:
        skip_index.append(item['index'][0])
      

if __name__ == '__main__':
  HEIGHTS = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
  M = Model(HEIGHTS)
  print(json.dumps(asdict(M), indent=2))
