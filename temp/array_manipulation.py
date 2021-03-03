#!usr/bin/env python3

from typing import List


def model(n: int, queries: List[List[int]]):
  total = 0
  a = min(queries[0][0], queries[0][1])
  b = max(queries[0][0], queries[0][1])
  interval = [x for x in range(a, b + 1)]
  print(interval)

  for row in queries[1:]:
    
    if (row[0] in interval and row[1] in interval):
      total += row[2]
      print(row, a, b)

  return total


if __name__ == '__main__':
  inputs = [
    [[5,3],
    [1,2,100],
    [2,5,100],
    [3,4,100]]
  ]
  for item in inputs:
    m = model(1, item)
    print(m)