'''

Word Squares

 

https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/#!

'''

 

list1 = ['BALL', 'AREA', 'LEAD', 'LADY']
list2 =['LADY', 'AREA', 'DEAR', 'YARD']
list3 = ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']

square_list = []

# Sort by first character of each word in a list
def sort_list(u_list):
  s_list = [] # Sorted list variable

  for item in sorted(u_list):
    s_list.append(item)
  return s_list

print(sort_list(list1))

# Function to determine if given input containts a word square
def square_check(w_list): 
  ws_bool = False
  w_len = len(w_list[1])
  ws_bool = True

  for r in range(0, len(w_list)):
    print(list(w_list[r]))

    if len(w_list[r]) != w_len:
      ws_bool = False

    for i in range(0, len(w_list[r])):
        if w_list[r][i] != w_list[i][r]:
          ws_bool = False

  if ws_bool:
    return 'This list is a word square\n'
  else:
    return 'This list is not a word square\n'

print(square_check(list1))
print(square_check(sort_list(list1)))
print(square_check(list2))
print(square_check(sort_list(list2)))
