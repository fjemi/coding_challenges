#!usr/bin/env python3

from typing import List

def string_to_list(s: str) -> List[str]:
  l = []
  [l.append(char) for char in s]
  return l


def model(s: str) -> str:
  store = {}

  for i in range(len(s)):
    # set substring and string to loop through to check 
    # for instances of the substring
    substring = string_to_list(s[:i + 1])
    loop_string = string_to_list(s[i - 1:])

    # create substrings of the loop string to check
    # for the original substring
    for i in range(len(loop_string)):
      check_string = loop_string[i: i + len(substring)]
      
      if (len(substring) == len(check_string) and 
        sorted(substring) == sorted(check_string)):
        store[''.join(substring)] = 1
        print(substring, check_string)

    # forwards and backards
    # check each char

  return len(store.keys())


if __name__ == '__main__':
  inputs = [
    {'s': 'mom'}, 
    {'s': 'abba'}, 
    {'s': 'ifailuhkqq'},
    {'s': 'kkkk'},
    {'s': 'cdcd'}
  ]
  for item in inputs:
    m = model(item['s'])
    print(m)