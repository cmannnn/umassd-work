import math as m
import time
import numpy as np

def time_list(N):
    """ time it takes to compute sin(x) at N points in list"""
    t = time.time()
    xs = range(N)
    y = []
    for x in xs:
        y.append(m.sin(x))
    elapsed = time.time() - t
    print("elapsed list %f" % (elapsed))

def time_numpy(N):
    """time it takes to compute sin(x) at N points in numpy array"""
    t = time.time()
    xs = np.arange(N)
    y = np.sin(xs)
    elapsed = time.time() - t
    print("elapsed numpy %f" % (elapsed))

time_list(1000000)
time_numpy(1000000)
time_list(10000000)
time_numpy(10000000)
time_list(100000000)
time_numpy(100000000)
