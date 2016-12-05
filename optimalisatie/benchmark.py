from timeit import timeit

print "Power"

print "i * i: ", timeit('i * i', setup='i = 5')

print "**: ", timeit('7. ** i', setup='i = 5')

print "pow: ", timeit('pow(7., i)', setup='i = 5')

print "math.pow(): ", timeit('math.pow(7, i)', setup='import math; i = 5')

print "Root"

print "**.05: ", timeit('7. ** .5')

print "math.sqrt(): ", timeit('math.sqrt(7)', setup='import math')
