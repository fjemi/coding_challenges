#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('utils/')
from array_to_linked_list import array_to_linked_list


def return_kth_to_last(
  linked_list: array_to_linked_list,
  k: int
) -> array_to_linked_list:
  '''2.2 Return Kth to Last
  Implement an algorithm to find the kth to last element of a singly linked list.
  '''

  if linked_list is None:
    return None

  store = []
  current_node = linked_list

  while current_node.next:
    # add elements to store
    store.append(current_node.val)
    current_node = current_node.next

  if len(store) == 1:
    return store[0]
  # return kth to last element
  if k == 0:
    return store[len(store) - 1]
  return store[len(store) - k + 1]

if __name__ == '__main__':
  l1 = array_to_linked_list([2, 3, 3, 2, 2, 5, 1, 3, 3, 3])
  k = 5
  RKtL = return_kth_to_last(l1, k)
  print(RKtL)
