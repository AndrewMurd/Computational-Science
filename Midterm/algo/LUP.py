# By L. van Veen, UOIT 2019.
# PLU decomposition (with pivoting)
# Input: n X n matrix A
# Output: n X n matrices L and U such that LU=PA and L and U are triangular
import math
import scipy
from copy import copy
import numpy as np
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")
    print()

# Note: indices i,j and k are used as matrix indeces (starting from 1) while s is used as python array index (starting from 0).
def LUP(A):
    small = 1e-12                                 # a pivot smaller than this will raise the error flag "ok=0"
    n = scipy.shape(A)[0]                         # extract matrix size
    U = copy(A)                                   # copy content of A (avoid linking U and A)
    L = scipy.identity(n)                         # initialize L and P
    P = scipy.identity(n)
    par = 1                                       # initial permutation (identity) is even
    ok = 1                                        # by default, we assume the matrix is non-singular
    counter = 1
    for k in range(1,n):
        s = scipy.argmax(abs(U[k-1:n,k-1]))+k-1   # find pivot element
        if abs(U[s,k-1]) < small:                 # check if pivot is too close to zero
            print("(nearly) singular matrix, pivot smaller than %e" % small)
            ok = 0
            break                                 # matrix is too close to singular, exit with error flag up
        if s != k-1:                              # if the pivot is not on the diagonal...
            par = -par                            # change parity
            U = swap(U,s,k-1,n)                   # swap rows of U
            if k>1:                               # swap rows of L left of diagonal element
                L = swap(L,s,k-1,k-1)
            P = swap(P,s,k-1,n)                   # swap rows of P
        for j in range(k+1,n+1):                  # Gauss elimination of rows below pivot
            L[j-1,k-1] = U[j-1,k-1]/U[k-1,k-1]
            for i in range(k,n+1):
                U[j-1,i-1]=U[j-1,i-1] - L[j-1,k-1]*U[k-1,i-1]
            print('iteration# = ',counter)
            print('L=')
            matprint(L)
            print('U =')
            matprint(U)
            print('P =')
            matprint(P)
            counter +=1
    return L,U,P,par,ok

def swap(M,i,j,k):
# Swap rows i and j from column 0 up to (but not including) k.
# Indices in this function are used as python array indices (starting from 0).
    dum = copy(M[i,0:k])
    M[i,0:k] = copy(M[j,0:k])
    M[j,0:k] = copy(dum)
    return M

def ForwardSub(L,P,y):
    # Solve the triangular system L z = P y, where L is lower triangular and has diagonal elements equal to 1 and P a permutation matrix.
    n = scipy.shape(L)[0]
    z = scipy.zeros((n,1))
    y = scipy.dot(P,y)
    for i in range(1,n+1):
        z[i-1] = y[i-1]
        for j in range(1,i):
            z[i-1] -= L[i-1,j-1] * z[j-1]
        z[i-1] /= L[i-1,i-1]
    return z

def BackwardSub(U,z):
    # Solve the triangular system U x = z, where L is lower triangular and has diagonal elements equal to 1.
    n = scipy.shape(U)[0]
    x = scipy.zeros((n,1))
    for i in range(n,0,-1):
        x[i-1] = z[i-1]
        for j in range(i+1,n+1):
            x[i-1] -= U[i-1,j-1] * x[j-1]
        x[i-1] /= U[i-1,i-1]
    return x


a = np.matrix([1 -3, 1], 
              [-2,1.5, 3],
              [2.5, 6, 1.5])

LUP(a)


