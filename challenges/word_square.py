'''
Word Squares

https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/#!
'''

from itertools import permutations

list1 = ['BALL', 'AREA', 'LEAD', 'LADY']
list2 =['LADY', 'AREA', 'DEAR', 'YARD']
list3 = ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']

# Sort by first character of each word in a list
def sort_list(u_list):
  s_list = [] # Sorted list variable

  for item in sorted(u_list):
    s_list.append(item)
  return s_list

# Function to determine if given input containts a word square
def square_check(w_list): 
  w_len = len(w_list[0])
  ws_bool = True
  
  if len(w_list[0]) == 1:
    return ('Word Square: %s\n' % ws_bool)

  # Exit the loop
  for r in range(0, len(w_list)):
    # Check that all rows are of the same length
    if len(w_list[r]) != w_len:
      ws_bool = False
      break
     
    # If the array equals its transpose then we have a square
    for i in range(0, len(w_list[r])):
      if w_list[r][i] != w_list[i][r]:
        ws_bool = False
        break
          
  if ws_bool == True:
	  print(w_list)
	  print('Word Square: %s\n' % ws_bool)
	
  return ws_bool

# Check if a list/sorted is a square
square_check(list1)
square_check(sort_list(list1))
square_check(list2)
square_check(sort_list(list2))

# n choose k permutation
per = list(permutations(list3, len(list3[0])))

# Iterate through the permutations and check for squares
for item in per:  
  square_check(item)

#square_check(['BOe'])
square_check([''])
