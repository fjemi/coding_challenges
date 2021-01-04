#!/usr/bin/env python3

def arrange_coins(n: int) -> int:
  ''' 441. Arrange Coins
  https://leetcode.com/problems/arranging-coins/
  '''
  # Remaing coins after each row
  remaining_coins = n
  # Determine coins in a row
  for i in range(n + 1):
    row_coins = i
    remaining_coins = remaining_coins - i
    if remaining_coins <= row_coins:
      break
  return row_coins


if __name__ == '__main__':
  n = [0, 1, 5, 8]
  for i in n:
    AC = arrange_coins(i)
    print({'rowCoins': AC})
