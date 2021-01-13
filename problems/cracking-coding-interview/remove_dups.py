#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('utils/')
from array_to_linked_list import array_to_linked_list


def remove_dups(linked_list: array_to_linked_list):
  '''2.1 Remove Dups! 
  Write code to remove duplicates from an unsorted linked list.
  '''
  # store unique values
  store = []
  current_node = linked_list

  while current_node.next:
    if current_node.val not in store:
      # add node value to store
      store.append(current_node.val)
      current_node = current_node.next
    else:
      # move to next node if value already in store
      current_node = current_node.next

  # return store as a linked list
  return array_to_linked_list(store)

if __name__ == '__main__':
  l1 = array_to_linked_list([2, 3, 3, 2, 2, 3, 1, 3, 3, 3])
  RD = remove_dups(l1)
  print(RD)