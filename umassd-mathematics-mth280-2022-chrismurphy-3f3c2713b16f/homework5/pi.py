# 04/26/2022
# author: Chris Murphy
# MTH 280 homework 5
# BONUS QUESTION

import numpy as np
import matplotlib.pyplot as plt
import math as m

n = 5
xi_ = [] 
yi_ = []
for i in range(n):
	xi = 0.5 * m.cos(2 * np.pi * i / n)
	yi = 0.5 * m.sin(2 * np.pi * i / n)
	# print(xi)
	# print(yi)
	# print(' ')
	xi_.append(xi)
	yi_.append(yi)

# ------------	
# 	plt.plot(xi_, yi_, 'bo')
# plt.xlim([-0.5, 0.5])
# plt.ylim([-0.5, 0.5])
# # plt.title('N = 50')
# plt.show()
# ------------

# print(xi_)
# print(yi_)

xi_yi_zipped = [(xi_, yi_) for xi_, yi_ in zip(xi_, yi_)]

print(xi_yi_zipped)
print(' ')
diff_list = []
for x, y in xi_yi_zipped:
	print(x)
	print(y)
	diff = m.dist([x], [y])
	diff_list.append(diff)

# print(' ')
# print(diff_list)
diff_list_sum = sum(diff_list)
print(' ')
print(diff_list_sum)



# Write a Python program to compute π according to Archimedes’ method. Now run your code for a
# polygon with N = 50, 500, 5000, 50000 points and record the estimated value for π as a code comment. Provide
# evidence that an N-sided polygon’s perimeter will converge to π as N → ∞. Finally, make a plot showing the set of
# points (depicted as blue circles) for N = 50 and save it as points.png (from part b; see below). Save your code as
# code as pi.py. Upload your code and the figure to bitbucket.



