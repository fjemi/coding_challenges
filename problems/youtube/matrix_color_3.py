'''Tree treversal example (recursive) method 3
www.youtube.com/watch?v=IWvbPIYQPFM
'''

# Data modeling
from dataclasses import dataclass, field, asdict
import json
import jsbeautifier
# Type hinting
from typing import List, Dict, Any
# Linear algebra
import numpy as np

# jsbeautifier settings
opts = jsbeautifier.default_options()
opts.indent_size = 2

@dataclass
class TreeTraversal:
  '''Given a a an mxn matrix of colors (tree), identify the number of 
  connections between adjacent (up/down, left/right, or diagonal) 
  colors of the same kind
  
  Identify edges, sides, and corners
  '''
  tree: List[List]
  nodes: List[List] = field(default_factory=lambda: [])
  adjacencies: Dict = field(default_factory=lambda: [])
  connections: Dict = field(default_factory=lambda: {})
  connections_count: Dict = field(default_factory=lambda: {})
  
  
  def __post_init__(self):
    '''Set the corner, edge, and inner nodes of the matrix
    '''
    
    # Convert the list to a numpy array
    a = np.array(self.tree)
    # Array dimensions
    m, n = a.shape[0], a.shape[1]
    
    for i in range(m):
      for j in range(n):
        node_value = self.tree[i][j]
        # Store fo connected nodes; adjacent nodes with the same value
        self.connections[self.tree[i][j]] = []
        self.connections_count[self.tree[i][j]] = 0
        # List each node
        self.nodes.append([i, j])
    
    # Store parent/child (adjacent) nodes
    connections = {}
    for node in self.nodes:
      # Set child attributes for for each parent
      for i in range(node[0] - 1, node[0] + 2):
        for j in range(node[1] - 1, node[1] + 2):
          # Ignore indecies outside the tree dimensions
          if i in range(0, m) and j in range(0, n):
            if (i, j) != (node[0], node[1]):
              parent_value = self.tree[node[0]][node[1]]
              child_value = self.tree[i][j]
              connected = False
              # Check if nodes are connected
              if parent_value == child_value and node != [i, j]:
                connected = True
                connections[str(sorted([node, [i, j]]))] = parent_value
              self.adjacencies.append({
                'parent_node': node,
                'parent_value': parent_value,
                'child_node': [i, j],
                'child_value': child_value,
                'connected': connected
              })
              
    for key in connections.keys():
      self.connections[connections[key]].append(key)
      
    # Count the number of connections
    for connection in self.connections:
      self.connections_count[connection] = len(self.connections[connection])
      
  
if __name__ == '__main__':
  tree = [
    ['blue', 'green', 'red'],
    ['blue', 'blue', 'green'],
    ['red', 'blue', 'green'],
    ['red','red', 'blue']
  ]
  TT = TreeTraversal(tree)
  print(jsbeautifier.beautify(json.dumps(asdict(TT)), opts))
