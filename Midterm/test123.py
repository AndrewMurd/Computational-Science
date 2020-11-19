
import numpy as np
from numpy import linalg as LA


a = [[1, -3, 1], 
    [-2, 5.9, -2],
    [2.5, 6.0, 1.5]]

b = np.matrix([[6],
     [-11.8],
     [-11]])

x = np.matrix([[0.99960385], 
     [-1.99996435],
     [-1.0000192]])



top = a*x - b
topnorm = LA.norm(top, 2)
bnorm = LA.norm(b, 2)
ka = LA.cond(a, 2)

print(ka*topnorm/bnorm)

print(topnorm, bnorm, ka)



