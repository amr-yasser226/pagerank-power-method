import numpy as np
from utils import l1_norm, residual

def power_method(M):
    residuals = []
    epsilon=1e-8, max_iter=100
    n = M.shape[0]
    r = np.ones(n)/n
   

    for k in range(max_iter):
        r_prev = r.copy()
        r = M @ r_prev
        r /= l1_norm(r)
        res = residual(r, r_prev)
        residuals.append(res)
        if res < epsilon:
            break
            
    return r, k+1, residuals