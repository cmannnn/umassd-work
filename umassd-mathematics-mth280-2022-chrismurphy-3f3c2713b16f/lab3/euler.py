# this program will numerically check Euler's equation
# author: Chris Murphy
# 02/08/2022

import math as m
import cmath as cm


theta = 0.0
while theta <= 6.0:
#for l in theta:
	LHS = m.e ** (1.0j * theta)
	RHS = cm.cos(theta) + (1.0j) * cm.sin(theta)
	difference = abs(LHS - RHS)
	print('theta = %.1f, |LHS - RHS| of euler\'s equation = %.1e' % (theta, difference))
	theta = theta + 0.5

