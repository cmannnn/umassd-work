# 03/17/2022
# author: Chris Murphy
# MTH 280 homework 3

# imports
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# setting constants, population, people infected at day zero, and people recovered at day zero
# susceptible people is the remaining people
population = 300000000
infected_zero, recovered_zero = 100000, 0
susceptible_zero = population - infected_zero - recovered_zero

# setting the contact rate (R0) and recovery rate (20 days)
contact_rate, recovery_rate = 1.7, 1./20

# creating numbers to be used as days
array = np.linspace(0, 80, 80)

# defining the derivative function for scipy odeint
def derivative(y, t, population, contact_rate, recovery_rate):
	S, I, R = y
	# S derivative function
	dSdt = -contact_rate * S * I / population
	# I derivative function
	dIdt = contact_rate * S * I / population - recovery_rate * I
	# R derivative function
	dRdt = recovery_rate * I
	# return the 3 derivatives
	return dSdt, dIdt, dRdt

# initializing the zero day
y0 = susceptible_zero, infected_zero, recovered_zero

# calling scipy odeint
integrate = odeint(derivative, y0, array, args = (population, contact_rate, recovery_rate))

# S, I, R numbers in ndarray
S, I, R = integrate.T

# printing the rounded max number of people infected in I ndarray
print(f'The maximum number of people infected is: {round(max(I))}')

# plotting ndarray values, setting figsize
fig = plt.figure(figsize = (12, 7))
# adding subplot to figure
ax = fig.add_subplot(111, axisbelow = True)
# dividing data by 1000 to get y axis to population and plotting  
ax.plot(array, S/1000, 'b', label = 'Susceptible')
ax.plot(array, I/1000, 'r', label = 'Infected')
ax.plot(array, R/1000, 'g', label = 'Recovered')
# setting title
ax.set_title('R0 = 1.7')
# setting x and y labels
ax.set_xlabel('Days since 03/29/2020')
ax.set_ylabel('Population')
# setting x any y limit
ax.set_xlim(0)
ax.set_ylim(0)
# setting legend to best placement
ax.legend(loc = 'best')
# getting graph grid lines
ax.grid(visible = True)
# showing graph
plt.show()