import numpy as np
from scipy import linalg,random
import time
import matplotlib.pyplot as plt
from doctest import testmod


def det(matrix):

    time_start = int(round(time.time() * 1000))
    
    if matrix.shape[0] != matrix.shape[1]:
        return None, int(round(time.time() * 1000)) - time_start

    if matrix.shape == (1, 1):
        return matrix[0], int(round(time.time() * 1000))- time_start

    if matrix.shape == (2, 2):
        return (
            matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0],
            int(round(time.time() * 1000))- time_start,
        )

    determ = 0

    matrix_notop = matrix[1:]
    parity = -1

    for i, value in enumerate(matrix[0]):
        parity *= -1

        newMatrix = np.delete(matrix_notop, i, axis=1)
        determ += parity * value * det(newMatrix)[0]
    return [determ, int(round(time.time() * 1000)) - time_start]

