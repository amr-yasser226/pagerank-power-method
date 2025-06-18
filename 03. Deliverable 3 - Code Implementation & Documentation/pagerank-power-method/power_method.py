'''
power_method.py

Purpose:
    Implement the iterative solver for the PageRank eigenproblem using the Power Method.

Main Function:
    compute_pagerank(
        P: csr_matrix,
        v: np.ndarray,
        alpha: float = 0.85,
        tol: float = 1e-6,
        max_iter: int = 100
    ) -> Tuple[np.ndarray, List[float], int, float]

Behavior:
    - Initializes a uniform rank vector.
    - Iteratively updates via the Google operator: r_new = alpha * P @ r + (1-alpha) * v.
    - Optionally normalizes the vector each step for numerical stability.
    - Tracks L1 residual at each iteration for convergence diagnostics.
    - Returns final rank, residual history, iterations count, and runtime.
'''

from typing import Tuple, List
import numpy as np
import time
from scipy.sparse import csr_matrix
from utils import normalize_vector, residual


def compute_pagerank(
    P: csr_matrix,
    v: np.ndarray,
    alpha: float = 0.85,
    tol: float = 1e-6,
    max_iter: int = 100
) -> Tuple[np.ndarray, List[float], int, float]:
    """
    Compute PageRank scores using the Power Method.

    Solves for r satisfying:
        r = alpha * P @ r + (1 - alpha) * v

    Args:
        P: Column-stochastic transition matrix (n x n).
        v: Teleportation vector (n,), sums to 1.
        alpha: Damping factor, typically 0.85.
        tol: Convergence tolerance on L1 norm.
        max_iter: Maximum number of iterations.

    Returns:
        r: Final PageRank vector (n,), L1-normalized.
        residuals: List of L1 residuals per iteration.
        iterations: Number of iterations performed.
        runtime: Total time elapsed (seconds).

    Raises:
        ValueError: If dimensions of P and v mismatch.
    """
    # Validate inputs
    n = P.shape[0]
    if P.shape[1] != n:
        raise ValueError(f"Transition matrix P must be square, got {P.shape}")
    if v.shape[0] != n:
        raise ValueError(f"Teleportation vector v length {v.shape[0]} does not match P dimension {n}")

    # Initialize rank vector uniformly
    r = np.ones(n, dtype=float) / n
    residuals: List[float] = []

    start_time = time.time()
    # Power iteration
    for k in range(1, max_iter + 1):
        # Apply Google operator
        r_new = alpha * (P @ r) + (1 - alpha) * v
        # Normalize for numerical stability
        r_new = normalize_vector(r_new)

        # Compute L1 residual
        res = residual(r_new, r)
        residuals.append(res)

        # Check convergence
        if res < tol:
            r = r_new
            break

        r = r_new

    runtime = time.time() - start_time
    return r, residuals, k, runtime
