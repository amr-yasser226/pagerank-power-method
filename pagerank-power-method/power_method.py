import numpy as np
import time

def pagerank_power_method(P, v, alpha=0.85, tol=1e-6, max_iter=100):
    n = len(v)
    r = np.copy(v)
    residuals = []
    start = time.time()

    for k in range(max_iter):
        r_new = alpha * P @ r + (1 - alpha) * v
        res = np.linalg.norm(r_new - r, 1)
        residuals.append(res)
        if res < tol:
            break
        r = r_new

    runtime = time.time() - start
    return r, residuals, k + 1, runtime
