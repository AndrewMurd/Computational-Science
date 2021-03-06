"""
#Andrew Murdoch
#100707816

This script uses finite differences to aproximate f'(x) at x = 2 and compares error of aproximation to O(h) and O(h) slopes
"""

import numpy as np
import matplotlib.pyplot as plt
a = 2                            #f(a) so f(x=2)           
fwd_diff = np.zeros((17,1))
c_diff = np.zeros((17,1))
E_f = np.zeros((17,1))
E_c = np.zeros((17,1))

def f(x):
    return np.log(x)        #Initialize f

def fprime(x):              #Initialize fprime
    return 1/x

h = [1.0]
for i in range (1,17):
    h.append(10**-i)        #Append correct h values  

def ffd(h):
    return (f(a+h)-f(a))/h 

def cd(h):
    return (f(a+h)-f(a-h))/(2*h)    

for j in range(0,17):
    c_diff[j,0] = cd(h[j])                      #Calculate both finite differences values
    fwd_diff[j,0] = ffd(h[j])                   
    E_f[j,0] = abs(fprime(a) - fwd_diff[j,0])   #Calculate error of equations
    E_c[j,0] = abs(fprime(a) - c_diff[j,0])
    
    Ep = E_f[j,0]
    E = E_c[j,0]
    H = h[j]
    print("h: %e Ep: %e E: %e" % (H,Ep,E))
    
    
#Plotting errors Ep and E compared to error of finite differences formulas
def g(x):
    return x
def k(x):
    return x**2

oh = []
oh2 = []
for i in range (17):
    oh.append(g(h[i]))
    oh2.append(k(h[i]))

plt.figure()
plt.title("Error of finite differencing")
plt.loglog(h,E_f,'bo-',label = "Error in Forward Finite Difference")
plt.loglog(h,E_c,'ro-',label = "Error in Centred Finite Difference")
plt.plot(h[0:9],oh[0:9],'g--',label = "y = x, showing slope of O(h)" )
plt.plot(h[0:7],oh2[0:7],'--',color = "orange",label = "y = x^2 showing slope of O(h^2)")
plt.xlabel("h")
plt.ylabel("Error")
plt.xlim(1e-15,1e0)
plt.ylim(1e-11,10)
plt.legend()
plt.show()