'''
This is an example of using the numpy library to create a matrix and print out the properties of matrix (shape, length, width, etc.). It also contains the solution to a Google interview question on 

www.youtube.com/watch?v=IWvbPIYQPFM
'''

import numpy as np

# Create an array
a = np.array([['blue', 'green', 'red'],
	['blue', 'blue', 'green'],
	['red', 'blue', 'green'],
	['red','red','blue']])

# Print the array	
print('Array:')
print(a)

# Print the size of the array
print('\nArray shape: %s' % str(a.shape))
print('Width: %s' % str(a.shape[1]))
print('Length: %s\n' % str(a.shape[0]))

# Print each row of the array	
count = 1
for row in a:
	print('Row %d: %s' % (count, str(row)))
	count += 1
print('\n')

# Print each element of the array
count = 1
for i in range(0, a.shape[0]):
	for j in range(0, a.shape[1]):
		print('Element %d: %s' % (count, a[i][j]))
		count += 1
print('\n')

# 
color_count = {'blue': 0, 'red': 0, 'green': 0}
for i in range(0, a.shape[0] - 1):
	for j in range(0, a.shape[1]):
		#print(color_count[a[i][j]])
		if j == a.shape[1]-1:
			if a[i][j] == a[i+1][j]:
				print('test')
		
		'''if a[i][j] == a[i+1][j]:
			color_count[str(a[i][j])] += 1
		if a[i][j] == a[i][j+1]:
			color_count[str(a[i][j])] += 1'''
			
print(color_count)
print(color_count['blue'])
color_count['blue'] += 1
print(color_count['blue'])




print(a[1][2])
