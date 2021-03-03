#!usr/bin/env python3


from typing import List
from math import floor


def model(expenditure: List[int], d: int):
  notification_count = 0
 
  for i in range(len(expenditure)):
    if i + d < len(expenditure):
      previous_spend = sorted(expenditure[i:i + d])
      current_spend = expenditure[i + d]

      # calculate median
      if d % 2 != 0:
        position = floor(d / 2)
        median = previous_spend[position]
      else:
        num1 = previous_spend[int(d / 2)]
        num2 = previous_spend[int(d / 2) - 1] 
        median = (num1 + num2) / 2

      if current_spend >= median * 2:
        notification_count += 1

  return notification_count


if __name__ == '__main__':
  inputs = [
    {'expenditure': [10,20,30,40,50], 'd': 3},
    {'expenditure': [1,2,3,4,4], 'd': 4},
    {'expenditure': [2,3,4,2,3,6,8,4,5], 'd': 5}
  ]
  for input in inputs:
    m = model(input['expenditure'], input['d'])
    print(m)