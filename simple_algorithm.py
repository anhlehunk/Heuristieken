from graphics import *
from random import randint
import weakref

# Classes
class small_house:

	width = 8*2
	height = 8*2
	min_free = 2*2
	worth = 285000
	value = 2

	instances = []

	def __init__(self, x, y, name=None):
		self.__class__.instances.append(weakref.proxy(self))
		self.x = x
		self.y = y
		self.name = name

class medium_house:

	width = 10*2
	height = int(7.5*2) # Convert float to int
	min_free = 3*2
	worth = 399000
	value = 3

	instances = []

	def __init__(self, x, y, name=None):
		self.__class__.instances.append(weakref.proxy(self))
		self.x = x
		self.y = y
		self.name = name

class big_house:

	width = 11*2
	height = int(10.5*2) # Convert float to int
	min_free = 6*2
	worth = 610000
	value = 4

	instances = []

	def __init__(self, x, y, name=None):
		self.__class__.instances.append(weakref.proxy(self))
		self.x = x
		self.y = y
		self.name = name
     
# Test
#house1 = small_house(10,20, "house1")
#house2 = small_house(30,40, "house2")
#house3 = small_house(50,60, "house3")
#house4 = small_house(70,80, "house4")
#house5 = small_house(90,100, "house5")
#house6 = small_house(110,120, "house6")
#for instance in small_house.instances:
#    print(instance.name, instance.x, instance.y)


# Define map size and structures
WIDTH=320
HEIGHT=300
STRUCTURELIST=[]

# Values for different type of structures
WATER=1
HOUSE_SMALL=2
HOUSE_MEDIUM=3
HOUSE_LARGE=4

def print_list(list):
	# Prints every sublist on a new ine
	for i in list:
		print i

def make_list():
	# Makes empty 2d list with dimensions height x width
	newlist = [[0 for i in range(WIDTH)]for j in range(HEIGHT)]
	return newlist

def add_structure(tdlist, start_x, start_y, value, heigth, width, amount):
	# Adds an item to 2d list
	# Start_x: top left x coordinate (int)
	# Start_y: top left y coordinate (int)
	# Value: value of item added (int or string)
	# Height: height of structure to add (int)
	# Width: width of structure to add (int)
	# TODO check to see if out of range
	tdlistcopy = tdlist
	for x in range(start_x, start_x + width):
		for y in range(start_y, start_y + heigth):
			if tdlist[y][x] != 0:
				# Only prints warning, still adds structure to map
				print "overlap found, placing again."
				return tdlistcopy, amount+1
			else:
				tdlist[y][x] = value
				#if value == 2:
				#	print "value is 2"
				#elif value == 3:
				#	print "value is 3"
				#elif value == 4:
				#	print "value is 4"
				#else:
				#	print "Water class not done"
	# Should only append if no overlap, but now appends everything
	STRUCTURELIST.append(((start_x,start_y), (start_x+width, start_y+heigth), (value)))
	return tdlist, amount	

def add_water(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(0,290), randint(0,270), WATER, randint(10,30), randint(10,30), amount)
		amount -=1

def add_small_house(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(small_house.min_free,WIDTH-small_house.min_free-small_house.width), randint(small_house.min_free,HEIGHT-small_house.min_free-small_house.height), HOUSE_SMALL, small_house.height, small_house.width, amount)
		amount -=1

def add_medium_house(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(medium_house.min_free,WIDTH-medium_house.min_free-medium_house.width), randint(medium_house.min_free,HEIGHT-medium_house.min_free-medium_house.height), HOUSE_MEDIUM, medium_house.height, medium_house.width, amount)
		amount -=1

def add_big_house(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(big_house.min_free,WIDTH-big_house.min_free-big_house.width), randint(big_house.min_free,HEIGHT-big_house.min_free-big_house.height), HOUSE_LARGE, big_house.height, big_house.width, amount)
		amount -=1
			
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
		elif value == 3:
			structure.setFill('red')
			structure.setOutline('red')
		elif value == 4:
			structure.setFill('purple')
			structure.setOutline('purple')
		else:
			print "Structure value not defined"
		structure.draw(win)

	# Make window
	win.getMouse()
	win.close()

# Make list from HEIGHT and WIDTH
two_d_list = make_list()

# Adds structues on random places
#add_water(randint(1,4), two_d_list)
#add_small_house(12, two_d_list)
#add_medium_house(6, two_d_list)
#add_big_house(5, two_d_list)

# Draws the list
#new_draw_array(two_d_list)
