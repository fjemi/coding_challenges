'''Word Squares
https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/#!
'''

# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hinting
from typing import List, Dict, Any
# Permutations
from itertools import permutations

# Word square
from word_square_check import WordSquareCheck

@dataclass
class GenerateWordSquares:
  words: List[str]
  squares: List[str] = field(default_factory=lambda: [])
  square_length: int = None
  
  def __post_init__(self):
    '''Generate all possible word squares given a list of words
    '''
      
    # Set square sizes (number of words to include)
    self.square_length = len(self.words[0])
    
    # Generate permutations of the 
    perm = list(permutations(self.words, self.square_length))
    for i in range(len(perm)):
      
      wsc = WordSquareCheck(perm[i])
      if wsc.is_word_square == 'yes':
        print(perm[i])
        self.squares.append(perm[i])

if __name__ == '__main__':
  input = [
    ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD'],
    ['BALL', 'AREA', 'LEAD', 'LADY']
  ]
  
  for words in input:
    GWS = GenerateWordSquares(words)
    print(json.dumps(asdict(GWS), indent=2))
