#!usr/bin/env python3

from dataclasses import dataclass
from typing import List, Any


def model(data: List[int]) -> List[int]:
  position = 0
  swap_count = 0

  while position + 1 < len(data):
    if data[position] > data[position + 1]:
      swap_value = data[position]
      data[position] = data[position + 1]
      data[position + 1] = swap_value
      position = 0
      swap_count += 1
    else:
      position += 1

  return swap_count


if __name__ == '__main__':
  inputs = [
    {'data': [2,4,1]},
    {'data': [1,1,1,2,2]},
    {'data': [2,1,3,1,2]}
  ]
  for i in inputs:
    m = model(i['data'])
    print(m)