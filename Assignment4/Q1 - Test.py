"""
Created on Wed Mar 11 15:16:28 2020

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

def f(x):
    return np.log((x + 2)/(x + 1))

y = [0, 0, 0]
x = [1, 1.5, 2]

for i in range(3):
    y[i] = f(x[i])

f = interp.interp1d(x, y)
xnew = np.arange(1,2,0.01)

plt.plot(x,y,'*',xnew,f(xnew))
plt.title("Interpolant and Data Points")
plt.xlabel("x")
plt.ylabel("y")