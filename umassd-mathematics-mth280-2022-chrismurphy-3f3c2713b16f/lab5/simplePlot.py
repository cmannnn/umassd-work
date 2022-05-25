from math import sin as sine
import matplotlib.pyplot as plt

dx = .05 # distance between x values
xs = [] # list of x values
ys = [] # list of y values

# this loop evaluates sine(x) at many values of x
for i in range(0,301,1): # loop over list of integrs from 0 to 300
	x = i * dx # convert integers to "physical" x values
	xs.append(x)
	ys.append( sine(x) )

# inspect the contents of our lists
# print(xs)
# print(ys)

# setting x, y axis limiter
plt.xlim([-5, 15])
plt.ylim([-1.5, 1.5])

# setting x, y label
plt.xlabel('x values')
plt.ylabel('y values')

# setting graph title
plt.title('Chris_Murphy')

# setting graph legend
plt.legend(['sine(x)'])

# plotting and saving
plt.plot(xs, ys, 'ro')
plt.savefig('mySimplePlot.png', bbox = 'tight')