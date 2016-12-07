import matplotlib.pyplot as plt
from collections import Counter, OrderedDict
import numpy as np

# Reads list from file
# File must have int or float, one value per line
def readfile(file):
	temp = open(file).readlines()
	output = [int(float(i.strip())) for i in temp]
	rounded = [round(i,-5) for i in output] # Rounded to 5 zeros before comma
	return rounded

# Define file
FILE = "newvalues.txt"

# Y is list from file
y = readfile(FILE)

# Average and standard deviation
avg = sum(y)/len(y)
std = np.std(y)

# Print some data
print ("Average value: ", avg)
print ("Standard deviation: ", std)
print ("Approx. 68% of values between: ", round(avg - 1*std, -2), " and ", round(avg + 1*std, -2))
print ("Approx. 95% of values between: ", round(avg - 2*std, -2), " and ", round(avg + 2*std, -2))
print ("Approx. 99% of values between: ", round(avg - 2*std, -2), " and ", round(avg + 3*std, -2))

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
plt.setp(labels, rotation=60)

# Show plot
plt.show()
