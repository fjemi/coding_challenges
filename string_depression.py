'''
Compression/Depression coding challenge

https://techdevguide.withgoogle.com/resources/compress-decompression/#!
'''

t1 = '3[abc]4[ab]c' # Test case 1
t2 = '2[3[a]b]'		# Test case 2
t3 = '1[a]2[3[b]]'	# Test case 3


def depression(c_string):	# Function to decompression the string
	count = 0
	bracket_count = 0
	brackets = {}	# Dictionary to store brackets/characters of the string
	
	for index, char in enumerate(c_string): # Enumerate through the index/characters of the string
		#print (index, char)
		
		if bracket_count != count:
			count = bracket_count
		
		if char == '[':
			brackets[count] = [index, '', '', '']	# Add a new key and the opening backets' indexes to the dictionary
			count += 1
			bracket_count += 1
		
		if char == ']':
			brackets[count - 1][1] = index	# Add the closing brackets' indexes to the dictionary 
			brackets[count - 1][2] = c_string[(brackets[count - 1][0] + 1):brackets[count - 1][1]]
			
			'''if count == 1:
				brackets[count - 1][2] = c_string[brackets[count - 1][0]:brackets[count - 1][1]]
			else:
				brackets[count - 1][2] = c_string[brackets[count - 1][0]:brackets[count - 1][1]]'''
			count -= 1
			
		
	print(brackets)
		

depression(t1)
depression(t2)
depression(t3)
		

