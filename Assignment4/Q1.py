# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:41:34 2020

@author: andre
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log((x + 2)/(x + 1))

xi = np.array([1, 1.5, 2])         
V = np.vander(xi, increasing= True)      
yi = np.zeros(3) 
for i in range(3):
    yi[i] = f(xi[i])   
M = np.linalg.solve(V, yi)  

print("Vandermonde Matrix =")                       
print(V)
print("\ncoeff(a) =")                              
print(M) 

x = np.linspace(1,2,3)                   
P = M[0] + M[1]*x + M[2]*x**2


plt.plot(xi,yi,'*')                          
plt.plot(x,P,'-')                           	       
plt.title("Interpolant and Data Points")
plt.xlabel("x")
plt.ylabel("y")
plt.show()