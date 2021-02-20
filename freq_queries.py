#!usr/bin/env python3

from typing import List, Tuple


def model(queries: List[Tuple]):
  store = []
  freq = {}

  for q in queries:
    if q[0] == 1:
      store.append(q[1])
      if q[1] not in freq.keys():
        freq[q[1]] = 1
      else:
        freq[q[1]] += 1
    elif q[0] == 2:
      try:
        store.remove(q[1])
        freq[q[1]] -= 1
      except:
        pass
    elif q[0] == 3:
      if q[1] in freq.values():
        print(1)
      else:
        print(0)
    
  return None


if __name__ == '__main__':
  queries = [
    (1,1), (2,2), (3,2), (1,1), (1,1), (2,1),(3,2)
  ]
  model(queries)