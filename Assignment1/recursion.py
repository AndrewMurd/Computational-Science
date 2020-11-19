'''
 Andrew Murdoch 
 100707816

 This program apoximates the root solution to the given equations recursively.
'''
import math

xk_old = 0
iterations = 1

def f(x): # function f
    l=math.sin(math.pi*x)-(x**2)
    return l
    
def g(x): #function g
    l=(1/(2*math.pi))*(math.sin(math.pi*x))-(1/(2*math.pi))*(x**2)+x
    return l

def compSequence(xO, itmax, tolx, toly):
    global xk_old
    global iterations           # Set global varibles for tracking
    xk = xO                     
    xk_old = xk                 # Set var for old aproximation
    xk = g(xk_old)              # Calculate new aproximation
    error = abs(xk - xk_old)
    residual = abs(f(xk))
    
    print("iteration: ", iterations," Approx solution: ", xk," Estimated Error: ", error, " Residual: ", residual)

    if (error < tolx and residual < toly) or itmax <= iterations:   # Check if algorithm has aproximated solution within given tolerance
        return xk

    iterations = iterations + 1
    compSequence(xk, itmax, tolx, toly) # Recusive call for loop

compSequence(2, 17, 0.0001, 0.0001)
