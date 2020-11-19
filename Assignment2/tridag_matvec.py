'''
Andrew Murdoch 
100707816

This function computes the matrix-vector product of A with a vector x where A is vectors a, b, and c.
'''

import numpy as np

def tridag(a, b, c, x):
    
    n = np.size(x)              #get size of array
    y = np.zeros((n,1))         #create solution array
    
    for i in range(0, n-2):
        y[i,0] = a[i]*x[i] + b[i]*x[i+1] + c[i]*x[i+2]  #calculate product of vectors up to n-2 
        
    y[n-2,0] = a[n-2]*x[n-2] + b[n-2]*x[n-1]            #calculate entry n-2
    y[n-1,0] = a[n-1]*x[n-1]                            #calculate entry n-1
    
    return y