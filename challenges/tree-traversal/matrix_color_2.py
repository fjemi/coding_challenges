'''Tree treversal example (recursive)
www.youtube.com/watch?v=IWvbPIYQPFM
'''

# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hinting
from typing import List, Dict, Any
# Linear algebra
import numpy as np

@dataclass
class Model:
  '''Given a a an mxn matrix of colors (tree), identify the number of 
  connections between adjacent (up/down, left/right, or diagonal) 
  colors of the same kind
  
  Identify edges, sides, and corners
  '''
  tree: List[List]
  connections: Dict = field(default_factory=lambda: {})
  edges: Dict = field(default_factory=lambda: {})
  corners: Dict = field(default_factory=lambda: {})
  insides: List[str] = field(default_factory=lambda: [])
  
  def set_nodes(self):
    '''Set the corner, edge, and inner nodes of the matrix
    '''
    
    # Convert the list to a numpy array
    a = np.array(self.tree)
    # Array dimensions
    m, n = a.shape[0], a.shape[1]
    
    # Store node connections
    for node in np.unique(a):
      self.connections[node] = []
    
    # Set corner nodes
    self.corners = {
      'top_left': '(0, 0)',
      'bottom_left': f'({m}, 0)',
      'top_right': f'(0, {n})',
      'bottom_right': f'({m}, {n})'
    }
    
    # Store for edge nodes
    edges = {
        'right': {},
        'left': {},
        'top': {},
        'bottom': {}
    }
    unique_edges = {}
    
    # Set edge nodes
    for i in range(m):
      edges['right'][str((i, n))] = 1
      edges['left'][str((i, 0))] = 1
      edges['bottom'][str((m, i))] = 1
      edges['top'][str((0, i))] = 1  
        
    # Reset the edge nodes
    for edge in edges.keys():
      self.edges[edge] = list(edges[edge].keys())
      # Remove corner nodes
      for node in self.edges[edge]:
        if node in self.corners.values():
          self.edges[edge].remove(node)
    
    # Set inner nodes
    for i in range(1, m - 1):
      for j in range (1, n - 1):
        self.insides.append(f'({i}, {j})')
        
    
  def find_connections(self):
    '''
    '''
    
    # Check if there are any inner nodes
    if len(self.insides) == 0:
      return None
    
    # Convert a string representation of a node into a list
    node_list = []
    for node in self.insides:
      node_list.append(
        node[1:-1].replace(' ', '').split(',')
      )
    
    for node in node_list:
      # Set value of current node
      current_node = self.tree[int(node[0])][int(node[1])]
      # Search surrounding cells to find connections
      for i in range(int(node[0]) - 1, int(node[0]) + 2):
        for j in range(int(node[1]) - 1, int(node[1]) + 2):
          # Set value of adjacent node
          adjacent_node = self.tree[i][j]
          if current_node == adjacent_node:
            # Set the connected nodes
            connection = sorted([(i, j), (int(node[0]), int(node[1]))])
            # Do not add if already in list
            if connection not in self.connections[current_node] and [i, j] != [int(node[0]), int(node[1])]:
              self.connections[current_node].append(connection)
              print(sorted([(i, j), (int(node[0]), int(node[1]))]))
      
      
if __name__ == '__main__':
  TREE = [
    ['blue', 'green', 'red'],
    ['blue', 'blue', 'green'],
    ['red', 'blue', 'green'],
    ['red','red', 'blue']
  ]
  M = Model(TREE)
  M.set_nodes()
  M.find_connections()
  #print(json.dumps(asdict(M), indent=2))
