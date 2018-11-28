'''
Minesweeper

https://techdevguide.withgoogle.com/resources/coding-question-minesweeper/#!
'''

import numpy as np
import random

# Decorator/function to count the number of times a function is called
def call_count(function):
  function()
  c_count += 1
  print(c_count)
  return c_count

# Class to create an n(m) matrix
class MineField(object):

  def __init__(self, row, column, mine):
    self.row = row
    self.column = column
    self.mine = mine

  # Initialize and n x m zero matrix
  def field(self):
    #field = []
    field = np.full((self.row, self.column), '-')
    return field

  def mine_field(self):
    max_mine = self.mine
    array_size = self.field().size - 1
    m_field = self.field()

    # Reset the max number of mines if the intial value was to high
    if self.mine >= max_mine:
      self.mine = random.randint(1, array_size)
    
    # Fill the field with mines
    for count in range(0, max_mine):
      empty = False

      while not empty:
        m_row = random.randint(0, self.row) - 1
        m_column = random.randint(0, self.column) - 1

        if m_field[m_row][m_column] == '-':
          m_field[m_row][m_column] = 'X'
          empty = True
  
    return m_field
    
  def click_field(self, c_row, c_column):
    field = self.field()
    c_field = self.mine_field()
    
    if c_field[c_row][c_column] != 'X':
      field[c_row][c_column] = ' '
      return ('Please make another selection', field)
    else:
      c_field[c_row][c_column] = 'O'
      return  ('You selected a mine', c_field)

  
  def p_field(self):

    return p_field

  #@call_count
  def click(self, c_row, c_column):
    print(self.field())
    print(self.m_field()[c_row][c_column])
    return 'hi'
    


# Initialize a MineField object
m = 7
n = 7
a = MineField(m, n, random.randint(1, m * n))
# Print the field
print('Blank field: \n', a.field(), '\n')
print('Mine field: \n', a.mine_field())
clicked = a.click_field(1,1) # loop clicks unitl a mine is selected or the matrix doesn't contain any '-'
print(clicked[0])
print(clicked[1])
