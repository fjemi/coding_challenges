#!usr/bin/env python3

from typing import List


def model(magazine: str, note: str):
  count = 0
  magazine = sorted(magazine.split())
  note = sorted(note.split())

  for i in range(len(note)):
    if note[i] in magazine:
      magazine.remove(note[i])
    else:
      return 'No'

  return 'Yes'


if __name__ == '__main__':
  inputs = [{
    'magazine': 'ive got a lovely bunch of coconuts', 
    'note': 'ive got some coconuts'
  }, {
    'magazine': 'give me one grand today night',
    'note': 'give one grand today'
  }]
  for item in inputs:
    m = model(item['magazine'], item['note'])
    print(m)