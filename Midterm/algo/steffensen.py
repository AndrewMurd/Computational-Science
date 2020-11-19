# By: Cole Mollica 100706187
# Partner: Nischal Bhardwaj 100706116
# Python 3.5.3

import math




# Takes function, functions_prime (not derivative), inital guess point, max error,
# and max iteratoions

# Will return x* estimate and error in a list

def steffensen(f,f_prime,x,epsilon,N):
	for i in range(N):
		y1 = x
		y2 = y1 - f(y1) / f_prime(y1,f)
		y3 = y2 - f(y2) / f_prime(y2,f)


		x = y1 - ((math.pow((y2-y1),2)) / (y3 - (2*y2) + y1))
		
		print("iteration"+str(i)+ abs(f(x)))

		if (abs(f(x)) < epsilon):
			print("Converged")
			return x,f(x)

def f(x):
	return math.exp(-1*math.pow(x,2) + x) + (-1*(.5*x) - 1.0836)

def fp(x,f):
	return (f(x+f(x)) / f(x)) -1