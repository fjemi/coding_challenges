#!/usr/bin/env python

def merge_two_arrays(a: list, b: list) -> list:
    '''merge two arrays
    '''
    store = []
    item_count = len(a) + len(b)
    
    for i in range(item_count):
        # if a or b is empty return the the other
        if not a or not b:
            return store + a + b
        # add to store and remove from lists
        if b[0] <= a[0]:
            store.append(b[0])
            b.pop(0)
        else:
            store.append(a[0])
            a.pop(0)
    return store
  
if __name__ == '__main__':
  a = [1,2,4]
  b = [1,3,4]
  print(a, b)
  mta = merge_two_arrays(a, b)
  print(mta)
