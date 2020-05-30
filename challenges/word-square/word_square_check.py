'''Word Squares
https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/#!
'''

# Data modeling
from dataclasses import dataclass, field, asdict
import json
# Type hinting
from typing import List, Dict, Any

@dataclass
class Model:
  words: List[str]
  length_check: bool = True
  is_word_square: str = 'yes'
  
  def __post_init__(self):
    '''Check if a list of words froms a word square
    '''
    
    # Nummber of words must equal the lengths of the words
    for word in self.words:
      if len(word) != len(self.words):
        self.length_check = False
        self.is_word_square = 'no'
        break
    
    # Check if letters are the same
    for i in range(len(self.words)):
      for j in range(len(self.words)):
        if i != j: # Ignore the diagonal
          if self.words[i][j:j + 1] != self.words[j][i:i + 1]:
            self.is_word_square = 'no'
            break

if __name__ == '__main__':
  input = [
    ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD'],
    ['BALL', 'AREA', 'LEAD', 'LADY']
  ]
  
  for words in input:
    M = Model(words)
    print(json.dumps(asdict(M), indent=2))
