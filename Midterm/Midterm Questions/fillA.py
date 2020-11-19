# Name: Andrew Murdoch
# Student ID: 100707816

# Do not change the name of the variables already given in the template.
# You can implement the method as you want as long as you keep the specified variables the same.
# You are allowed to change the function definition as long as the given variable names are not changed.
# Save your function as fillA.py

import numpy as np

def fillA(n):

    A = np.zeros((n,n))
    
    for i in range(0, n):
        for j in range(0, n):
            A[i, j] = 1/(1 + (i-j)**2)
            
    return A



