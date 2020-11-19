# Sample solution to MATH/CSCI 2072U A5Q2. By L. van Veen, Ontario Tech U, 2020.
import numpy as np
import matplotlib.pyplot as plt
from compositeSimpson import compositeSimpson

# Define test function and its antiderivative:
def f(x):
    return x * np.exp(-x**2)
def F(x):
    return - np.exp(-x**2)/2.0

# Evaluate the exact result:
exact = F(3.0) - F(0.0)

# Loop over increasing numbers of subintervals until the error is less than 10^{-12}:
M = 1
err = 1.0
while err > 1e-12:
    appr = compositeSimpson(f,0.0,3.0,M)
    err = abs(exact-appr)
    print("%d %e" % (M,err))
    M += 1
