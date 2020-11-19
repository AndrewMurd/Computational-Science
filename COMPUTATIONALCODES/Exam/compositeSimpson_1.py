# Composite Simpson's method. By L. van Veen, Ontario Tech U, 2020.
import math
import scipy
from scipy import integrate

def f(x):
    return math.cos(1 + x**2)          

def compositeSimpson(f,a,b,M):
    x = scipy.linspace(a,b,M+1)           
    h = (b-a)/float(M)                  
    I = 0.0 
    
    for i in range(1,M+1):
        I += (h/6.0) * (f(x[i-1]) + 4 * f((x[i-1] + x[i])/2.0) + f(x[i]))   
    return I


actual = scipy.integrate.quad(lambda x:x*math.exp(-x**2),0,3) 

M = 1
err = 0
while(True):
    errPrev = err
    I = compositeSimpson(f,-1,1,M)   
    err = abs(I-actual[0])
    if errPrev == err:
        break         
    if err > 10**-12:             
        M = M + 1
    else:
        break
    print("M: %d err: %e" %(M,err))
    
print('aprox: ',I)
print('actual: ',actual)
