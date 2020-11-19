import numpy as np


def phi(xk, a):
    return 0.5 * (xk + (a/xk))

def FP(xO, a, kmax, epsilon):
    errors = []
    xk_new = xO

    for i in range(kmax):
        xk_old = xk_new
        xk_new = phi(xk_new, a)
        change_in_xk = abs(xk_new - xk_old)
        print(xk_new)

        if change_in_xk < epsilon:
            break

        true_answer = np.sqrt(a)
        true_error = abs(xk_new - true_answer)
        errors.append(true_error)

def F(x):
    
    return


FP(0.3, 5, 10, 1/1000)

