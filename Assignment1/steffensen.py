'''
 Andrew Murdoch 
 100707816

 This program implements Steffensen's iteration algorithm. It also compares this algorithm to the newton iteration algorithm. 
 Newton algo does not converge quadratically while Steffensen's does (faster). You can see that Steffensen's iteration converges 
 with half the amount of iterations as Newton's iteration.
'''

import math

def steffensen(f, f1, x, eps, n):
    p = 0

    for i in range(1, n + 1):
        y1 = x                      
        y2 = y1 - f(y1)/f1(y1)                      # First Newton step 
        y3 = y2 - f(y2)/f1(y2)                      # Second Newton step
        x = y1 - (((y2 - y1)**2)/(y3 - 2*y2 + y1))  # Calculate new aproximation 

        err = abs(f(x))     # Error 
        res = abs(x - y1)   # Residual
        print("Iteration", i, " x =", x, " Error =", err, " Residual =", res) # Print each iteration

        if err < eps and res < eps:   # Check if algorithm has converged
            print("Converged!")
            p = 1
            break
    if p == 0:                        # Check if maximum number of iterations was acheived
        print("Maximum number of iterations reached!") 

    return x, err, res


def newtons(f, f1, x, eps, n):
    p = 0

    for i in range(1, n + 1):
        y1 = x - f(x)/f1(x) # Calculate Newton's iteration
        err = abs(f(x))     # Error
        res = abs(x - y1)   # Residual
        x = y1              # Set new x value
        print("Iteration", i, " x =", y1, " Error =", err, " Residual =", res) 

        if err < eps and res < eps:
            print("Converged!")
            p = 1
            break
    if p == 0:  
        print("Maximum number of iterations reached!") 
    
    return y1, err, res

def function1(x):                                # Function input
    return math.exp((-(x**2))+x) - x/2 - 1.0836

def functionPrime(x):                            # Prime function (derivative)
    return (1-(2*x))*math.exp((-x**2)+x)-0.5

# Print both methods
print("Steffensen's method: ")
x, err, res = steffensen(function1, functionPrime, 1, 1e-10, 30)
print("\nConverged too", x, "with error of +/-", err, "and residual of", res)

print("\nNewton's method: ")
x, err, res = newtons(function1, functionPrime, 1, 1e-10, 30)
print("\nConverged too", x, "with error of +/-", err, "and residual of", res)
    

