#!usr/bin/env python3

from typing import List
from json import dumps

def most_similar_graph_path(
  n: int, roads: List[List[int]], 
  names: List[str], target_path: List[str]
) -> List[int]:
  ''''''
  store = [names.index(target_path[0])]
  #store = []
  paths = {}
  
  ## expand the paths (forward and backward)
  #for road in roads:
    #paths[f'{names[road[0]]}-{names[road[1]]}'] = road
    #paths[f'{names[road[1]]}-{names[road[0]]}'] = list(reversed(road))
  
  #for i in range(len(roads)):
    #paths[f'{names[roads[i][0]]}-{names[roads[i][1]]}'] = roads[i]
    #paths[f'{names[roads[i][1]]}-{names[roads[i][0]]}'] = roads[i]
  #print(dumps(paths, indent=2))
  
  #for i in range(len(target_path) - 1):
    #path1 = f'{target_path[i]}-{target_path[i + 1]}'
    #path2 = f'{target_path[i]}-{target_path[i + 1]}'
    #if path1 in list(paths.keys()):
      #store.append(paths[path1])
    #elif path2 in list(paths.keys()):
      #store.append(paths[path2])
    #else:
      ## return to starting pointing
      #store.append(list(reversed(store[-1])))
      #target_path[i + 1] = target_path[i]
    #print(store)
    
  
  for road in roads:
    # forwards
    if road[0] in paths.keys():
      paths[road[0]].append(road[1])
    else:
      paths[road[0]] = [road[1]]
    # backwards
    if road[1] in paths.keys():
      paths[road[1]].append(road[0])
    else:
      paths[road[1]] = [road[0]]
  print(paths)
  
  target_path_nums = []
  for target in target_path:
    target_path_nums.append(names.index(target))
  print(target_path_nums)
 
      
  for i in range(1, len(target_path_nums)):
    if target_path_nums[i] in paths[store[0]]:
      store.append(target_path_nums[i])
    else:
      pass
      

  
  #print(paths)
  print(store)

if __name__ == '__main__':
  n = 5
  roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]
  names = ["ATL","PEK","LAX","DXB","HND"]
  target_path = ["ATL","DXB","HND","LAX"]
  result = [0,2,4,2]
  ms = most_similar_graph_path(n, roads, names, target_path)
  #assert result == ms
