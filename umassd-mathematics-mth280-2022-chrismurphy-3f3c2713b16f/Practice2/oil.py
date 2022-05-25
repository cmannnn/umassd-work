# 03/14/2022
# author: Chris Murphy
# MTH 322 280 midterm exam practice

# Congratulations! You’ve discovered a formula to predict the price of oil, P, on each day, D. 
# Write a program to (i) print the price P on days D = 1, 2, 3, (ii) find the maximum price over the next year,
# and (iii) find the day on which this maximum price occurs. That is, for these second and third parts use
# D = 1, 2, 3, . . . , 365 (these are the days over the next year).

import math

# d = day
# p = price of oil

price = []
day = list(range(1, 366))
d = 1
while d < 366:
	p = 3 + math.sin(d) * math.sin(2 * d) + math.exp(d / 1000)
	price.append(p)
	d = d + 1



price_day = dict(zip(day, price))
max_value = max(price_day.values())
max_keys = [k for k, v in price_day.items() if v == max_value]
max_keys = int(max_keys[0])
max_value = float(max_value)

h = 0
c = 1
while c < 4:
	x = 3 + math.sin(c) * math.sin(2 * c) + math.exp(c / 1000)
	print('The price of oil on day %.0f is %.02f' % (c, x))
	c = c + 1
print('The maximum price of oil is %.02f on day %.0f' % (max_value, max_keys))






