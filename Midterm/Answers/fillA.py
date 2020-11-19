import numpy as np

def fillA(n):
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = 1.0/(1.0+(i-j)**2)
    return A
