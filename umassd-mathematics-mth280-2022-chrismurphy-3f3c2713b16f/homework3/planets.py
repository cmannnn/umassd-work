# 03/16/2022
# author: Chris Murphy
# MTH 280 homework 3

# must use Numpy array, no list should appear in solution!
# must use numpy's loadtxt function

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
plt.style.use('fivethirtyeight')
import math as m

# loading text with numpy into x and y
x, y = np.loadtxt('planetdata.txt', unpack = True)

# arranging the second set of 9 x values
num = np.arange(57909227, 5906440628, 10000000)

# setting Newton's constant
g = (6.7430 * (10 ** (-11))) 

# setting mass of the sun
sun = 2.0 * 10 ** (30)

# list comprehension using newton's law of gravity 
x2 = [((m.sqrt(g * sun) / p) * 1e3) for p in num]

# plotting
figure(num = 1, figsize = (18, 10), dpi = 80)
plt.xlabel('~ Distance to sun (km)')
plt.ylabel('~ Velocity (km/h)')
plt.title('Planet velocity: Newton calculation vs. NASA data')
plot1, = plt.plot(x, y, 'bo')
plot2, = plt.plot(num, x2, 'r')
plt.legend([plot1,plot2], ['Planetary Data', 'Newton/s equation'])
plt.show()

# OPTIONAL QUESTIONS:
# Which planet has the largest deviation (measured as a relative error) from this simple model
# and how large? What do you think causes this? You can provide your answer as a code comment.

deviation_set = np.array(x2[0::65])
deviation = [abs((deviation_set - y) / y) * 100]
print(deviation)
print('The largest deviation is: %.2f' % np.amax(deviation))
# The planet with the largest deviation (measured from relative error) is Mars. I think this is the case because at the 4th element is where the curve flattens
# and the model may not follow the curve accurately when this is taking place.  



