"""
#Andrew Murdoch
#100707816

This script calculates the simpson aproximation until the error is less then 10^-12
"""

import math
import scipy
from scipy import integrate
from compositeSimpson import compositeSimpson
from compositeSimpson import f

actual = scipy.integrate.quad(lambda x:x*math.exp(-x**2),0,3) #Get actual integral answer

M = 1
while(True):
    I = compositeSimpson(f,0,3,M)   #Call function to aproximate
    err = abs(I-actual[0])          #Get error between approximate value and actual value
    if(err > 10**-12):              #Continue if error is larger then 10^-12
        M = M + 1
    
    else:
        break
    print("M: %d err: %e" %(M,err)) 