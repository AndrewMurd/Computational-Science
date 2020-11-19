#Author: Lennaert van Veen
#Date: 1/17/2017
# Python function for bisection using recursion.
import math

def func(x):
    return (math.exp(-x)-x**2)

def bisection(l, r, kMax, epsX, epsF):
# Input: initial left and right boundary, max nr. of iterations, tolerance for error and residual
    m = (l+r)/2                # Compute midpoint
    err = abs(r-l)/2           # Compute current error
    fm = func(m)               # Compute function value at mid point
    res = abs(fm)              # Compute current residual
    x=m                        # Set surrent approximation
    print("x="+str(x)+"  l="+str(l)+"  r="+str(r)+"  err="+str(err)+"  res="+str(res))
    if (kMax > 0):             # If number of iterations is not exceeded...
        if err > epsX or res > epsF:       # If not converged yet...
            fl = func(l)       # Compute function value at left boundary
            if (fm*fl > 0):
                l = m          # Discard left half
            else:
                r = m          # Discard right half
            x,err,res = bisection(l, r, kMax-1, epsX, epsF) # Recursive call
    else:
        print("Warning: maximal number of iterations exceeded...")

    return x,err,res

bisection(0, 1, 15, 0.05, 0.05)
