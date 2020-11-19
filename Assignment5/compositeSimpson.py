"""
#Andrew Murdoch
#100707816

This script implements the Composite Simpson function
"""

import math
import scipy as sp

def f(x):
    return x*math.exp(-x**2)            #Initialize function

def compositeSimpson(f,a,b,M):
    x = sp.linspace(a,b,M+1)            #Get m+1 x values between interval a to b
    h = (b-a)/float(M)                  #calculate h
    I = 0.0 
    
    for i in range(1,M+1):
        I += (h/6.0) * (f(x[i-1]) + 4 * f((x[i-1] + x[i])/2.0) + f(x[i]))   #aproximate answer 
    return I
