# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:08:20 2020

@author: AndreForbes
"""

def spline(x,y):
    a = []
    b = []
    for i in range(x.length()):
        a.append(y[i])
        appendToB = (y[i+1] - a[i])/(x[i+1] - x[i])
        b.append(appendToB)
    return a,b

x = [] ## x values
y = [] ## y values

newA, newB = spline(x,y)
        