# Name: Andrew Murdoch
# Student ID: 100707816

# Do not change the name of the variables already given in the template.
# You can implement the script as you want as long as you keep the specified variables the same.
# Do not change the print statements.
# Save your script as test.py

from fillA import fillA
from solve import solve

n = 10
eps = 10e-10

# Use the following names. Implementation is up to you as long as the names are the dollowing:
A = fillA(n)
v, lam = solve(A, eps)


# Do not change the print statements. If you edited any variable name,
# make sure you edit only the variable name in the print statements.

print("Matrix size: %d \nTolerance: %e" % (n,eps))
print("=================Solution=================")
print("Eigenvalue = %e" % (lam))
print("Eigenvector = ", v)
