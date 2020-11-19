"""
BISECTION
"""
import math


def f(x):  # your function goes here
    return (0.1 * math.exp(4.43 * x)) - math.sqrt(4.43 * x)


def bisection(l, r, n, eps):
    m = (l + r) / 2
    err = abs(r - l) / 2
    fm = f(m)
    res = abs(fm)
    x = m
    print("l=" + str(l) + " r=" + str(r) + "error=" + str(err))
    if n > 0:
        if err > eps:
            fl = f(l)
            if fm * fl > 0:
                l = m
            else:
                r = m
            x, err, res = bisection(l, r, n - 1, eps)
    return x, err, res


l = 0  # your left bound goes here

r = 5  # your right bound goes here

n = 10000  # your max iterations goes here

eps = 10 ** -6  # your error bound goes here

print(bisection(l, r, n, eps))
print(f(0.63683))  # displays the bisection function
