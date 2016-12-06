# Write list to file, every item on a new line
def writefile(file, input):
	outfile = open(file, "w")
	print >> outfile, "\n".join(str(i) for i in input)
	outfile.close()

# Reads list from file
# File must have int or float, one value per line
def readfile(file):
	temp = open(file).readlines()
	output = [int(float(i.strip())) for i in temp]
	rounded = [round(i,-5) for i in output] # Rounded to 5 zeros before comma
	return rounded

# Merge file1 and file2 to outputfile
def merge(file1, file2, outputfile):
	temp1 = readfile(file1)
	temp2 = readfile(file2)
	thelist = temp1 + temp2
	stripped = [i.strip() for i in thelist]
	allint = [int(float(i)) for i in stripped]
	writefile(outputfile, allint)
