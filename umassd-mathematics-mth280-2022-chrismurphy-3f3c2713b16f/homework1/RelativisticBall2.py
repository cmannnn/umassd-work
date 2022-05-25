# write a program which outputs the values yE(t), yN(t), and E(t) every 0.5 seconds until the ball hits the ground
# find the max discrepancy between Einstein and Newton prediction as a comment in the source code (largest value of E(t))
# find object of comparable length (to Burj Khalifa) and speculate on the possibility of performing this experiment

# ANSWERS:

# Newton's 2nd Law:
# yN(0.50) = 1.23e+00
# yN(1.00) = 4.91e+00
# yN(1.50) = 1.10e+01
# yN(2.00) = 1.96e+01
# yN(2.50) = 3.07e+01
# yN(3.00) = 4.41e+01
# yN(3.50) = 6.01e+01
# yN(4.00) = 7.85e+01
# yN(4.50) = 9.93e+01
# yN(5.00) = 1.23e+02
# yN(5.50) = 1.48e+02
# yN(6.00) = 1.77e+02
# yN(6.50) = 2.07e+02
# yN(7.00) = 2.40e+02
# yN(7.50) = 2.76e+02
# yN(8.00) = 3.14e+02
# yN(8.50) = 3.54e+02
# yN(9.00) = 3.97e+02
# yN(9.50) = 4.43e+02
# yN(10.00) = 4.90e+02
# yN(10.50) = 5.41e+02
# yN(11.00) = 5.94e+02
# yN(11.50) = 6.49e+02
# yN(12.00) = 7.06e+02
# yN(12.50) = 7.66e+02
# yN(13.00) = 8.29e+02

# Einstein's Theory of Relativity
# yE(0.00) = 0.00e+00
# yE(0.50) = 1.23e+00
# yE(1.00) = 4.91e+00
# yE(1.50) = 1.10e+01
# yE(2.00) = 1.96e+01
# yE(2.50) = 3.07e+01
# yE(3.00) = 4.41e+01
# yE(3.50) = 6.01e+01
# yE(4.00) = 7.85e+01
# yE(4.50) = 9.93e+01
# yE(5.00) = 1.23e+02
# yE(5.50) = 1.48e+02
# yE(6.00) = 1.77e+02
# yE(6.50) = 2.07e+02
# yE(7.00) = 2.40e+02
# yE(7.50) = 2.76e+02
# yE(8.00) = 3.14e+02
# yE(8.50) = 3.54e+02
# yE(9.00) = 3.97e+02
# yE(9.50) = 4.43e+02
# yE(10.00) = 4.90e+02
# yE(10.50) = 5.41e+02
# yE(11.00) = 5.94e+02
# yE(11.50) = 6.49e+02
# yE(12.00) = 7.06e+02
# yE(12.50) = 7.66e+02
# yE(13.00) = 8.29e+02

# Difference
# E(t) = 0.00e+00
# E(t) = 2.22e-16
# E(t) = 8.88e-16
# E(t) = 1.78e-15
# E(t) = 3.55e-15
# E(t) = 2.13e-14
# E(t) = 2.84e-14
# E(t) = 5.68e-14
# E(t) = 1.14e-13
# E(t) = 1.71e-13
# E(t) = 2.70e-13
# E(t) = 3.41e-13
# E(t) = 5.40e-13
# E(t) = 7.39e-13
# E(t) = 9.66e-13
# E(t) = 1.36e-12
# E(t) = 1.71e-12
# E(t) = 2.27e-12
# E(t) = 2.84e-12
# E(t) = 3.64e-12
# E(t) = 4.43e-12
# E(t) = 5.12e-12
# E(t) = 6.37e-12
# E(t) = 7.62e-12
# E(t) = 8.98e-12
# E(t) = 1.06e-11
# E(t) = 1.26e-11

# Object of comparable length
# My max difference calculation was evaluated in scientific terms at 1.26e-11. 
# In non-scientific terms this equals 0.0126 nanometers. To put this number into perspective, 
# a piece of paper is 100,000 nanometers thick and a strand of DNA is 2.5 nanometers thick. 
# The difference I calculated between the two equations is ~198 times smaller than a single strand of DNA.
# It would be incredibly difficult to conducting an experiment on data this small.


# author: Chris Murphy
# date: 02/16/2022

import math as m
import cmath as cm

c = 299792458
g = 9.81 
h = 829.8

t = 0
newton = (1/2) * g * (t ** 2)
while newton < h:
	print('yN(%.2f) = %.2e' % (t, newton))
	#print(t)
	t = t + 0.5 
	newton = (1/2) * g * (t ** 2)

t = 0
einstein = 2 * (c ** 2 / g) * abs((cm.sin((1 / 2) * (g / c) * t) ** 2))
while einstein < h:
	print('yE(%.2f) = %.2e' % (t, einstein))
	t = t + 0.5
	einstein = 2 * (c ** 2 / g) * abs((cm.sin((1 / 2) * (g / c) * t) ** 2))

t = 0
newton = (1/2) * g * (t ** 2)
einstein = 2 * (c ** 2 / g) * abs((cm.sin((1 / 2) * (g / c) * t) ** 2))
while newton < h and einstein < h:
	diff = abs(newton - einstein)
	print('E(t) = %.2e' % diff)
	t = t + 0.5
	newton = (1/2) * g * (t ** 2)
	einstein = 2 * (c ** 2 / g) * abs((cm.sin((1 / 2) * (g / c) * t) ** 2))


