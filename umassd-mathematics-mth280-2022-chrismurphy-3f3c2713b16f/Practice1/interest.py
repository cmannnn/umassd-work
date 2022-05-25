# 03/13/2022
# author: Chris Murphy
# MTH 322 280 midterm exam practice

# 1. Write a program which displays how much money 1000 dollars at a 5% return rate has
# grown to after 0,1,2,3,..., 100 years. You should use a loop. The output should be formatted as
# Year = X, dollars = Y
# where X is the year and Y is the current investment amount in year X. For example, there should be 101 total
# output lines, and the first line your program should output will be
# Year = 0, dollars = 1000

# A = initial investment
# p = stocks return rate
# n = years

A = 1000
p = .05
n = 0

while n < 101:
	
	# return rate calculation
	return_rate = A * (1 + (p / 100)) ** n
	
	# print formatting
	print("Year = %.0f, dollars = %.2f" % (n, return_rate)) 
	
	# base case
	n = n + 1

