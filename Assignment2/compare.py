'''
Andrew Murdoch
100707816

This program creates test vectors to compute the time it takes tridag function to compute y when x is size 10^i from 2 to 7.
It also produces a plot to visualize the time taken by function versus n. You can see that the algorithm is linear as n increases. O(n)

'''

import numpy as np
from tridag_matvec import tridag
import time
import matplotlib.pyplot as plt


times = []                                      #Creating array to store times

for i in range(2, 8):                           #loop through range of 2 to 7
    start_time = time.time()                    #set start time of loop
    n = pow(10, i)                              #create size of array for each loop

    a = np.random.rand(n, 1)                    #create vectors for input
    b = np.random.rand(n - 1, 1)
    c = np.random.rand(n - 2, 1)                
    x = np.random.rand(n, 1)
    
    y = tridag(a, b, c, x)                      #call function with input vectors
    times.append(time.time() - start_time)      #add time from current loop to array
    
    
plt.plot(range(2, 8), times)                    #plot time in seconds versus n
plt.yscale("log")
plt.suptitle("Time vs Matrix Size")             #set y scale to log
plt.xlabel("Size of Matrix (n)")                
plt.ylabel("Time (Seconds)")
plt.show()
