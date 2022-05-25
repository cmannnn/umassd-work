import numpy as np
import matplotlib.pyplot as plt



def riemann_sum(integrand, xleft, xright, rectangles):
	""" Input
	=====
	integrand -- takes integrand function
	rectangles -- number of rectangles used to compute the Riemann sum
	xleft -- left value of integration (default = 0.0)
	xright -- right value of integration (default = 2.0)"""

	# compute the width of each rectangle
	dx = (xright - xleft) / rectangles

	# generate a uniform grid (equally spaced) of x-values
	# each x value is located in the middle of a rectangle
	x0 = xleft + dx/2.0

	xend = xright - dx/2.0
	x_points = np.linspace(x0, xend, rectangles)

	# evaluate the function at the middle of each rectangle
	y_values = integrand(x_points)

	# print x and y values -- code check
	# print(y_values)
	# print(x_points)

	# numerically compute the integral by a Riemann sum
	integral = np.sum(y_values) * dx
	print( "integral = %1.15e"%integral )
	print( "integral error = %1.15e"%(integral-1.0) )