"""
Andrew Murdoch
100707816

This program calculates the least squares regression line for a set of discrete data points x,y.
"""

from scipy.linalg import solve
import numpy as np
import matplotlib.pyplot as plt

x = [-2, 0.25, 0.9, 1]          #Setting x,y values
y = [2.23, 4.29, 5.12, 6.3]
xy = np.multiply(x,y)           #Mutiplying xy vector
x2 = np.multiply(x,x)           #Squaring x^2 vector

n = len(x)
sum_x = sum(x)      #Calculating all sums needed for equations
sum_y = sum(y)
sum_xy = sum(xy)
sum_x2 = sum(x2)

A = [[n, sum_x],        #Building A matrix used used to solve Ax = b
     [sum_x, sum_x2]]

b = [sum_y, sum_xy]     #Building b in Ax = b

solution = solve(A, b)  #Solve for solution

c = round(solution[0],4)
m = round(solution[1],4)

print("Slope =", str(m))        #Output slop and y-intercept
print("Y-intercept =", str(c))

y_calculated = []
least_square_error = 0
for i in range(len(x)):
    y_calc = c + m*x[i]             #Caclulating the y value according to linear regression equation
    y_calculated.append(y_calc)     #Append y value to vector
    error = y[i] - y_calc           #Calculating error between y value and calculated y value
    least_square_error += error**2  #Square all errors for correct least squares error
    
print("Least Squares error = ", str(least_square_error))

plt.plot(x,y,'*')                   #Discrete data points 
plt.plot(x,y_calculated)            #Calculated points
plt.show()
