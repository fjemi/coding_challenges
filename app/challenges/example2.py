'''
This is an example of using the numpy library to create a 
matrix and print out the properties of matrix (shape, length, width, etc.).
It also contains a tree treversal example (recursive).

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

# Print the element at index (1,2)
print('Array[1,2]: %s\n' % str(a[1][2]))

# Recursively check for connected nodes
color_count = {'blue': 0, 'red': 0, 'green': 0}
for i in range(0, a.shape[0]):
	for j in range(0, a.shape[1]):
	
		if j < (a.shape[1] - 1) and i < (a.shape[0] - 1):
			if a[i][j] == a[i+1][j]:
				color_count[str(a[i][j])] += 1
			if a[i][j] == a[i][j +1]:
				color_count[str(a[i][j])] += 1
		
		elif i == (a.shape[0] - 1) and j < (a.shape[1] - 1):
			if a[i][j] == a[i][j+1]:
				color_count[str(a[i][j])] += 1
				
		elif j == (a.shape[1] - 1) and i < (a.shape[0] - 1):
			if a[i][j] == a[i+ 1][j]:
				color_count[str(a[i][j])] += 1
		
			
print('Connect nodes by color: %s\n' % str(color_count))




