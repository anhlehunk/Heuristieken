from graphics import *

WIDTH=160
HEIGHT=150
STRUCTURELIST=[]

def print_list(list):
	# Prints every sublist on a new ine
	for i in list:
		print i

def make_list():
	# Makes empty 2d list with dimensions height x width
	newlist = [[0 for i in range(WIDTH)]for j in range(HEIGHT)]
	return newlist

def add_structure(tdlist, start_x, start_y, value, heigth, width):
	# Adds an item to 2d list
	# Start_x: top left x coordinate (int)
	# Start_y: top left y coordinate (int)
	# Value: value of item added (int or string)
	# Height: height of structure to add (int)
	# Width: width of structure to add (int)
	# TODO check to see if out of range
	STRUCTURELIST.append(((start_x,start_y), (start_x+width, start_y+heigth), (value)))
	for x in range(start_x, start_x + width):
		for y in range(start_y, start_y + heigth):
			tdlist[y][x] = value
	return tdlist	

def old_draw_array(tdlist):
	# Uses graphics lib to draw the 2d list
	win = GraphWin("Map",WIDTH,HEIGHT)
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

def new_draw_array(tdlist):
	win = GraphWin("Map",WIDTH, HEIGHT)

	# Draw green background
	grass = Rectangle(Point(0,0), Point(WIDTH,HEIGHT))
	grass.setFill('green')
	grass.setOutline('green')
	grass.draw(win)

	# Get coordinates and values from STRUCTURELIST
	for tuple in STRUCTURELIST:
		# tuple: ((x1,y1), (x2,y2), (value))
		topleft = tuple[0]
		bottomright = tuple[1]
		value = tuple[2]
		structure = Rectangle(Point(topleft[0],topleft[1]), Point(bottomright[0], bottomright[1]))
		if value == 1:
			structure.setFill('blue')
			structure.setOutline('blue')
		elif value == 2:
			structure.setFill('black')
			structure.setOutline('black')
		# etc for other structures
		else:
			print "Structure value not defined"
		structure.draw(win)


	# Make window
	win.getMouse()
	win.close()

# Make list from HEIGHT and WIDTH
two_d_list = make_list()

# Adds structure with top left coordinates (10,10), heigth 50, width 25 and value 1
add_structure(two_d_list, 10, 10, 1, 50, 25)

# Draws the list
new_draw_array(two_d_list)




# Sources
# https://www.dotnetperls.com/2d-python
# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/graphics.html
# http://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
# http://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item
