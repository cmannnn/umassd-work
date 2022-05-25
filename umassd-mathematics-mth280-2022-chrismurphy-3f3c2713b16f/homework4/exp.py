# 04/14/2022
# author: Chris Murphy
# MTH 280 homework 4

# imports
import math as m
import matplotlib.pyplot as plt
import numpy as np

# creating the exp_sums
def exp_sums(x, N):
	""" Creating an exponential function then plotting the absolute and relative error against the actual using np.exp()
	Inputs: x = the exponential value being calculated
	N = the number of numbers used as input
	Output: semilog graph of absolute/relative errors of exponential approximation"""

	# setting exp_sum as the value sum that will be updated
	exp_sum = 0.0

	# calculating the actual exp_sum that will be used to calculate errors
	exp_sum_actual = np.exp(x)
	
	# empty list to store x_values used in graph based on input N
	x_val = []

	# empty list to store the calculated absolute error values
	y_absol_error = []

	# empty list to store the calculated relative error values
	y_rel_error = []

	# main for loop to calculate actual/approximation exponential values for N
	for i in range(N + 1):
		fac = m.factorial(i)
		next_term = (x ** i) / fac
		exp_sum += next_term
		
		# calculating the absolute/relative errors using the actual and approx numbers calculated above
		absol_error = abs(exp_sum_actual - exp_sum) 
		rel_error = abs((exp_sum_actual - exp_sum) / exp_sum_actual)

		# appending everything to the above created lists
		x_val.append(i)
		y_absol_error.append(absol_error)
		y_rel_error.append(rel_error)

	# optional printing values
	# print(f'y_absol_error: {y_absol_error}')
	# print(f'y_rel_error: {y_rel_error}')

	# plotting the graph on a semilogy 
	plt.semilogy(x_val, y_absol_error, 'b')
	plt.semilogy(x_val, y_rel_error, 'r')
	plt.xlabel('N')
	plt.legend(['Absolute error', 'Relative error'])
	plt.show()

exp_sums(1, 20)
# exp_sums(20, 100)
# exp_sums(100, 200)
# exp_sums(-5, 50)
# exp_sums(-10, 60)
# exp_sums(-20, 100)


# Do the errors saturate?
# (that is, do you notice a limit to how small the errors can be made)? Why or why not? Is the absolute error
# ever misleadingly large or small? Do overflow or underflow errors become problematic (and if so when)? Is the
# series evaluated at x = 20 or x = −20 a better numerical approximation to the exponential function? Explain
# your reasoning. Your answers should always rely on properties of floating-point numbers. Add your answer to
# part c as a code comment.

# Yes, the errors do saturate. This can be experimented on by keeping x = 1 and increasing N. The pair of values with the 
# smallest difference in errors is when x = 1 and N = 1000 
# when the relative error is 1.6337129034990842e-16. When N is > 1000 the errors have been minimized to the greatest 
# extent and increasing N will cause no further decrease in the difference of errors. The absolute error for x = 100, N = 200 is 
# misleadingly large with the first few values hover around 2.6881171418161356e+43. The last 9 values however, completely drop off to 0. 
# Overflow/underflow errors will 
# happen if you continue to increase N. The series at x = 20 is a better numerical approximation of floating-point numbers. 
# The min relative error when x = 20 is 2.457086589859197e-16. 
# When x = -20 the min relative error is 0.7342215128027164.  
































