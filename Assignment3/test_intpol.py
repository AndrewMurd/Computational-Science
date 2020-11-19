"""
Andrew Murdoch
100707816

This script calculates the vandermonde matrix and the coefficients of a. 
The calculates the y values for each sample and plots the interpolant and data points
"""
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt

xi = np.array([-1.2, 0.5, 2.2, 3.1])         #Create x value array for Vandermonde matrix
V = np.vander(xi, increasing= True)          #Create Vandermonde matrix
yi = np.array([-0.4, 1.2, 5.5, 10.2])        #Create array of y values
M = np.linalg.solve(V, yi)                   #Solve system
    
print("Vandermonde Matrix =")                       
print(V)
print("\ncoeff(a) =")                              
print(M) 

x = numpy.linspace(-1.7,3.6,1000)            #1000 number samples from -1.7 to 3.6       
y = M[0] + M[1]*x + M[2]*x**2 + M[3]*x**3    #Calculate the value of y for each sample  

plt.plot(xi,yi,'*')                          #Plotting interpolant and data points
plt.plot(x,y,'-')                           	       
plt.title("Interpolant and Data Points")
plt.xlabel("x")
plt.ylabel("y")
plt.show()