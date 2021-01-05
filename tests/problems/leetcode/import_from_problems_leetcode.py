#!/usr/bin/env python3

import pytest
from os.path import abspath
import sys

# enable imports from utils directory
PROBLEMS_DIR = abspath('../../..') + '/problems/leetcode/'
sys.path.insert(0, PROBLEMS_DIR)