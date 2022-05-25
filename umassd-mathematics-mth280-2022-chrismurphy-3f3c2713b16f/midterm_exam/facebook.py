# 03/15/2022
# author: Chris Murphy
# MTH 322 280 midterm exam

import math

# getting year 2004 -> 2050
year = range(2004, 2051)

# looping over year
for t in year:
	# users fn
	users = 1400000000 / (1 + math.exp((2009.975 - t) / 0.85))
	print('year = %.0f, Facebook users = %.1e' % (t, users))