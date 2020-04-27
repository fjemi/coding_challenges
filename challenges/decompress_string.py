'''Challenge: Decompress a compressed string
https://techdevguide.withgoogle.com/resources/compress-decompression/#!
'''

# Date modeling
from dataclasses import dataclass, field, asdict
import json
# Type hints
from typing import List, Dict

@dataclass
class Decompress:
  '''Class to decompress compressed strings
  '''
  compressed_str: str
  split_string: List = field(default=None)
  replace_string: List = field(default_factory=lambda: [])
  decompressed_str: str = field(default='')
  
  def __post_init__(self):
    '''Get the types of characters in the string
    '''
    # Split the string on closing brackets
    self.split_string = self.compressed_str.split(']')
    # Replace opening brackets with '*'
    for item in self.split_string:
      # Check for empty strings
      if item != '':
        self.replace_string.append(
          item.replace('[', '*')
        )
    # Evaluate each expression in replace_string
    
    for item in self.replace_string:
      # Find the left most multiply operator. 
      # If non exists add the expression to the decompressed
      alpha_string = ''
      operator_index = 1 # 1 if not `*` exists
      multiplier = 1 # 1 if no multiplier string exists
      for i, char in enumerate(reversed(item)):
        if char == '*':
          operator_index = len(item) - i - 1
          multiplier = eval(item[0:operator_index])
          break
        # The string that gets multiplied
        alpha_string =  f'{char}{alpha_string}'
      # Create the decompressed string
      self.decompressed_str = f'{self.decompressed_str}{alpha_string * multiplier}'

if __name__ == '__main__':
  compressed_str = ['3[abc]4[ab]c']#, '2[3[a]b]', '1[a]2[3[b]]']
  for string in compressed_str:
    D = Decompress(string)
    print(json.dumps(asdict(D), indent=2))
