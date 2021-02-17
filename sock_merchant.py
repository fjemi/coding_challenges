#!usr/bin/env python3

from dataclasses import dataclass, field
from typing import List


def sock_merchant(ar: List[int]) -> int:
  store = {}
  count = 0

  for num in ar:
    if num not in store.keys():
      store[num] = 1
    else:
      store[num] += 1
      if store[num] == 2:
        count += 1
        store[num] = 0

  return(count)
    

if __name__ == '__main__':
  sm = sock_merchant([1,2,1,2,1,3,2])
  print(sm)