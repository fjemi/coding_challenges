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
  w_len = len(w_list[1])
  ws_bool = True

  # Exit the loop
  for r in range(0, len(w_list)):
    if len(w_list[r]) != w_len:
      ws_bool = False
      break

    for i in range(0, len(w_list[r])):
      if w_list[r][i] != w_list[i][r]:
        ws_bool = False
        break
          
  if ws_bool == True:
	  print(w_list)
	  print('Word Square: %s\n' % ws_bool)
	
  return ws_bool

square_check(list1)
square_check(sort_list(list1))
square_check(list2)
square_check(sort_list(list2))

per = tuple(permutations(list3, len(list3[0])))
p_list = []
count1 = 0
count2 = 0

'''for i in per:
	if square_check(i):
		print('hi')'''
	#print('Word Square: %s\n' % square_check(i))
		


