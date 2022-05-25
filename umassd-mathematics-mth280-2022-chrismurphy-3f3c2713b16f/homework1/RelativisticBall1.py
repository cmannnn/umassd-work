# write a python program that computes the distance a ball has fallen according to Newton's second law of 
# motion and Einstein's theory of special relativity
# my code's output was yN(t) = 1.23e+02 meters, yE(t) = 1.23e+02 meters, and their difference was 2.70e-13 meters
# author: Chris Murphy
# 02/16/2022

import math as m
import cmath as cm

# y = distance ball has fallen
# t = time in seconds
# g = gravity of earth

c = 299792458
t = 5.0
g = 9.81 

# calculation w/ Newton's second law of motion
newton = (1/2) * g * (t ** 2)
print('yN(t) = %.2e' % newton)

# calculation w/ Einstein's theory of special relativity
einstein = 2 * (c ** 2 / g) * abs((cm.sin((1 / 2) * (g / c) * t) ** 2))
print('yE(t) = %.2e' % einstein)

# difference calculation
diff = abs(newton - einstein)
print('E(t) = %.2e' % diff)