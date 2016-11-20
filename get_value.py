import copy
import math

thelist = [[0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0],
		   [0,1,1,0,0,0,0,1,1,0],
		   [0,1,1,0,0,0,0,1,1,0],
		   [0,0,0,0,0,0,0,0,0,0]]

struclist = [((1,7), (2,8), 1), ((7,7), (8,8), 1)]
#(start_x,start_y), (start_x+width, start_y+heigth), (value))

def score(struclist):
	total_value = 0
	for i in struclist:
		start_y = i[0][1]
		end_y = i[1][1]+1 #+1 wss ook oplossing voor ons probleem
		start_x = i[0][0]
		end_x = i[1][0]+1

		copy_list = copy.deepcopy(thelist)
		coordinates_selected_house = []

		for x in range(start_x, end_x):
			for y in range(start_y, end_y):
				copy_list[y][x] = 9	
				coordinates_selected_house.append([y,x])
				
		for count in range(len(thelist)):
			other_house = check_surrounding(start_y - count, end_y + count, start_x - count, end_x + count, count, copy_list)
			
			if other_house != None:
				shortest_distance = distance(coordinates_selected_house, other_house)
				print shortest_distance
				break


					
				
def check_surrounding(start_y, end_y, start_x, end_x, count, copy_list):

	start_x = check_negative(start_x)
	start_y = check_negative(start_y)
	end_y = check_negative(end_y)
	end_x = check_negative(end_x)
				
	list = copy_list[start_y:end_y]
	base_list = []	
	count_y = 0
	
	for y in list:
		x_row = y[start_x:end_x]
		base_list.append(x_row)
		if 1 in base_list[-1]:
			print x_row
			print "^ found other building"
			return [count_y + start_y, base_list[-1].index(1)+start_x]
		print x_row	
		count_y += 1		
	print " "
	return None
	
	
def check_negative(number):
	if number < 0:
		return 0
	else:
		return number
	
	
def distance(house_1, house_2):
	distances = []
	for coordinate in house_1:
		distances.append(math.sqrt(math.pow(coordinate[0] - house_2[0], 2)+math.pow(coordinate[1] - house_2[1],2 )))
	return min(distances)
		

score(struclist)
