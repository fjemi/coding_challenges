#!usr/bin/env python3

from typing import List, Any
from dataclasses import dataclass


@dataclass
class TreeNode:
  val: int = None
  left: Any = None
  right: Any = None
  
  
def list_to_treenode(l: List[int]) -> TreeNode:
  '''create a binary tree from a list of integers'''

  '''
  if len(l) == 1:
    return TreeNode(l[0])
  elif len(l) == 2:
    return TreeNode(l[0], TreeNode(l[1]))
  elif len(l) == 3:
    return TreeNode(l[0], TreeNode(l[1]), TreeNode(l[2]))
  '''

  
  store = {}
  steps = [1, 2]
  for i in range(len(l)):
    # set left chid
    try:
      left = l[steps[-2]]
    except:
      left = None
    # set right child
    try:
      right = l[steps[-1]]
    except:
      right = None
    # add node and children to store
    if left is not None and right is not None:
      store[f'{i}_{l[i]}'] = [f'{steps[-2]}_{left}', f'{steps[-1]}_{right}']
    # update steps
    steps.extend([steps[-1] + 1, steps[-1] + 2])
  
  print(store)
  
  for key in reversed(store.keys()):
    for i in range(len(store[key])):
      print(store[key][i])
      try:
        print(store[store[key][i]])
      except:
        pass
      
def model(root: TreeNode) -> bool:
  if root.left == root.right:
    return True  
  return False


if __name__ == '__main__':
  inputs = [
    [1],
    [1,2],
    [1,2,2],
    [1,2,2,3,4,4,3]
  ]
  for i in inputs:
    print(i)
    i = list_to_treenode(i)
    #print(model(i))
