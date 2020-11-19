import numpy as np



def calc_err(a,x_aprox,b):
    res = np.linalg.norm(b - np.matmul(a,x_aprox))
    
    rel_res = res/np.linalg.norm(b)
    

    k = np.linalg.cond(a)
    
    rel_error = k * rel_res

    print("Residual = %f Relative Residual = %f Relative Error = %f Condition Number = %f" %(res,rel_res,rel_error,k))

    return res, rel_res, rel_error, k
