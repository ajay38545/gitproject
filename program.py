def cube(x):
    return x**2

print "MAP EXMAPLE"
cube  = map(cube, range(10))
print cubes

print "LAMBDA EXAMPLES"

print (lambda x: x**2)(5)

print (lambda x, y: x*y) (3, 4)

print "FILTER EXAMPLE"

special_cubes = filter(lambda x: x > 9 and x < 60, cubes)

print special_cube
