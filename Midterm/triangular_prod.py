# Code for multiplication of triangular matrices, see 2019 midterm, Q4. Author: L. van Veen, UOIT, 2019.
import scipy

def triangular_prod(L1,L2):
    n = L1.shape[0]
    L = scipy.zeros((n,n))
    for i in range(0,n):
        for j in range(0,i+1):
            for k in range(0,n):              # Change to range(j,i+1) for greater efficiency (see bonus question) 
                L[i,j] += L1[i,k]*L2[k,j]
    return L
