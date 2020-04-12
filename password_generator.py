'''Simple script to generate passwords in Python'''

# CL arguements
import ast
import sys
# Character types
import string
# Generate random integer
from random import randint
# Data modeling
from dataclasses import dataclass
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
  '''
    Dataclass for generating a random password
  '''
  # The length of the password
  length: int
  # Types of characters to include: lowercase, uppercase, etc.
  chars: List
  # Pool of characters to chose from
  pool: str = ''
  password: str = ''
  
  def __post_init__(self):
    '''
      Set the pool of characters
    '''
    for type_ in self.chars:
      # Check if valid char type
      if type_ in CHAR_TYPES.keys():
        self.pool = self.pool + CHAR_TYPES[type_]
    
    pool_size = len(self.pool) - 1
    # Check if pool is populated
    if pool_size > 0:    
      for i in range(self.length):
        random_number = randint(0, pool_size)
        self.password = self.password + self.pool[random_number]
    
  def get_password(self):
    return {'password': self.password}
   
if __name__ == '__main__':
  # Example input/output passed as arguements from CL
  # CMD: python password_generator.py 8 "['number', 'lowercase']"
  try:
    length = int(sys.argv[1])
    chars = ast.literal_eval(sys.argv[2])
  except:
    length = 8
    chars = ['number', 'lowercase', 'uppercase', 'special']
  pg = PasswordGenerator(length, chars)
  print(pg.get_password())
        
        

