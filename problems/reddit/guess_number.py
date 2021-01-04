
'''Guess Number
https://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/
'''


import string
from random import randint
# Data modeling
from dataclasses import dataclass, field, asdict
from json import dumps as json_dumps
# Type hints
from typing import List
from numbers import Integral


@dataclass
class Model:
  '''Class for guess a random number
  '''
  guesses: List = field(default_factory=lambda: [])
  number: int = randint(0, 100)
  guess_range: List[int] = field(default_factory=lambda: [0, 100])
  
  
  def __post_init__(self):
    '''Execute after class initializes
    '''
    while True:
      #print(self)
      # Get user input
      input_message = f'Guess a number between {self.guess_range[0]} and {self.guess_range[1]}: '
      user_input = input(input_message)
      
      # Check if input is a number
      number_check = True
      try:
        user_input = int(user_input)
        self.guesses.append(user_input)
      except:
        number_check = False
        print(f'"{user_input}" is not a number. Please try again.')
      
      # Check if the guess is correct
      if number_check:
        if user_input > self.number:
          self.guess_range[1] = user_input
          print(f'The number is less than "{user_input}"')
        elif user_input < self.number:
          self.guess_range[0] = user_input
          print(f'The number is greater than "{user_input}"')
        elif user_input == self.number:
          print(f'Good guess! "{self.number}" is the correct number.')  
          break
    
    
if __name__ == '__main__':
  M = Model()
  print(json_dumps(asdict(M), indent=2))
