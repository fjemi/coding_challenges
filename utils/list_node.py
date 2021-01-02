#!/usr/bin/env python

from typing import List
from dataclasses import dataclass

@dataclass
class ListNode():
    '''Class for a node in a linked list
    :type val: int
    :type next: ListNode
    '''
    val: int = float('-inf')
    next: int = None


if __name__ == '__main__':
  ln = ListNode(100)
  print(ln)
