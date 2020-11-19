# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:13:03 2020

@author: AndreForbes
"""
import scipy as sp


def f(x):
    return sp.exp(1 + x**2)

a = -1
b = 1
M = 2
h = (b-a)/M

loopVals = f(a)/2



for i in range(1,M):
    loopVals += f(a + i*h)
    
loopVals += f(b)/2
fAndLoop = loopVals 

iCT = h*fAndLoop

print("iCT: " + str(iCT))

