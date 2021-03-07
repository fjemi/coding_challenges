#!usr/bin/env python3

from typing import List, Dict


def list_to_tree(l: List[int]) -> Dict:
  '''create a binary tree from a list of integers'''

  # store root and child nodes
  json_store = {}
  # store visited child nodes
  steps = [1, 2]
  
  # create dictionary root and child nodes -> {root: [left, right]}
  # nodes are represented as position_value, where position is 
  # is the index of the value in a list
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
      
    # add root node and children to store
    json_store[f'{i}_{l[i]}'] = {'left': f'{steps[-2]}_{left}', 'right': f'{steps[-1]}_{right}'}
    # update steps with positions for next nodes children
    steps.extend([steps[-1] + 1, steps[-1] + 2])
    
  # reset and trim nodes
  keys = list(json_store.keys())
  
  for key in reversed(keys):
    left = json_store[key]['left']
    right = json_store[key]['right']
    # remove position from child -> position_value
    left_no_underscore = left[left.find('_') + 1:]
    right_no_underscore = right[:right.find('_'):]
    
    try:
      # set the left child for current node
      json_store[key]['left'] = {left_no_underscore: json_store[left]}
      del json_store[left]
    except:
      # if child is None remove the underscore
      json_store[key]['left'] = left[left.find('_') + 1:]
      pass
    
    try:
      # set the right child for current node
      json_store[key]['right'] = {right_no_underscore: json_store[right]}
      del json_store[right]
    except:
      # if child is None remove the underscore
      json_store[key]['right'] = right[right.find('_') + 1:]
      pass
  
  return json_store


def model(tree: Dict) -> bool:
  root = list(tree.keys())[0]
  if tree[root]['left'] == tree[root]['right']:
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
    print(f'input: {i}')
    i = list_to_tree(i)
    print(f'tree: {i}')
    print(f'symmetric: {model(i)}','\n')
