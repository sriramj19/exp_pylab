__author__ = "Sriram Jayaraman"

import pylab as plt

positions = ['GK', 'LCD', 'RCD', 'LB', 'RB', 'LCM', 'RCM', 'LW', 'RW', 'LS', 'RS']
print("Enter the heights of the various players(The first Eleven): ")
heights = [int(x) for x in input().split()]
if len(heights) != len(positions):
    print("Insufficient Data")
    exit(0)
np_positions=plt.array(positions)
np_heights=plt.array(heights)
x = range(len(np_positions))
plt.xticks(x, np_positions)
plt.plot(x,np_heights,"g")
plt.show()