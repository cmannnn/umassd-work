# 05/05/2022
# author: Chris Murphy
# MTH 280 final exam

import math as m
from scipy import integrate
import numpy as np

def sn(x):
	return 1 / (1 - x)
# print(sn(2))

x = [0.9, 0.99, 0.9995]
Sn = 0
error = 0
# number of terms
n_terms = 0
S = np.linspace(1, 10000)
In = 0


for p in x:
	while error <= 1.0e-10:
		In = sn(2)
		Sn += In
		error_calc = abs((In - S) / S)
		error += error_calc
		n_terms += 1
		print(f'x = {p}, n_terms = {n_terms}, Sn = {Sn}, error = {error}')

# ------------
