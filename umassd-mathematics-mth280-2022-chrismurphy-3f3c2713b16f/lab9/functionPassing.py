def find_max(y, a, b):
	""" INPUT
	=====
	y: the function y(x) to maximize. This function must be able to
	accept a numpy array as input, and it will return a numpy
	array as output. For example:
	>>> xs = np.array( [0, .5, 1])
	>>> ys = y(xs)
	a: the interval's left boundary
	b: the interval's right boundary
	OUTPUT
	======
	max of y(x) such that x is in the interval [a,b]"""
	import numpy as np # import numpy from inside the find_max function

	x_values = np.linspace(a,b,10000) # generate many points in [a,b]
	y_values = y(x_values)
	maximum = np.max(y_values)
	return maximum

def y1(x):
	return 0.5*x
def y2(x):
	import numpy as np
	return np.sin(x)

# call your find_max twice on different intervals and get the result
max_y1 = find_max(y1, -1.0, 1.0)
max_y2 = find_max(y2, -1.0, 2.0)

print(max_y1)
print(max_y2)