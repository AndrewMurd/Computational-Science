"""
POLYNOMIAL INTERPOLATION
"""

import numpy as np
import matplotlib.pyplot as plt

def vandermondeMatrix(x,y):                         #function that creates Vandermonde Matrix
    n=np.shape(x)[0]                                #creates n value based on size of set
    P=np.zeros((n,n))                               #creates empty Matrix to input Vandermonde Matrix
    for i in range(n):              
        for j in range(n):
            P[i,j] = x[i]**j                          #inputs value into empty Matrix based on Vandermonde Matrix
    return P

def solveInterpolation(P,y):                        #function that solves Interpolation
    return np.linalg.solve(P,y)

def Pa(x,a):                                        #function for interpolation line
    return (a[0])+(a[1]*x)+(a[2]*x**2)+(a[3]*x**3)    

x = np.array([np.linspace(0,2,5)])                    #x value array
y = np.array([np.linspace(0,2,5)])                    #y value array

P = vandermondeMatrix(x,y)                          #creates vandermonde matrix
a = solveInterpolation(P,y)                         #creates interpolant a array


plt.plot(x,y,'o')                                   #plots x,y arrays
X = np.linspace(-4, 4, 50, endpoint=True)           #creates linespace
plt.plot(X,Pa(X,a))                                 #plots interpolation based off linespace
print(a)
plt.grid(b=True, which='both', color='0.65', linestyle='-')     #creates grid
plt.show()                  

