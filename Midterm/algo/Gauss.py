# Code for solving A x = y using Gauss elimination and back substitution. L. van Veen, Ontario Tech U, 2020.
import numpy as np

def Gauss(A,y):
    # Performs Gauss elimination on the extended matrix (A|y)
    n = np.shape(A)[0]
    B = np.concatenate((A,y),1)
    for j in range(1,n):                                # loop over columns
        for i in range(j+1,n+1):                        # loop over rows below diagonal
            m = B[i-1,j-1]/B[j-1,j-1];                  # Gauss elimination
            for k in range(j,n+2):
                B[i-1,k-1] = B[i-1,k-1] - m * B[j-1,k-1]
            print(B)
    return B

def BackSub(B):
    # Solve U x = z where U is upper triangular. Input is the extended matrix B = (U|z), output is solution x.
    n = np.shape(B)[0]
    x = np.zeros((n,1))
    for i in range(n,0,-1):               # loop over rows, starting from the last
        x[i-1] = B[i-1,n]
        for j in range(i,n):              # the inner loop uses elements of x already solved for
            x[i-1] -= B[i-1,j] * x[j,0]
        x[i-1] /= B[i-1,i-1]
    return x