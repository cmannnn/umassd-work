# 03/13/2022
# author: Chris Murphy
# MTH 322 280 midterm exam practice
# Write a program to generate n equally spaced numbers in the interval [a, b]

# creating function
def points(a, b, n):
	# special case, when n = 2 variables "forget about" n
	if n == 2:
		print(f"{a}, {b}")
		return 
	# special case #2, when n = 3
	if n == 3:
		n = (b - a) / (n - 1)
		print(f"{a}, {n}, {b}")
		return

	# when the difference between a and b is negative!
	if a - b < 0:
		# changing to float to match other numbers type
		print(float(a))
		diff = 0
		# getting the correct amount of non start/end numbers
		for t in range(n - 1):
			diff += (b - a) / (n)
			# have to subtract diff by 1 for negative #'s
			print(diff - 1)
		print(float(b))

	# other catch all case
	else:
		# changing to float to match other numbers type
		print(float(a))
		diff = 0
		# getting the correct amount of non start/end numbers
		for t in range(n - 1):
			diff += (b - a) / (n)
			print(diff)
		print(float(b))

points(1, 10, 6)