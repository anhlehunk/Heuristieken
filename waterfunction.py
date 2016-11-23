def createWater(n, M):


	split = [0] + [rand(0, 1) for _ in range(0,n-1)] + [1]
	split.sort()

	#this creates the list with randint(1,4) ints, with a random value between 0 and 1
	diff = [x - split[i - 1] for i, x in enumerate(split)][1:]

	#surface is a copy of diff, where the items in the list are duplicated by the WATERSURFACE
	surfaces = diff[:]
	surfaces = [x * WATERSURFACE for x in surfaces]

	#calculates (duplicates) the x's with the filled in M (in our case, a certain surface)
	result = map(lambda x:x*M, diff)

	
	
	print("SPLITS", split)
	print ("This is the sum of the surfaces of the water")
	print (sum(surfaces))
	print ("						")
	print ("these are the random generated surfaces of the water")
	print (surfaces)
	print ("						")
	
	

	return result

result = createWater(randint(1,4),WATERSURFACE)

print (result)
print ("")
print (sum(result))
