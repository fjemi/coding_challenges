#!usr/bin/env python3

from typing import List

def substring_check(s1: str, s2: str) -> str:
  for i in range(len(s2)):
    if s1.find(s2[i]) > -1:
      return 'Yes'
  return 'No'


def model(s1: str, s2: str) -> str:
  
  l1 = len(s1)
  l2 = len(s2)

  if l1 >= l2:
    result = substring_check(s1, s2)
  else:
    result = substring_check(s2, s1)

  return result


if __name__ == '__main__':
  inputs = [{
    's1': 'hello', 
    's2': 'world'
  }, {
    's1': 'and',
    's2': 'art'
  }, {
    's1': 'hi',
    's2': 'world'
  }]
  for item in inputs:
    m = model(item['s1'], item['s2'])
    print(m)