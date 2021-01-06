#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('utils/')

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
