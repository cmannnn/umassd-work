# 03/15/2022
# author: Chris Murphy
# MTH 322 280 midterm exam

# BONUS QUESTION

import numpy as np
from math import floor

# defining function to calculate the int coordinates (NOT ON BOUNDARY)
def total(radius):
	# rounding radius down to whole num
    r0 = floor(radius)
    # setting up coordinates with numpy arrange
    ys = np.arange(1, r0 + 1)
    # calculating the radius and discluding the boundary num
    halves = 2 * np.sum(2 * np.floor(np.sqrt(radius * radius - ys * ys)))
    # returning the num of coordinates for fixed y coordinate
    return halves + 1 + 2 * r0

# i. the num of points in Ir for radius = 1 -> 100
for t in range(1, 101):
	print(int(total(t)))

# ii. the ratio of number of points in Ir / r^2
for p in range(1, 101):
	ratio = int(total(p)) / (p) **  2
	print(ratio)
