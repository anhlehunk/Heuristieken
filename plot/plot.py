import matplotlib.pyplot as plt
from collections import Counter, OrderedDict

# Reads list from file
def readfile(file):
	temp = open(file).readlines()
	output = [int(i.strip()) for i in temp]
	rounded = [round(i,-5) for i in output] # Rounded to 5 zeros before comma
	return rounded

# Y is list from file
y = readfile("values.txt")

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
plt.setp(labels, rotation=90)

# Show plot
plt.show()
