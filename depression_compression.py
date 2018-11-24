'''
Compression/Depression coding challenge

https://techdevguide.withgoogle.com/resources/compress-decompression/#!
'''
t1 = '3[abc]4[ab]c' # Test case 1
t2 = '2[3[a]b]'		# Test case 2

c_string = t2 	# Compressed input sring
d_string = '' 	# Decompressed output string

d_dummy = '' 	#

b_dict = {} 	# Dictionary for bracket indecies


c_count = 0 	# Open bracket counter
o_count = 0 	# Closed bracket counter
c_total = c_string.count('[') 	# Count the number of occurances of the open bracket
print('total open brackets: %s\n' % c_total)

for index, char in enumerate(c_string): 	# Iterate through the string to find bracket pairs
	print(index, char) 
	
	if char == '[':
		b_dict[o_count] = [index, '', 'c_dummy[:index]', ''] 	# Add a new key to the dictionary
		o_count += 1
		
	elif char == ']':
		if c_count == c_total:
			c_actual = c_total
		else:
			c_actual = c_count
		try:
			b_dict[c_actual][1] = index 	# Add a new value to a dictionary key
			b_dict[c_actual][2] = c_string[(b_dict[c_actual][0]+1):b_dict[c_actual][1]]
		
			if c_actual == 0:
				b_dict[c_actual][3] = c_string[:b_dict[c_actual][0]]
			else:
				b_dict[c_actual][3] = c_string[(b_dict[c_actual - 1][1] + 1):b_dict[c_actual][0]]
			
			d_dummy += b_dict[c_actual][2] * int(b_dict[c_actual][3]) 	# Overload multiplication to repeat a string an integer number of times
		
			c_count += 1
			c_actual -= 1
		except:
			print('hi')
	
print('open brackets: %s\nclosed brackets: %s\n' % (c_count, o_count))
print(b_dict)
print(b_dict[1][0]) 	# Print a dictionary key/value
try: 	# Error handler: Try/Except
	print(b_dict[0])
except:
	print(0)
print(d_dummy)
