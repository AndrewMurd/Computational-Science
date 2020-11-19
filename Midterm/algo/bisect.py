#Author: Lennaert van Veen
#Date: 1/17/2017
# Python function for bisection using recursion.
import math

def bisect(l, r, kMax, epsX, epsF,func):
# Input: initial left and right boundary, max nr. of iterations, tolerance for error and residual
    m = (l+r)/2                # Compute midpoint
    err = abs(r-l)/2           # Compute current error
    fm = func(m)               # Compute function value at mid point
    res = abs(fm)              # Compute current residual
    x=m                        # Set surrent approximation
    print("l="+str(l)+" r="+str(r),"x="+str(x),"err: "+str(err),"res:"+str(res))
    if (kMax > 0):             # If number of iterations is not exceeded...
        if err > epsX or res > epsF:       # If not converged yet...
            fl = func(l)       # Compute function value at left boundary
            if (fm*fl > 0):
                l = m          # Discard left half
            else:
                r = m          # Discard right half
            x,err,res = bisect(l, r, kMax-1, epsX, epsF,func) # Recursive call
    else:
        print("Warning: maximal number of iterations exceeded...")

    return x,err,res
