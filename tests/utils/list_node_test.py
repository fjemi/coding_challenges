#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
UTILS_DIR = abspath('../..') + '/utils'
sys.path.insert(0, UTILS_DIR)

from list_node import list_node

def test_utils_list_node():
  '''
  '''
  
  ln = list_node()
  assert ln.val == float('-inf')
  assert ln.next == None
  
  ln = list_node(1)
  ln.next = list_node(2)
  assert ln.val == 1
  assert ln.next.val == 2
