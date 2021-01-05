#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
UTILS_DIR = abspath('../..') + '/utils'
sys.path.insert(0, UTILS_DIR)

from array_to_linked_list import array_to_linked_list

def test_array_to_linked_list():
  '''
  '''
  atll = array_to_linked_list([])
  assert atll.val == float('-inf')
  assert atll.next == None
  
  atll = array_to_linked_list([0])
  assert atll.val == 0
  assert atll.next == None
  
  atll = array_to_linked_list([1, 2, 3, 4])
  assert atll.val == 1
  assert atll.next.val == 2
  assert atll.next.next.val == 3
  assert atll.next.next.next.val == 4
  assert atll.next.next.next.next == None
