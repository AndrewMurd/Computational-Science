import math 
def dist(theta,c=0.001,g=9.8,V0=40):
    return (1/c) * math.log((c*V0*math.cos(theta)/math.sqrt(c*g)) *                    \
                       (math.atan(math.sqrt(c/g)*V0*math.sin(theta)) +                 \
                        math.acosh(math.sqrt((g+c* V0**2 * math.sin(theta)**2)/g)))+1.0) -100


def secant_method(f, x0: int, x1: int, iterations: int, resVal: float, errVal: float) -> float:
    """Return the root calculated using the secant method."""
    xs = [x0, x1] + iterations * [None]  # Allocate x's vector

    for i, x in enumerate(xs):
        if i < iterations:
            x1 = xs[i+1]
            xs[i+2] = x1 - f(x1) * (x1 - x) / (f(x1) - f(x)) # fill component xs[i+2]
        err = abs(xs[i+2] - xs[i+1])
        res = abs(f(xs[i+2]))
        if err < errVal and res < resVal:
            print("Converfed")
            return xs[i+2],err,res

    return xs[-1]  # Return the now filled last entry



print(secant_method(dist,1,math.pi/2,99,1e-12,1e-12))