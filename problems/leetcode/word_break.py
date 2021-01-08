#!/usr/bin/env python3

from typing import List

def break_helper(s: str, word: str) -> str:
  ''' helper function for breaking up a string
  :params s: string to break up
  :params word: word to remove from s
  :type s: str
  :type word: str
  :rtype: str
  '''
  while True:
    index = s.find(word)

    # exit loop if word not found in string
    if index == -1:
      return s

    if index == 0:
      # logice if word is at the begining of the string
      s = s[index + len(word):]
      #print(s, word)
    else:
      # logic if word anywhere else in string
      s = s[:index] + s[index + len(word):]
      #print(s, word)
  return s

  


def word_break(s: str, word_dict: List[str]) -> bool:
  '''
  '''

  # word_dict in reverse
  r_word_dict = word_dict[::-1]
  # copies to move fowards and backwards
  print(s, word_dict)
  s_forward = s[:]
  s_backward = s[:]

  for i in range(len(word_dict)):
    s_forward = break_helper(s_forward, word_dict[i])
    s_backward = break_helper(s_backward, r_word_dict[i])

  if s_forward == '' or s_backward == '':
    return True

  return False

if __name__ == '__main__':
  WB = word_break("leetcode", ["leet", "code"])
  print(WB)

  WB = word_break('cars', ['car', 'ca', 'rs'])
  print(WB)

  WB = word_break('ccbb', ['bc', 'cb'])
  print(WB)

  WB = word_break("applepenapple", ["apple","pen"])
  print(WB)
