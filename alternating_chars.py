#!usr/bin/env python3


def model(s: str) -> str:
  s = [char for char in s]
  store = [s[0]]

  i = 1
  while i < len(s):
    if store[-1] != s[i]:
      store.append(s[i])
    i += 1

  count = len(s) - len(store)
  return count


if __name__ == '__main__':
  inputs = [
    'AABAAB',
    'AAABBB'
  ]
  for i in inputs:
    m = model(i)
    print(m)