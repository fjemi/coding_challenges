#!/usr/bin/env python3

from os.path import abspath
import sys

# enable imports from utils directory
PROBLEMS_DIR = abspath('../../..') + '/problems/leetcode/'
sys.path.insert(0, PROBLEMS_DIR)

def get_problems_dir() -> str:
  '''
  '''
  return PROBLEMS_DIR