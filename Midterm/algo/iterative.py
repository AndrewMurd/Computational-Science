import math 

def iterative(func,initial_point,K,res,error):
    x = initial_point
    
    for i in range(K):
        print("iteration:"+str(i)+" x="+str(x))
     
        x_prev = x

        x = func(x)
        if abs(func(x)) < res and abs(x-x_prev) < error:
            return x
        

def fx(x):
    return (1/(2*math.pi))*math.sin(math.pi*x)-(1/(2*math.pi))*(x**2)+x

print(iterative(fx,2,10,1e-10,1e-10))