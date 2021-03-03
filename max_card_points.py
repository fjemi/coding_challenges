#!usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Data:
  card_points: list[int] = None
  k: int = None
  max_points: int = 0
  error: str = None
  
  
def max_score(data: Data) -> int:
  ''''''
  if not data.card_points or not data.k:
    data.error = 'number of cards or k is not defined'
    return data
  
  num_of_cards = len(data.card_points)
  
  if num_of_cards < data.k:
    data.error = 'number of cards is less than k'
    return data
  
  elif num_of_cards == data.k:
    data.max_points = sum(data.card_points)
    return data
  
  else:
    left = data.card_points[:][0:data.k]
    right = data.card_points[:][num_of_cards - data.k:]

    store = []
    for i in range(data.k):
      if right[-1] >= left[0]:
        store.append(right[-1])
        right = right[:-1]
      else:
        store.append(left[0])
        left.pop(0)
      
    data.max_points = sum(store)
    return data
  
  return data
  
  
if __name__ == '__main__':
  data = [
    Data([1,2,3,4,5,6,1], 3),
    Data([9,7,7,9,7,7,9], 7),
    Data([100,40,17,9,73,75], 3),
    Data([2,2,2], 2),
    Data([1,79,80,1,1,1,200,1], 3),
    Data([1,1000,1], 1)
  ]
  for item in data:
    print(max_score(item))
    
