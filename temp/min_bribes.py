#!usr/bin/env python3

from typing import List


def model(q: List[int]):
  count = 0
  for i in range(len(q)):
    bribe = abs(i + 1 - q[i])
    if bribe > 2:
      return 'Too chaotic'
    count += bribe / 2
  return count


if __name__ == '__main__':
  inputs = [
    [4,1,2,3],
    [2,1,5,3,4],
    [2,5,1,3,4],
    [5,1,2,3,7,8,6,4],
    [1,2,5,3,7,8,6,4]
  ]
  for item in inputs:
    m = model(item)
    print(m)