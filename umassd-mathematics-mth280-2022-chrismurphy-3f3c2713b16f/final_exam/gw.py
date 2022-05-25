# 05/05/2022
# author: Chris Murphy
# MTH 280 final exam

import matplotlib.pyplot as plt
import numpy as np

dataset = np.loadtxt('gravityWave.txt') 

time = dataset[:,0] 
signal = dataset[:,1]

xmax = time[np.argmax(signal)]
ymax = signal.max()

plt.plot(time, signal)
plt.plot(xmax, ymax, 'r*')
plt.xlabel('Time (seconds)')
plt.ylabel('Signal (no units)')
plt.title('Gravitational wave signal')
plt.show()