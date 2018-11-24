'''
Compression/Depression coding challenge

https://techdevguide.withgoogle.com/resources/compress-decompression/#!
'''

c_string = '3[abc]4[ab]c' # Compressed input sring
d_string = '' # Decompressed output string

d_dummy = '' #

b_dict = {} # Dictionary for bracket indecies

# Counters for the open and closed brackets, example 
c_count = 0
o_count = 0

for index, char in enumerate(c_string): # Iterate through the string to find bracket pairs
	print(index, char) 
	
	if char == '[':
		b_dict[o_count] = [index, '', 'c_dummy[:index]', ''] # Add a new key to the dictionary
		o_count += 1
		
	if char == ']':
		
		b_dict[c_count][1] = index # Add a new value to a dictionary key
		b_dict[c_count][2] = c_string[(b_dict[c_count][0]+1):b_dict[c_count][1]]
		
		if c_count == 0:
			b_dict[c_count][3] = c_string[:b_dict[c_count][0]]
		else:
			b_dict[c_count][3] = c_string[(b_dict[c_count - 1][1] + 1):b_dict[c_count][0]]
			
		d_dummy += b_dict[c_count][2] * int(b_dict[c_count][3]) # Overload multiplication to repeat a string an integer number of times
		
		c_count += 1
	
print('open brackets: %s\nclosed brackets: %s\n' % (c_count, o_count))
print(b_dict)
print(b_dict[1][0]) # Print a dictionary key/value
try: # Error handler: Try/Except
	print(b_dict[0])
except:
	print(0)
print(d_dummy)
