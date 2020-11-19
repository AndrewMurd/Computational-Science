# Test code for triangular matrix-matrix multiplication. Midterm 2019, Q1d. Author: L. van Veen, UOIT, 2019.

import scipy
from triangular_prod import *

n = 20                                     # Fix n>1
A = scipy.zeros((n,n))                     # Create random triangular matrices
B = scipy.zeros((n,n))
for i in range(0,n):
    A[i,0:i+1] = scipy.random.rand(1,i+1)
    B[i,0:i+1] = scipy.random.rand(1,i+1)

C = triangular_prod(A,B)                   # Compute the product without function
C_check = scipy.dot(A,B)                   # Check versus in-built matrix-matrix multiplication

err = scipy.amax(C-C_check)
print('Maximal difference is %e\n' % (err))
