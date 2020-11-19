import numpy as np

def solve(A,eps,itmx):
    # Initialize v and lambda:
    n = np.shape(A)[0]
    v = np.ones((n,1))
    lam = 0.0
    # Set convergence flag (other ways to break the loop and exit can be used):
    conv = 0
    for i in range(itmx):
        w = A@v                                       # @ is python3, alternatively use np.dot 
        nu = np.linalg.norm(w,2)/np.linalg.norm(v,2)
        err = abs(lam-nu)
        print("%d %e" % (i,err))
        if err < eps:
            conv = 1
            break
        v = np.copy(w)/np.linalg.norm(w,2)            # Not using copy may break things
        lam = np.copy(nu)                             # as lam and nu would point to the same value
    if conv == 0:
        print("No convergence!")
    return v,lam
