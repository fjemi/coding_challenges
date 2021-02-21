#!usr/bin/env python3

from dataclasses import dataclass
from typing import List, Any


def model(data: List[List[Any]]) -> List[List[Any]]:
  store = {}
  output = []

  for item in data:
    if item[1] not in store.keys():
      store[item[1]] = [item[0]]
    else:
      store[item[1]].append(item[0])

  names = list(store.values())
  scores = list(store.keys())

  for i in range(len(names)):
    sorted_names = sorted(names[i])
    for j in range(len(sorted_names)):
      output.append([sorted_names[j], scores[i]])

  return output


if __name__ == '__main__':
  inputs = [
    {'data': [['Smith',20],['Jones',15],['Jones',20]]},
    {'data': [['amy', 100],['david',100],['heraldo',50],['aakansha',75],['aleksa',150]]}
  ]
  for i in inputs:
    m = model(i['data'])
    print(m)