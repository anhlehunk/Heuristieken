import matplotlib.pyplot as plt
from collections import Counter, OrderedDict
import numpy as np
import sys

# Get list of arguments
arglist = sys.argv

# Set arguments
arg1 = arglist[1]

# Reads list from file
# File must have int or float, one value per line
def readfile(file):
	temp = open(file).readlines()
	output = [int(float(i.strip())) for i in temp]
	return output

FILE = str(arg1)

# Y is list from file
x = readfile(FILE)

# Average and standard deviation
avg = sum(x)/len(x)
std = np.std(x)
med = np.median(x)

# Normally distributed data
print ("Normal distribution: ")
print ("Average value: ", round(avg, 1))
print ("Standard deviation: ", round(std, 0))
print ("Approx. 68% of values between: ", int(round(avg - 1*std, -2)), " and ", int(round(avg + 1*std, -2)))
print ("Approx. 95% of values between: ", int(round(avg - 2*std, -2)), " and ", int(round(avg + 2*std, -2)))
print ("Approx. 99% of values between: ", int(round(avg - 2*std, -2)), " and ", int(round(avg + 3*std, -2)))
print ("Highest found value: ", max(x))
print ()

# Skewed data
print ("Skewed distribution:  ")
print ("Median: ", med)
print ("Better than 75% if value is higher than: ", np.percentile(x,75))
print ("Better than 95% if value is higher than: ", np.percentile(x,95))
print ("Better than 99% if value is higher than: ", np.percentile(x,99))
print ("Highest found value: ", max(x))

# Round values here
y = [round(i,-5) for i in x]
# Count each value
count= Counter(y)

# Make dictionary from counter object
D = dict(count)

# Order dictionary by key
od = OrderedDict(sorted(D.items()))

# Plot od
plt.bar(range(len(od)), od.values(), align='center')
plt.xticks(range(len(od)), list(od.keys()))
locs, labels = plt.xticks()
plt.setp(labels, rotation=45)

# Show plot
plt.show()
