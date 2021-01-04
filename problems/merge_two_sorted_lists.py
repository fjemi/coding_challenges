#!/usr/bin/env python3

from os.path import abspath
import sys

# enable imports from utils directory
UTILS_DIR = abspath('') + '/utils'
print(UTILS_DIR)
sys.path.insert(0, UTILS_DIR)

from list_node import list_node
from array_to_linked_list import array_to_linked_list


def merge_two_lists(l1: list_node, l2: list_node) -> list_node:
  '''21. Merge Two Sorted Lists
  https://leetcode.com/problems/merge-two-sorted-lists/)
  '''
    #initialize heand and tail of the node
    head = current = list_node()
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = list_node(l1.val)
            current = current.next
            l1 = l1.next
        else:
            current.next = list_node(l2.val)
            current = current.next
            l2 = l2.next
        
    # tenary operation 
    current.next = l1 or l2
    return head.next
  
if __name__ == '__main__':
  a, b = [1, 2, 4], [1, 3, 4]
  print(a, b)
  mtl = merge_two_lists(array_to_linked_list(a), array_to_linked_list(b))
  print(mtl)
