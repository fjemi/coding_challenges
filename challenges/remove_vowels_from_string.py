#!usr/bin/env python3

def model(s: str) -> str:
  s_copy = list(s)
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  
  for i in range(len(s)):
    if s[i].lower() in vowels:
      s_copy.remove(s[i])
  return ''.join(s_copy)

if __name__ == '__main__':
  inputs = ['test']
  for i in inputs:
    print(model(i))
    
