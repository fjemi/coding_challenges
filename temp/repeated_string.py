#!usr/bin/env python3


def repeated_string(s: str, n: int) -> int:
  count = 0
  
  limit = 10**12
  if n > limit:
    n = limit
  '''new_s = s * int((n / len(s)) + 1) 

  for i in range(n):
    if new_s[i] == 'a':
      count += 1'''

  #new_s = len(s) * int((n / len(s)) + 1) 
  new_s = int((n / len(s))) 

  print(n, '\n', new_s)
  #return count


if __name__ == '__main__':
  rs = repeated_string('aba', 10)
  print(rs)

  rs = repeated_string('a',1000000000000)
  print(rs)