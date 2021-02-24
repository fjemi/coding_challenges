#!usr/bin/env python3

from typing import List

VALID_DENOMINATIONS = [10,20,50,100,200,500,1000]

def model(data: List[str]) -> int:
  '''Count Counterfeit'''
  total = 0

  for d in data:
    counterfeit = False

    if len(d) <10 or len(d) > 12:
      counterfeit = True

    if not counterfeit:
      d = [char for char in d]

    # check uniquness and uppercase of first 3 chars
    if not counterfeit:
      store = {}
      for char in d[:3]:
        if char in store.keys() or char.isdigit() or char != char.upper():
          counterfeit = True
          break
        store[char] = 1

    # check note year between 1900 and 2019
    if not counterfeit:
      try:
        year = int(''.join(d[3:7]))
        if year > 2019 or year < 1900:
          counterfeit = True
      except:
        counterfeit = True

      # check last char is uppercase alpha
      if not counterfeit:
        if d[-1].isdigit() or d[-1] != d[-1].upper():
          counterfeit = True

    # set note denomination
    if not counterfeit:
      try:
        denomination = int(''.join(d[7:-1]))
        if denomination in VALID_DENOMINATIONS:
          total += denomination
      except:
        pass

  return total


if __name__ == '__main__':
  inputs = [
    'AVG190420T',
    'RTF20001000Z',
    'QWER201850G',
    'AFA199620E',
    'ERT1947200T',
    'RTY20202004',
    'DRV1984500Y',
    'ETB2010400G'
  ]
  m = model(inputs)
  print(m, inputs)