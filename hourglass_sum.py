#!usr/bin/env python3

from typing import List


def hourglass_sum(arr: List[List[int]]) -> int:
  store = []

  m = len(arr)
  n = len(arr[0])

  if m < 3 or n < 3:
    return 0

  i_steps = [-1, 1]
  j_steps = [-1, 0, 1]
  
  # sum hourglass nums
  for i in range(1, m - 1):
    for j in range(1, n - 1):
      current_sum = arr[i][j]
      # step through nums that make hourglass
      for i_step in i_steps:
        k = i + i_step
        for j_step in j_steps:
          l = j + j_step
          current_sum += arr[k][l]
      store.append(current_sum)

  return sum(store)


if __name__ == '__main__':
  arr = [
    [1,1,1,1],
    [0,3,0,1],
    [1,4,1,1],
    [1,1,1,1]
  ]
  hs = hourglass_sum(arr)
  print(hs)

  arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
  ]
  hs = hourglass_sum(arr)
  print(hs)