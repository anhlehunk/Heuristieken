from graphics import *
from random import randint
from random import uniform as rand
from random import choice
import weakref
import math

#  python -m cProfile -s time alg.py > profile.text 2>&1

# Classes
class small_house:

	width = 8*2
	height = 8*2
	min_free = 2*2
	worth = 285000
	value = 2

	instances = []

	def __init__(self, x, y, ID=None):
		self.x = x
		self.y = y
		self.ID = ID

class medium_house:

	width = 10*2
	height = int(7.5*2) # Convert float to int
	min_free = 3*2
	worth = 399000
	value = 3

	instances = []

	def __init__(self, x, y, ID=None):
		self.x = x
		self.y = y
		self.ID = ID

class big_house:

	width = 11*2
	height = int(10.5*2) # Convert float to int
	min_free = 6*2
	worth = 610000
	value = 4

	instances = []

	def __init__(self, x, y, ID=None):
		self.x = x
		self.y = y
		self.ID = ID

# Define map size and structures
WIDTH=320
HEIGHT=300
WATERSURFACE = WIDTH*HEIGHT*.2
STRUCTURELIST=[]

# Values for different type of structures
WATER=1
HOUSE_SMALL=2
HOUSE_MEDIUM=3
HOUSE_LARGE=4

def make_list():
	# Makes empty 2d list with dimensions height x width
	newlist = [[0 for i in range(WIDTH)]for j in range(HEIGHT)]
	return newlist
	
def create_water(tdlist):
	# Makes 4 water structures of equal size in surface
	surfaces = [.25 * WATERSURFACE for x in range(4)]

	# Counter
	count = 0

	# Changes dimensions of the water structures below
	for water in surfaces:
		dimension = math.sqrt(water)
		
		#Makes sure that the proportion is not more than 1:4
		new_proportion = 2
		dimensions = [int(dimension * new_proportion), int(dimension / new_proportion)]
		height_water = dimensions[1]
		width_water = dimensions[0]

		# Add water and update count for new coordinates
		tdlist, amount = add_structure(tdlist, 70 , 34 + 68*count, 1, height_water, width_water, 1)
		count += 1

def add_structure(tdlist, start_x, start_y, value, height, width, amount):
	# Adds an item to 2d list
	# Start_x: top left x coordinate (int)
	# Start_y: top left y coordinate (int)
	# Value: value of item added (int or string)
	# Height: height of structure to add (int)
	# Width: width of structure to add (int)
	end_y_range = start_y + height + 1
	end_x_range = start_x + width + 1

	# Replaced deepcopy with nested list comprehension. Much faster
	copy_list = [[i for i in j] for j in tdlist]

	# Checks whether the coordinate is already taken by free space or other building/water
	for x in range(start_x, end_x_range):
		for y in range(start_y, end_y_range):
			if tdlist[y][x] != 0:
				# Here there is something else on the coordinate on which we wanted to place a house/water
				# This results in this function being called again because the conditions are not met.
				print "overlap found, placing again.    ", len(STRUCTURELIST),"houses placed, ", value, "is selected type house"
				
				return tdlist, amount+1
			else:
				tdlist[y][x] = value
	# Below we check if there is enough free space for the houses which are placed
	# Water doesnt need this, so we start at the value of a small house.
	# Only checks the surroundings of the minimal free space!
	# If there is something else in the surrounding -----> other_house != [] 
	
	# Surrounding of water doesnt need to be checked, so with value ==1 there is nothing else in the vacinity
	if value == 1:
		other_house = []
	# Checks surroundings if we are placing a small house
	if value == 2:
		space = small_house.min_free
		other_house = check_surrounding(start_y - space, end_y_range + space, start_x - space, end_x_range + space, copy_list)
	# Checks surroundings if we are placing a medium house
	if value == 3:
		space = medium_house.min_free
		other_house = check_surrounding(start_y - space, end_y_range + space, start_x - space, end_x_range + space, copy_list)
	# Checks surroundings if we are placing a small house	
	if value == 4:
		space = big_house.min_free
		other_house = check_surrounding(start_y - space, end_y_range + space, start_x - space, end_x_range + space, copy_list)
	# If there are no other houses in the free space of the house, free space is added for the selected house so that nothing else is placed in it later on.
	# This results in this function being called again because the conditions are not met.
	if other_house == [] and value != 1:
		for x in range(start_x - space, end_x_range + space):
			for y in range(start_y - space, end_y_range + space):
				# To make sure that the x and y are not out of bounds (negative or larger than the WIDTH and HEIGHT)
				if x < 0 or y < 0 or x > WIDTH-1 or y > HEIGHT-1:
					print "Free space out of bounds"
					return tdlist, amount+1 
				if tdlist[y][x]== 0:
					tdlist[y][x] = 9
	
	# If there is something in the free space, other house will NOT be equal to an empty list
	# This results in this function being called again because the conditions are not met.
	if other_house != []:
		print "Another house has been located in the minimal free space"
		return tdlist, amount+1
		
	# Should only append if no overlap
	STRUCTURELIST.append(((start_x,start_y), (start_x+width, start_y+height), (value)))

	# Add instances of structure to correct class
	# Amount here is just an identifier
	if value == 2:
		small_house.instances.append(small_house(start_x, start_y, amount))
	elif value == 3:
		medium_house.instances.append(medium_house(start_x, start_y, amount))
	elif value == 4:
		big_house.instances.append(big_house(start_x, start_y, amount))
	return tdlist, amount	
	
def score(struclist, tdlist):
	total_value = 0
	test = []
	for i in struclist:
		start_y = i[0][1]
		end_y = i[1][1]+1 
		start_x = i[0][0]
		end_x = i[1][0]+1
		if i[2] == 1:
			worth = 0
			minimal_free_space = 0
			percentage_increase_value = 0
		# Sets values for all the different kinds of houses
		if i[2] == 2:
			worth = small_house.worth
			minimal_free_space = small_house.min_free
			percentage_increase_value = 0.03
		if i[2] == 3:
			worth = medium_house.worth
			minimal_free_space = medium_house.min_free
			percentage_increase_value = 0.04
		if i[2] == 4:
			worth = big_house.worth
			minimal_free_space = big_house.min_free
			percentage_increase_value = 0.06

		# Replaced deepcopy with nested list comprehension. Much faster
		copy_list = [[i for i in j] for j in tdlist]

		coordinates_selected_house = []

		for x in range(start_x, end_x):
			for y in range(start_y, end_y):
				copy_list[y][x] = 9	
				coordinates_selected_house.append([y,x])
				
		for count in range(len(tdlist)):
			other_house = check_surrounding(start_y - count, end_y + count, start_x - count, end_x + count, copy_list)
			if other_house != []:
				shortest_distance = distance(coordinates_selected_house, other_house)
				added_value = (shortest_distance - minimal_free_space)/2*percentage_increase_value #/2 because the value increases every meter, not half meter.
				total_value += worth*(1+added_value)
				break
	print " Total value: ", total_value

	return total_value
	
def check_surrounding(start_y, end_y, start_x, end_x, copy_list):

	start_x = check_negative(start_x)
	start_y = check_negative(start_y)
	end_y = check_negative(end_y)
	end_x = check_negative(end_x)
				
	list = copy_list[start_y:end_y]
	base_list = []	
	count_y = 0
	return_list = []
	for y in list:
		x_row = y[start_x:end_x]
		base_list.append(x_row)
		count_x = 0
		# Checks if there are other buildings for each row at a time
		# Returns either an empty list if no other buildings are found, but else it returns the coordinates of locations which are already being used.
		for x in base_list[-1]:
			if x == 2:
				print "^ found small building"
				return_list.append([count_y + start_y, count_x+start_x])
			if x == 3:
				print "^ found medium building"
				return_list.append([count_y + start_y, count_x+start_x])
			if x == 4:
				print "^ found big building"
				return_list.append([count_y + start_y, count_x+start_x])
			count_x +=1
		count_y += 1				
	return return_list
	
# This function makes sure that the coordinates are within the bounds of the grid.	
def check_negative(number):
	if number < 0:
		return 0
	else:
		return number	
	
def distance(house_1, house_2):
	distances = []
	for coordinate_1 in house_1:
		for coordinate_2 in house_2:
			# distances.append(math.sqrt(math.pow(coordinate_1[0] - coordinate_2[0], 2)+math.pow(coordinate_1[1] - coordinate_2[1],2 )))  # Old, slower code. Is better readable
			distances.append((((coordinate_1[0] - coordinate_2[0]) * (coordinate_1[0] - coordinate_2[0])) + ((coordinate_1[1] - coordinate_2[1]) * (coordinate_1[1] - coordinate_2[1]))) ** .5 )
	print "Minimal distance ->>>>>>>>>   ",min(distances)
	return min(distances)

# Add structure function filled in with small house values
def add_small_house(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(small_house.min_free,WIDTH-small_house.min_free-small_house.width), randint(small_house.min_free,HEIGHT-small_house.min_free-small_house.height), HOUSE_SMALL, small_house.height, small_house.width, amount)
		amount -= 1

# Add structure function filled with medium house values
def add_medium_house(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(medium_house.min_free,WIDTH-medium_house.min_free-medium_house.width), randint(medium_house.min_free,HEIGHT-medium_house.min_free-medium_house.height), HOUSE_MEDIUM, medium_house.height, medium_house.width, amount)
		amount -=1

# Add structure function filled in with big house values
def add_big_house(amount, tdlist):
	while amount !=0:
		tdlist, amount = add_structure(tdlist, randint(big_house.min_free,WIDTH-big_house.min_free-big_house.width), randint(big_house.min_free,HEIGHT-big_house.min_free-big_house.height), HOUSE_LARGE, big_house.height, big_house.width, amount)
		amount -=1
		
# Old function, only use when new function doesnt work.
# Is many times slower than the new one	
def old_draw_array(tdlist):
	win = GraphWin("Map",WIDTH,HEIGHT)
	for y in enumerate(tdlist):
		for x in enumerate(y[1]):
			if x[1] == 0:
				pt = Point(x[0], y[0])
				pt.setFill('green')
			elif x[1] == 1:
				pt = Point(x[0], y[0])
				pt.setFill('blue')
			elif x[1] == 2:
				pt = Point(x[0], y[0])
				pt.setFill("black")
			elif x[1] == 9:
				pt = Point(x[0], y[0])
				pt.setFill("orange")
			else:
				print "Add color for value"
			pt.draw(win)
	win.getMouse()
	win.close()

# Used to write structuredict to file for analysis
def writetofile( file, input):
	# Write dict to file, used for calculations
	with open( file, 'w' ) as f:
		f.write("{}\n".format(input))

# Used to read structuredict from file
def readfile( file ):
	result  = []
	with open( file ) as f:
		for line in f:	
			result.append( line )

	return result

# Function to draw map from structurelist
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

# Run the random algorithm with variant 1,2 or 3 and with n iterations
def algorithm(variant, n):
	structuredict = {}
	for i in range(n):
		# New structurelist
		STRUCTURELIST = []

		# Debug printing
		print "STRUCTUREDICT", structuredict
		
		# Make list from HEIGHT and WIDTH
		two_d_list = make_list()
	
		# Different amount of structures for different variants
		if variant == 1:
			create_water(two_d_list)
			add_big_house(3, two_d_list)
			add_medium_house(5, two_d_list)
			add_small_house(12, two_d_list)	
		elif variant == 2:
			create_water(two_d_list)
			add_big_house(6, two_d_list)
			add_medium_house(10, two_d_list)
			add_small_house(24, two_d_list)
		elif variant == 3:
			create_water(two_d_list)
			add_big_house(9, two_d_list)
			add_medium_house(15, two_d_list)
			add_small_house(36, two_d_list)
		else:
			print "Variant must be 1,2 or 3"


		print STRUCTURELIST
		# Prints Total value
		value = score(STRUCTURELIST, two_d_list)

		# Add new entry to structuredict
		structuredict.update({ value : STRUCTURELIST })
	
		# Only draw map with 1 iteration
		if n == 1:
			new_draw_array(two_d_list)

		# Write structuredict to file
		writetofile("dict.txt", structuredict)

algorithm(1,1)
