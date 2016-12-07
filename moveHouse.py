# the append part of the add_structure function is changed into the code below:
#STRUCTURELIST.append([[start_x,start_y], [start_x+width, start_y+height], value])



def move_house():
	#choosing a random structure or house in the structurelist
	random_structure = random.choice(STRUCTURELIST)

	#value of the house (which house is it)
	kind_of_house = random_structure[2]
	print ("value",kind_of_house," list: ", random_structure)

	#take the needed values: the start and the end coordinates:
	sliced =  random_structure[:2]

	print ("sliced===>", sliced)

	#divide them into two lists: start coordinate and end coordinate
	edit_slice_start = sliced[0]
	edit_slice_end = sliced[1]


	#random values for addition OR substraction
	#so: addition OR substraction of the height or width value
	add_sub_height = randint(1,2) #50% chance to increase or decrease height
	add_sub_width = randint(1,2)  #50% chance to increase or decrease width	
	

	
	if kind_of_house == 2:
		print("Dit is het random gekozen huis: ", random_structure)
		#random addition or substraction for the y coordinate
		if add_sub_height == 1:
			#change the start_y coordinate and the end_y
			#move the house a certain height that is left between the house and the end of the map
			random_change_height = randint(1 ,HEIGHT- edit_slice_end[1]-small_house.min_free)

			#calculate the random height
			edit_slice_start[1] += random_change_height
			edit_slice_end[1] += random_change_height
			

		if add_sub_height == 2:
			
			random_change_height = randint(1 ,edit_slice_start[1] - small_house.min_free)
			edit_slice_start[1] -= random_change_height
			edit_slice_end[1] -= random_change_height


		
		#random addition or substraction for the x coordinate
		if add_sub_width == 1:	
			#change the start_x coordinate and the end_x
			random_change_width = randint(1 ,WIDTH- edit_slice_end[0]-small_house.min_free)
			edit_slice_start[0] += random_change_width
			edit_slice_end[0] += random_change_width


		if add_sub_width == 2:	
			random_change_width = randint(1 ,edit_slice_start[0] ) - small_house.min_free
			edit_slice_start[0] -= random_change_width
			edit_slice_end[0] -= random_change_width


	if kind_of_house == 3:
		print (add_sub_height)
		print (add_sub_width)
	
		print("Dit is het random gekozen huis: ", random_structure)
		#random addition or substraction for the y coordinate
		if add_sub_height == 1:
			#change the start_y coordinate and the end_y
			random_change_height = randint(1 ,HEIGHT- edit_slice_end[1]-medium_house.min_free)
			edit_slice_start[1] += random_change_height
			edit_slice_end[1] += random_change_height

		if add_sub_height == 2:
			
			random_change_height = randint(1 ,edit_slice_start[1] - medium_house.min_free)
			edit_slice_start[1] -= random_change_height
			edit_slice_end[1] -= random_change_height


		#random addition or substraction for the x coordinate
		if add_sub_width == 1:	
			#change the start_x coordinate and the end_x
			random_change_width = randint(1 ,WIDTH -edit_slice_end[0]-medium_house.min_free)
			edit_slice_start[0] += random_change_width
			edit_slice_end[0] += random_change_width


		if add_sub_width == 2:	
			print (edit_slice_end[0])
			random_change_width = randint(1 ,edit_slice_start[0] ) - medium_house.min_free
			edit_slice_start[0] -= random_change_width
			edit_slice_end[0] -= random_change_width

		

			

	if kind_of_house == 4:
		print("Dit is het random gekozen huis: ", random_structure)
		#random addition or substraction for the y coordinate
		if add_sub_height == 1:
			#change the start_y coordinate and the end_y
			random_change_height = randint(1 ,HEIGHT- edit_slice_end[1]) -big_house.min_free
			edit_slice_start[1] += random_change_height
			edit_slice_end[1] += random_change_height

		if add_sub_height == 2:
			
			random_change_height = randint(1 ,edit_slice_start[1] ) - big_house.min_free
			edit_slice_start[1] -= random_change_height
			edit_slice_end[1] -= random_change_height


		#random addition or substraction for the x coordinate
		if add_sub_width == 1:	
			#change the start_x coordinate and the end_x
			random_change_width = randint(1 ,WIDTH- edit_slice_end[0]-big_house.min_free)
			edit_slice_start[0] += random_change_width
			edit_slice_end[0] += random_change_width


		if add_sub_width == 2:	
			random_change_width = randint(1 ,edit_slice_start[0] ) - big_house.min_free
			edit_slice_start[0] -= random_change_width
			edit_slice_end[0] -= random_change_width

	
	print("Dit is het nieuw plekje: ", random_structure)
	
	
