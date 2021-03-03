#!usr/bin/env python3

from typing import List


def model(arr: List[int], r: int) -> int:
  count = 0

  for i in range(len(arr)):
    current = i
    temp = [arr[current]]
    dupes = 0

    while current < len(arr) - 1:
      if len(temp) == 3:
          if dupes == 0:
            count += 1
          else:
            count = count + dupes + 1
          break

      if arr[current] * r == arr[current + 1]:
        temp.append(str(arr[current + 1]))
        current += 1
      elif arr[current] == arr[current + 1]:
        current += 1
        dupes += 1
        
  return count


'''
def model(arr: List[int], r: int) -> int:
  store = {}
  count = 0
  dupes = 0
  dupe_dict = {}

  for i in range(len(arr) - 1):
    current = i
    temp = str(i)
    
    while current + 1 < len(arr):
      if arr[current] == arr[current + 1]:
        if current in dupe_dict.keys():
          dupe_dict[f'{i}{arr[current]}'] += 1
        else:
          dupe_dict[f'{i}{arr[current]}'] = 1
        current = current + 1
        dupes += 1
        
      elif arr[current] * r == arr[current + 1]:
        temp = temp + f'{current + 1}'
        current = current + 1
        #print(temp)
        if len(temp) == 3:
          count += 1
          break
      else:
        dupe_dict[f'{i}{arr[current]}'] = 0
        break
  return (count, dupes, dupe_dict)
  if dupes > 0 and count % 2 != 0:
    return int(count + dupes / 2)
  return count + dupes
'''


if __name__ == '__main__':
  inputs = [
    {'arr': [1,4,16,64], 'r': 4},
    {'arr': [1,2,2,2,4], 'r': 2},
    {'arr': [1,5,5,25,125], 'r': 5},
    {'arr': [1,5,5,5,5,25,25,125], 'r': 5},
    {'arr': [1,3,9,9,27,81], 'r': 3}
  ]
  for item in inputs:
    m = model(item['arr'], item['r'])
    print(m,item['arr'])