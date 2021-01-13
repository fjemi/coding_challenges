#!/usr/bin/env python3

from os.path import abspath, dirname
import sys

def get_modules_dir(dir_name: str) -> None:
  ''' Add a module directory to sys.path to enable imports
  :params dir_name: directory containing module to test
    - ex) 'problems/leetcode'
  :type dir_name: str
  :rtype: None
  '''
  
  # set directories
  this_dir = abspath(__file__)
  root_dir = this_dir[:this_dir.find('problems')]
  module_dir = root_dir + dir_name
  # enable imports from utils directory
  sys.path.insert(0, module_dir)
  return None