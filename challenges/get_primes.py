#!usr/bin/env python3


from typing import List


def model(a: List[int], n: int) -> List[int]:
  '''list primes between 0 and an interger `n`'''
  for i in range(n):
    prime = True
    
    if n < 3:
      return a
    
    if i not in [0,1,2]:   
      for num in a:
        print(i, num)
        if num != 0:
          if i % num == 0:
            prime = False
            break
      if prime:
        a.append(i)
        
  return a
  
  
if __name__ == '__main__':
  inputs = [{'a': [2], 'n': 50}]
  for i in inputs:
    m = model(i['a'], i['n'])
    print(m)
