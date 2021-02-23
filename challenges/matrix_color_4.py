'''ree treversal example (recursive).
www.youtube.com/watch?v=IWvbPIYQPFM
'''

# Array
import numpy as np
# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hinting
from typing import List, Dict, Any

@dataclass
class TreeTraversal:
  '''Class for counting connections (up/down and left/right)
  between nodes in a tree'''
  tree: List[List]
  connected_count: Dict = field(default_factory=lambda: {})
  connected_nodes: Dict = field(default_factory=lambda: {})
  
  def __post_init__(self):
    '''Execute after the class is initialized
    '''
    # Convert list to np array and set properties
    a = np.array(self.tree)
    m = a.shape[0]
    n = a.shape[1]
    
    # Create store for connected nodes
    for node in np.unique(a):
      self.connected_count[node] = 0
    
    # Iterate over elements within the array
    for i in range(m):
      for j in range(n):
        
        # Set diagonals to ignore
        diagonals = [
          [eval('i - 1'), eval('j - 1')],
          [eval('i, j')],
          [eval('i + 1'), eval('j + 1')],
          [1, eval('j + 1')],
          [eval('i + 1'), 1]
        ]
        
        # Loop through adjacent nodes
        for k in range(i - 1, i + 2):
          for l in range(j - 1, j + 2):
            if (k in range(m) and 
                l in range(n) and 
                [i, j] != [k, l] and 
                [k, l] not in diagonals
            ):
              if a[i][j] == a[k][l]:
                connection = sorted([[i, j], [k, l]])
                self.connected_nodes[f'{[connection]}'] = a[i][j]
    
    # Count the number of unique connections          
    for value in self.connected_nodes.values(): 
      self.connected_count[value] += 1 

        

if __name__ == '__main__':
  tree = [
    ['blue', 'green', 'red'],
    ['blue', 'blue', 'green'],
    ['red', 'blue', 'green'],
    ['red','red', 'blue']
  ]
  TT = TreeTraversal(tree)
  print(json.dumps(asdict(TT), indent=2))
