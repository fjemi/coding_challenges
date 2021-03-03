#!usr/bin/env python3

from typing import List


def rotate_left(a: List[int], d: int) -> List[int]:
  for i in range(d):
    last_element = a[0]
    a.pop(0)
    a.append(last_element)
    # one line solution that failed time requirement
    #a = a[1:] + [a[0]]
  return a


if __name__ == '__main__':
  rl = rotate_left([1,2,3,4,5], 4)
  print(rl)