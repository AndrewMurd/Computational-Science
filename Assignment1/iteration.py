'''
 Andrew Murdoch 
 100707816

 This program apoximates the root solution to the given equations iteratively.
'''

import math

def f(x): # function f
    l=math.sin(math.pi*x)-(x**2)
    return l
    
def g(x): #function g
    l=(1/(2*math.pi))*(math.sin(math.pi*x))-(1/(2*math.pi))*(x**2)+x
    return l

def compSequence(xO, itmax, tolx, toly):
    xk = xO

    for i in range(itmax):
        xk_old = xk                 # Set var for old aproximation
        xk = g(xk_old)              # Calculate new aproximation
        error = abs(xk - xk_old)    
        residual = abs(f(xk))
        print("iteration: ", i + 1," Approx solution: ", xk," Estimated Error: ", error, " Residual: ", residual) 

        if error < tolx and residual < toly:    # Check if algorithm has aproximated solution within given tolerance
            break
        
    return xk

compSequence(2, 17, 0.0001, 0.0001)

