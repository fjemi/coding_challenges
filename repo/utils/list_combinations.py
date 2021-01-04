from typing import List

def list_combinations(
    a: List[int], b: List[int]
) -> List[str]:
    '''Returns 2 digit combinations of elements from two lists
    :type a: List[int]
    :type b: List[int]
    :rtype: List[str]
    '''
    store = []
    
    if not a or not b:
        store = a + b
        for i in range(len(store)):
          store[i] = str(store[i])
    
    for i in range(len(a)):
        for j in range(len(b)):
            store.append(f'{a[i]}{b[j]}')
    
    return store
    
if __name__ == '__main__':
  lc = list_combinations([1,2,3], [5,4,6])
  print(lc)
