#!usr/bin/env python3

from typing import List
from time import time

def model1(data: List[int]) -> int:
  count = 0
  j_size = len(data)

  for i in range(len(data)):
    position = None
    if data[i] % 2 != 0:
      for j in range(i + 1, j_size):
        if data[j] % 2 == 0:
          position = j
      if position is not None:
        data[i], data[position] = data[position], data[i]
        #swap = data[i]
        #data[i] = data[position]
        #data[position] = swap
        count += 1
        j_size -= 1
  
  return count


def model2(data: List[int]) -> int:
  left = 0
  right = len(data) - 1
  count = 0

  while left < right:
    while (data[left] % 2 == 0 and left < right):
        left += 1

    while (data[right] % 2 == 1 and left < right):
        right -= 1

    if left < right:
      data[left], data[right] = data[right], data[left]
      left += 1
      right = right - 1
      count += 1

  return count


if __name__ == '__main__':
  print(time() - time())
  inputs = [
    [6,3,4,5],
    [13,10,21,20],
    [8,5,11,4,6]
  ] + [
    [
      329963077,403414481,437623101,485366585,599466263,959094281,
      82921272,110219722,162495938,470311130,583170602
    ] +
    [
      329963077,403414481,437623101,485366585,599466263,959094281,
      82921272,110219722,162495938,470311130,583170602
    ]

  ]
  
  for i in inputs:
    start = time()
    m1 = model1(i)
    end1 = time() - start
    start = time()
    m2 = model2(i)
    end2 = time() - start
    print(m1, m2, i, end1, end2)

  print((end2 - end1) / end1 * 100)