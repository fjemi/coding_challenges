'''Simple script to generate passwords in Python'''

import ast
import sys

import string
# Generate random integer
from random import randint
# Data modeling
from dataclasses import dataclass, field
# Type hints
from typing import List

CHAR_TYPES = {
    'lowercase': string.ascii_lowercase,
    'uppercase': string.ascii_uppercase,
    'number': string.digits,
    'special': string.punctuation
}

@dataclass
class PasswordGenerator:
  # The length of the password
  length: int
  # Types of characters to include: lowercase, uppercase, etc.
  chars: List
  # Pool of characters to chose from
  pool: str = ''
  password: str = ''
  
  def __post_init__(self):
    '''Set the pool of characters'''
    for chars in self.chars:
      # Check if valid char type
      if chars in CHAR_TYPES.keys():
        self.pool = self.pool + CHAR_TYPES[chars]
    
    pool_size = len(self.pool) - 1
    # Check if pool is populated
    if pool_size > 0:    
      for i in range(self.length):
        random_number = randint(0, pool_size)
        self.password = self.password + self.pool[random_number]
    
   
if __name__ == '__main__':
  # Example input/output
  chars = ['lowercase', 'uppercase']
  length = 8
  pg = PasswordGenerator(8, chars)
  print(pg)
  
  # Example input/output passed as arguements from CL
  # CMD: python password_generator.py 8 "['number', 'lowercase']"
  length = int(sys.argv[1])
  chars = ast.literal_eval(sys.argv[2])
  print(length, chars)
  pg = PasswordGenerator(length, chars)
  print(pg)
        
        

