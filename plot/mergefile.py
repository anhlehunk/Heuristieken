import sys

arglist = sys.argv

file1 = arglist[1]
file2 = arglist[2]
output = arglist[3]


# Write list to file, every item on a new line
def writefile(file, input):
	outfile = open(file, "w")
	print >> outfile, "\n".join(str(i) for i in input)
	outfile.close()

# Reads list from file
def readfile(file):
	temp = open(file).readlines()
	output = [int(float(i.strip())) for i in temp]
	return output

# Merge file1 and file2 to outputfile
def merge(file1, file2, outputfile):
	temp1 = readfile(file1)
	temp2 = readfile(file2)
	thelist = temp1 + temp2
	#stripped = [i.strip() for i in thelist]
	allint = [int(float(i)) for i in thelist]
	writefile(outputfile, allint)

merge(file1, file2, output)
