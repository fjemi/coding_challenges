#!/usr/bin/env python

from list_node import ListNode
from typing import List 

def array_to_linked_list(a: List) -> ListNode:
    '''create a linked list of list nodes from an array
    :params a: array to create linked list from
    :type a: List
    :rtype: ListNode
    '''
    # empty array
    if not a:
        return ListNode()
    
    # intialize the linked list
    linked_list = current = ListNode(float('-inf'))    
    
    for i in range(len(a)):
        # create a new list node
        new_node = ListNode(a[i])
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
