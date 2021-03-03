#!usr/bin/env python3

def backspace_compare(S: str, T: str) -> bool:
  new_S = ''
  new_T = ''
  
  for char in S:
    if char == '#':
      new_S = new_S[:-1]
    else:
      new_S = f'{new_S}{char}'
      
  for char in T:
    if char == '#':
      new_T = new_T[:-1]
    else:
      new_T = f'{new_T}{char}'
      
  if new_S == new_T:
    return True
  else:
    return False
  
 
if __name__ == '__main__':
  data = [
    {'S': "ab#c", 'T': "ad#c"}
  ]
  
  for d in data:
    bc = backspace_compare(d['S'], d['T'])
    print(bc)
