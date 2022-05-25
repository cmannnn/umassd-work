# 04/26/2022
# author: Chris Murphy
# MTH 280 homework 5

# imports
import numpy as np
import matplotlib.pyplot as plt

def finite_difference(y, a, dx):
"""Input
=====
y: pass a function y that is the python implementation of y(x)
a: where you want to evaluate the derivative
dx: equations

Output
======
Returns the value of the finite difference approximation for the
derivative of y(x) at x = a"""

	# return approximation of derivative 
	return (y(a + np.sum(dx)) - y(a)) / np.sum(dx)

# passing sin(x) function to pass to finite_difference() function 
def my_function(x):
	return np.sin(x)

# creating 1000 points from neg pi to pi as a to pass to finite_difference()
a = np.linspace(-np.pi, np.pi, 1000)

# main for loop, creating dx to find derivative at 4, 2, 1, .5, .1
for dx in [4, 2, 1, .5, .1]: 

	# calling finite_difference() function
	dy_dx = finite_difference(my_function, a, dx)

	# plotting ax all dx points
	plt.plot(a, dy_dx, linewidth = 4)

# plotting actual derivative cos() 
plt.plot(a, np.cos(a), 'k')

# creating a plot title
plt.title('Finite difference approximation of sin(x)')

# creating a plot legend
plt.legend(['dx = 4.0', 'dx = 2.0', 'dx = 1.0', 'dx = 0.50', 'dx = 0.10', 'cos(x)'])

# show plot
plt.show()





