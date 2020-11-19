import scipy
import math
import matplotlib.pyplot as plt

def secant(F, x0, x1, tolf, tolx, kmax):
    x = f(x0)                                                
    conv = 0                                              
    for k in range(1,kmax):                               
        r = F(x1) 
        dx = -r*(x1-x0)/(r-x)                                                                              
        err = abs(dx)                                   
        res = abs(r)                                   
        print('it=%d x=%e err=%e res=%e' % (k,x,err,res)) 
        if err < tolx and res < tolf:                    
            conv = 1                                      
            break                                  
    if conv == 0: 
        print("Max number of iterations!")                                        

    return x, err ,res

secant(distance, bisectFunc(), bisectFunc(), 10e-6, 10e-6, 15)


def bisection(l, r, kMax, epsX, epsF):
# Input: initial left and right boundary, max nr. of iterations, tolerance for error and residual
    m = (l+r)/2                # Compute midpoint
    err = abs(r-l)/2           # Compute current error
    fm = func(m)               # Compute function value at mid point
    res = abs(fm)              # Compute current residual
    x=m                        # Set surrent approximation
    print("l="+str(l)+" r="+str(r))
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

r = 100
c = 0.001
g = 9.8
v0 = 40

def func(theta, c, g, v0, R):
    return distFunc(theta, c, g, v0) - r
