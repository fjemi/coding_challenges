# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd



# data
heights = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
# list compression. determine index of each element of heights
index = [i for i in range(0, len(heights))]
volumes = []
v_list = []
total_volume = 0
  
def determine_volume(lst):
  """determine the volume of water between two heights"""
  for i in range(0, len(heights)):
    try: 
      v = heights[i] - heights[i - 1]
      if v > 0:
        v = 0
      else:
        v = abs(v)
    except:
      v = 0
    
    volumes.append(v)
  volumes.reverse()
  total_volume = sum(volumes)
  
  return (volumes, total_volume)

dv = determine_volume(heights)
print('height: %s' % heights)
print('volume: %s' % dv[0])
print('total volume: %s' % dv[1])

# y-axis in bold
rc('font', weight='bold')

# values of each group
bars1 = heights
bars2 = volumes

# position of the barts on the x-axis
r = index

# names of the group and bar width
names = index
barwidth = 1

# create brown bars
plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barwidth)
# create blue bars
plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barwidth)

# custome x axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")
 
# Show graphic
plt.show()




