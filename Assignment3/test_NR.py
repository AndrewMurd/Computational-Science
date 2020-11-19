"""
Andrew Murdoch
100707816

This program defines f(x) equations and its Jacobian (DF(x)). 
It calls Newton-Raphson Iteration to calculate solution.
"""

import numpy as np
from NR import NR


def f(x):                                                   
    y = np.zeros((3,1))                                      #Set empty array to store equations
    y[0] = (-1.0)*(x[1]**2.)-(x[2]**2.)-(1./4.*x[0])+2.      #Equation 1..3
    y[1] = (x[0]*x[1])-(4.*x[0]*x[2])-x[1]+1.
    y[2] = (4.*x[0]*x[1])+(x[0]*x[2]) - x[2]
    return y

def DF(x):                                                   
    J = np.zeros((3,3))                                      
    J[0,0] = -1./4.           #Creating Jacobian matrix with three equations
    J[0,1] = -2.*x[1]
    J[0,2] = -2.*x[2]
    J[1,0] = x[1]-4.*x[2]
    J[1,1] = x[0]-1.
    J[1,2] = -4.*x[0]
    J[2,0] = 4.*x[1]+x[2]
    J[2,1] = 4.*x[0]
    J[2,2] = x[0]-1
    return J

x0 = np.array([[7.0],[0.0],[0.0]])      #Initial guess

x, err, res = NR(x0, f, DF, 1e-5, 1e-5, 15)     



