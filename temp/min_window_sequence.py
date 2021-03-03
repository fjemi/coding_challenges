#!usr/bin/env python3


def minWindow(S: str, T: str) -> str:
  ''''''
  store = []
  T_size = len(T)
  min_subsequence_size = len(T)
  
  while min_subsequence_size <= len(S):
    for i in range(len(S)):
      count = 0
      # set the window size
      window = S[i:i + min_subsequence_size]
      # loop characters in the window to determine if it contains subsequence
      for char in window:
        if char == T[count]:
          count += 1
        # add to store and exit if once T is found in subsequence
        if count == T_size - 1:
          store.append(window)
          break
      # exit main loop if store contains subsequences
      if len(store) > 0:
        return store[0]
    
    # increment the window size
    min_subsequence_size += 1
  
  return ''


if __name__ == '__main__':
  S = "abcdebdde"
  T = "bdey"
  mw = minWindow(S, T)
  print(mw)
