'''tree treversal example (recursive).
www.youtube.com/watch?v=IWvbPIYQPFM
'''

import numpy as np

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
