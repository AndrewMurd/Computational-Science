"""
ITERATIVE METHODS
"""

import math

def newtons(f,f1,x,eps,n):                             #newtons method 
    y1=x-(f(x)/f1(x))
    err=abs(f(x))
    res=abs(x-y1)
    print("\nCurrent Approximation: "+str(y1))
    print("Error: "+str(err))
    print("Residual: "+str(res)) 
    if n > 0:
        if err < eps and res < eps:
            print("Converged")
    
        else:
            y1,err,res=newtons(f,f1,y1,eps,n-1)
    
    return y1,err,res

def f(x):                                               #your function goes here
    return x*math.sin(x)

def fp(x):                                              #your derivative function goes here
    return math.sin(x) + (x*math.cos(x))

x = 1                                                   #your initial x value goes here

eps = 10e-11                                            #your error bound goes here

n = 50                                                  #your max number of iterations goes here

print(newtons(f,fp,x,eps,n))                            #displays the newtons function                                               