import numpy
import scipy as sp

x = sp.array([[-2], [0.25], [0.9], [1.5], [2]])
y = sp.array([[0.99], [1.44], [1.59], [2.35], [3.24]])


def least_squares_interpolant(x, y):
    xmat = sp.zeros((len(x), 2))
    for i in range(len(x)):
        for j in range(2):
            xmat[i][j] = x[i] ** j
    a = sp.matmul(sp.transpose(xmat), xmat)
    b = sp.matmul(sp.transpose(xmat), y)
    ans = numpy.linalg.solve(a, b)
    return ans, xmat


def f(x, a):
    return a[0] + (x * a[1])


def findError(x, y, a, f):
    err = 0
    for i in range(len(x)):
        err = err + (y[i] - (f(x[i], a))) ** 2
    return err


a, xmat = least_squares_interpolant(x, y)
err = findError(x, y, a, f)

print('x: \n', x)
print('y: \n\n', y)
print('coefficients: \n', a)
print('\nerr:', err)
