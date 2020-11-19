from fillA import fillA
from solve1 import solve
n = 10
eps = 1e-10
itmx = 100

A = fillA(n)
v, lam = solve(A ,eps,itmx)
# Do not change the print statements. If you edited any variable name,
# make sure you edit only the variable name in the print statements.

print("Matrix size: %d \nTolerance: %e" % (n,eps))
print("=================Solution=================")
print("Eigenvalue = %e" % (lam))
print("Eigenvector = ", v)
