#!/usr/bin/env python3

from list_node import list_node
from typing import List 

def array_to_linked_list(a: List) -> list_node:
    '''create a linked list of list nodes from an array
    :params a: array to create linked list from
    :type a: List
    :rtype: list_node
    '''
    # empty array
    if not a:
        return list_node()
    
    # intialize the linked list
    linked_list = current = list_node(float('-inf'))    
    
    for i in range(len(a)):
        # create a new list node
        new_node = list_node(a[i])
        # set new node as the current node's next 
        current.next = new_node
        # reset the current node
        current = current.next
        
    return linked_list.next
  
if __name__ == '__main__':
  a = [[], [1,2,3,4]]
  
  for item in a:
    print(item)
    print(array_to_linked_list(item))
