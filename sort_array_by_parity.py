from typing import List


def sort_array_by_parity(array: List[int]) -> List[int]:
  ''''''
  odd = []
  for i in reversed(range(len(array))):
    if array[i] % 2 != 0:
      odd.append(array[i])
      del array[i]     
  return array + odd


if __name__ == '__main__':
  array = [3,1,2,4]
  output = [2,4,3,1]
  print(array, sort_array_by_parity(output))
