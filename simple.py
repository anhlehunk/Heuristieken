from graphics import *

def print_list(list):
	# Prints every sublist on a new ine
	for i in list:
		print i

def make_list(height, width):
	# Makes empty 2d list with dimensions height x width
	newlist = [[0 for i in range(width)]for j in range(height)]
	return newlist

def get_height(tdlist):
	# Returns height of list, obsolete if height is global variable
	return len(tdlist)

def get_width(tdlist):
	# Returns width of list, obsolete if width is global variable
	return len(tdlist[0])

def add_structure(tdlist, start_x, start_y, value, heigth, width):
	# Adds an item to 2d list
	# Start_x: top left x coordinate (int)
	# Start_y: top left y coordinate (int)
	# Value: value of item added (int or string)
	# Height: height of structure to add (int)
	# Width: width of structure to add (int)
	# TODO check to see if out of range
	for x in range(start_x, start_x + width):
		for y in range(start_y, start_y + heigth):
			tdlist[y][x] = value
	return tdlist	

def draw_array(tdlist):
	# Uses graphics lib to draw the 2d list
	win = GraphWin("Map",get_width(tdlist),get_height(tdlist))
	for y in enumerate(tdlist):
		for x in enumerate(y[1]):
			if x[1] == 0:
				pt = Point(x[0], y[0])
				pt.setFill('green')
			elif x[1] == 1:
				pt = Point(x[0], y[0])
				pt.setFill('blue')
			# and so on
			else:
				print "Add color for value"
			pt.draw(win)
	win.getMouse()
	win.close()

	
# Test
# Make list
two_d_list = make_list(150,160)
# Add some water
add_structure(two_d_list, 10, 10, 1, 50, 25)
# Draw the map
draw_array(two_d_list)


# Sources
# https://www.dotnetperls.com/2d-python
# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/graphics.html
# http://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
# http://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item
