#!/usr/bin/env python3

from copy import deepcopy
from typing import List

def total_cells(board: List[List[int]]) -> List[List[int]]:
    ''' determine the next state for cells in a board 
    sum of the cell's surrounding cells
    :type board: Lit[List[int]]
    :rtype: int
    '''

    # make a copy of the board
    copy_board = deepcopy(board)

    for i in range(len(copy_board)):
        for j in range(len(copy_board[i])):

            i_step = -1
            j_step = -1
            counter = 0
            # store the sum of adjacent cells
            adj_cells_sum = 0

            # use steps to visit cells adjacent to cell(i,j)
            while True:
                # reset steps and increment counter after j step has increase by 2
                if j_step > 1:
                    j_step = -1
                    i_step += 1
                    counter += 1

                # condition to break loop
                if counter == 3:
                    break

                # set the indices for an adjacent cell
                adj_i = i + i_step
                adj_j = j + j_step
                # add adjacent cells state to the store if it within range 
                if (adj_i >= 0 and adj_i < len(copy_board) and
                    adj_j >= 0 and adj_j < len(copy_board[i])):
                    #print(copy_board[adj_i][adj_j])
                    adj_cells_sum += copy_board[adj_i][adj_j]
                
                # incremnt j step to visit next cell
                j_step += 1
                
            # set the new state for the current cell
            #print(copy_board[i][j], adj_cells_sum)
            if copy_board[i][j] == 0:
                if adj_cells_sum - copy_board[i][j] == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            elif copy_board[i][j] == 1:
                if (adj_cells_sum - copy_board[i][j]) in [2, 3]:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
           
    return board

if __name__ == '__main__':
  board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

  for i in board:
      print(i)

  print()
  TL = total_cells(board)
  for j in TL:
      print(j)