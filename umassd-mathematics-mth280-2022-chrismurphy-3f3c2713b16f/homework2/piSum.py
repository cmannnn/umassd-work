# date: 03/04/2022
# by: Chris Murphy

# Write a program that prints SN and N for N = 0, 1, 2, 3, 4, . . . , 20. Using your code, demonstrate that
# SN approaches π. In a code comment, answer the following question: What is the smallest value of N such that SN
# matches the first 5 digits of π: 3.14159

import math as m
import cmath as cm

n = range(21)

running_total = []
running_error = []
total = 0
for a in n:
	if a % 2 == 1:
		s = (m.sqrt(12) * (-1/3 ** a)) / (2 * a + 1)
		total += s
		running_total.append(total)
		error = abs(total - m.pi) / m.pi
		running_error.append(error)
	else:
		s = (m.sqrt(12) * (1/3 ** a)) / (2 * a + 1)
		total += s
		running_total.append(total)
		error = abs(float(total) - float(m.pi)) / m.pi
		running_error.append(error)

print('Sn 0-20:')
for b in range(len(running_total)):
	print(running_total[b])

print(' ')

print('Error 0-20:')
for c in range(len(running_error)):
	print(running_error[c])

# what is the smallest value of N such that Sn matches the first 5 digits of pi?
# 8 is the smallest value of N that SN matches 3.14159.

