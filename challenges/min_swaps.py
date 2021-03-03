#!usr/bin/env python3

from typing import List


def model(q: List[int]):
  count = 0

  for i in range(len(q)):
    # check if num at index is equal to index + 1
    if q[i] != i + 1:
      # 
      swap_i = q.index(i + 1)
      # set values to swap
      swap_value = q[swap_i]
      current_value = q[i]
      # swap values
      q[swap_i] = current_value
      q[i] = swap_value
      count += 1

  return count


if __name__ == '__main__':
  inputs = [
    [4,3,1,2]
  ]
  for item in inputs:
    m = model(item)
    print(m)