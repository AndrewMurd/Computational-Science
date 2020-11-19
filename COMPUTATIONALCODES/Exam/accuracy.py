# Demonstration of ill-conditioned linear solving. See lecture 7, slide 21.
# By L. van Veen, Ontario Tech U, 2020.
import numpy as np
from LUP import *

# Set order of interpolating polynomial (see lectures 13/14):
n = 20
# Allocate grid x and Vandermonde matrix V:
xs = np.linspace(-1,1,n+1)
V = np.zeros((n+1,n+1))
# Fill matrix V (using the same ordering as the built-in np.vander function):
for i in range(n+1):
    V[i,n] = 1.0
    for j in range(n-1,-1,-1):
        V[i,j] = xs[i] * V[i,j+1]
# Set right hand side in such a way that we know the exact solution:
b = xs - xs*xs
b = np.reshape(b,(n+1,1)) # re-shape as column vector
L, U, P, par, ok = LUP(V) # LUP decomposition
z = ForwardSub(L,P,b)     # forward substitution 
x = BackwardSub(U,z)      # backward substitution
#x = np.linalg.solve(V,b) # or, alternatively, use the np.linalg.solve function
print(x)                  # print the solution, should be all zeros except entries 19 and 20)

# Define the exact solution:
exact = np.zeros((n+1,1))
exact[n-1,0] = 1.0
exact[n-2,0] = -1.0
# Compute K(V):
K = np.linalg.cond(V)
# Compute the residual for the numerical solution:
r = np.dot(V,x) - b
res = np.linalg.norm(r,2)
# Copmute the error of the numerical solution:
e = x - exact
err = np.linalg.norm(e,2)
# Print the result in the form of the inequality "rel. err. <= K(V) X rel. res."
print("rel. err. -> %e <= %e X %e = %e <- K(V) X rel. res." % (err/np.linalg.norm(exact,2),K,res/np.linalg.norm(b,2),K*res/np.linalg.norm(b,2)))
