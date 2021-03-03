#!usr/bin/env python3

from typing import List, Dict

def add_to_store(visited: List[List], store: Dict[List, List], 
  cell: List[int], adjacent_cell: List[int]) -> Dict[List, List]:
  '''add cell and adjacent cell to store'''
  
  cell_string = f'{cell[0]}/{cell[1]}'
  adjacent_string = f'{adjacent_cell[0]}/{adjacent_cell[1]}'
  store_keys = list(store.keys())
  
  # ignore cells already visited
  if adjacent_string in visited:
    return store
   
  # check wether to add cell/adjacent to store
  #'i/j' == cell(i,j)
  if cell_string not in list(store.keys()):
    store[cell_string] = [adjacent_string]
  else:
    store[cell_string].append(adjacent_string)
  
  visited.append(adjacent_string)
  return store
  

def max_area_island(grid: List[List[int]]) -> int:
  col_length = len(grid)
  row_length = len(grid[0])
  store = {}
  visited = []
  
  for i in range(col_length):
    for j in range(row_length):
      #print(i, j, grid[i][j])
      if grid[i][j] != 0:       
         # for stepping through adjacent cells
        steps = [-1,1]
        for step in steps:
          i_step = i + step
          # Only consider cells within the grid range with a value of 1
          if i_step > -1 and i_step < col_length and grid[i_step][j] == 1:
            # check to add cell/adjacent to store
            add_to_store(visited, store, [i,j], [i_step,j])
        for step in steps:
          j_step = j + step    
          if j_step > -1 and j_step < row_length and grid[i][j_step] == 1:
            add_to_store(visited, store, [i,j], [i,j_step])

        visited.append(f'{i}/{j}')  
   
  return store


if __name__ == '__main__':
  grid = [[0,0,0,0,1,1,1,0],
          [0,0,0,0,1,1,1,0]]
  grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0,0,0,0,0,0,0],
          [0,1,0,0,1,1,0,0,1,0,1,0,0],
          [0,1,0,0,1,1,0,0,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,1,1,0,0,0,0]]
  result = max_area_island(grid)
  print(f'direct connected cells: {result}')
  
  connected = {}
  temp = {}
  
  for key in result.keys():
    connected[key] = len(result[key])
    temp[key] = result[key][:]
    #print(key, result[key])
    
    for item in result[key]:
      try:
        temp[key].extend(result[item])
        # add adjacent cells connections to cell
        result[key].extend(result[item])
        # determine the number of connected cells
        connected[key] = len(result[key]) + 1
      except:
        pass

  print(f'indirect connected cells: {temp}')
  print(f'connected counts: {connected}')
  
