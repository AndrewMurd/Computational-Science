# Name: Andrew Murdoch
# Student ID: 100707816

# Do not change the name of the variables already given in the template.
# You can implement the method as you want as long as you keep the specified variables the same.
# You are allowed to change the function definition as long as the given variable names are not changed.
# Save your function as solve.py

import scipy
from numpy import linalg as LA

def solve(A,eps):
    lam = 0.0
    n = len(A)
    v = []
    for i in range(0, n):
        v.append(1.0)
    
    while True:
        w = A * v
        alpha = LA.norm(w, 2)/LA.norm(v, 2)
        if abs(alpha - lam) < eps:
            return v, lam
        else:
            v = w/LA.norm(w, 2)
            lam = alpha
    return v,lam


