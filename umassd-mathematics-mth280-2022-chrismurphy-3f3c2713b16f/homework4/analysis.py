# 04/14/2022
# author: Chris Murphy
# MTH 280 homework 4

# imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def my_function(x):
	""" function to integrate"""
	return 3.0 * x ** 2

def riemann_sum(rectangles, xleft=0.0, xright=2.0):
	""" Input
	=====
	rectangles --- number of rectangles used to compute the Riemann sum
	xleft -- left value of integration (default = 0.0)
	xright -- right value of integration (default = 2.0)"""

	# compute the width of each rectangle
	dx = (xright - xleft) / rectangles

	# generate a uniform grid (equally spaced) of x-values
	# each x value is located in the middle of a rectangle
	x0 = xleft + dx / 2.0

	xend = xright - dx / 2.0
	x_points = np.linspace(x0, xend, rectangles)

	# evaluate the function at the middle of each rectangle
	y_values = my_function(x_points)

	# numerically compute the integral by a Riemann sum
	integral = np.sum(y_values) * dx
	true_integral = integrate.quad(my_function, xleft, xright)

	# returning the approximated integral and the actual integral 
	return integral, true_integral[0]

# setting the rectangles in a list
rectangles = [1, 10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7]

# empty list to hold error values
En = []

# main for loop to calculate the error for each number of rectangles
for i in rectangles:
	p = abs((riemann_sum(i)[0] * .1) - riemann_sum(i)[1] * .1)
	En.append(p)

	# print N
	print(f'N: {i}')

	# print I
	print(f'I {riemann_sum(i)[0] * .1}')

	# print In
	print(f'In: {riemann_sum(i)[1] * .1}')
	
	# print En
	print(f'En: {p}')
	print(' ')

# checking plotting values
# print(rectangles)
# print(' ')
# print(En)

# plotting rectangles on the x axis and the error on the y axis with a log log plot
plt.loglog(rectangles, En)
plt.title('Riemann sum integral vs error')
plt.xlabel('Number of rectangles (log scale)')
plt.ylabel('Error (log scale)')
plt.legend(['Calculated error'])
plt.show()


