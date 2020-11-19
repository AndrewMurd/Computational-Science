from LUP import LUP
import numpy as np
import scipy
import time
import matplotlib.pyplot as plt


def determinant_lup(matrix):
     
    time_start = int(round(time.time() * 1000))
    

    values = LUP(matrix)
    U = values[1]
    P = values[2]

    sigma = -1

    if P.shape[0] % 2 == 0:
        sigma = 1
      
    determine_value = 1
    for i in range(U.shape[0]):
        determine_value *= U[i][i]

    determine_value * sigma

    return determine_value, int(round(time.time() * 1000)) - time_start
