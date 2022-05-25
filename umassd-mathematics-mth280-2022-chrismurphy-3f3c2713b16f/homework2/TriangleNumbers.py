# date: 03/04/2022
# by: Chris Murphy

# Write a program which prints the first 11 square triangle numbers. If we let Ni be the i
# the square triangle
# number, then your code is going to find N1, N2, ..., N11 (we already know N1 = 1, N2 = 36).

# imports
import math as m

# setting num to a very large number
num = range(15000000)

# initializing square total variable/list, triangle total/num, 
# and a final square triangle list
square_total = 0
square_num = []
triangle_total = 0
triangle_num = []
square_triangle = []

# first for loop to find triangle numbers and square numbers, 
# and appending to respective lists
for a in num:
	triangle_total += a
	triangle_num.append(triangle_total)
	square_total = a ** 2
	square_num.append(square_total)

# taking the intersection of the triangle and square numbers and 
# inserting into square triangle list
square_triangle = sorted(set(triangle_num).intersection(square_num))

# printing first 11 square triangle numbers
print('The first 11 square triangle numbers are:')
print(square_triangle)

# calculating the N of i using list comprehension
Ni = [((square_triangle[b] + square_triangle[b + 1]) / square_triangle[b]) - 1 for b in range(1, len(square_triangle) - 1)]

# printing N of i
print(' ')
print('Ni + 1 / Ni values for the square triangle numbers:')
print(Ni)

# printing right side of the error calculation
RH = (1 + m.sqrt(2)) ** 4
print(' ')
print('The numerical value of (1 + m.sqrt(2)) ** 4 is:')
print(RH)

# initializing separate error list, doing error calculation, and inserting into the list
print(' ')
error_list = []
for c in Ni:
	error = abs(c - RH) 
	error_list.append(error)

# printing the square triangle numbers error based on the formula
print('The error for the square triangle numbers is: ')
print(error_list)





