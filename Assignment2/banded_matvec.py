'''
Andrew Murdoch
100707816

This program computes the condition number of C. If we solve Cx = Q, 
where Q is a 2-Vector of which we know entries up to 5 digits of precision.

Output:
1252.4992015962914
This means we can computer x up to two digits in precision.
'''

import numpy as np
from scipy.linalg import solve

C = [[2,0], [50,1]]         

x = np.linalg.cond(C)  #Calculate Condition number of C.

print(x)