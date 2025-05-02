"""
power_method.py

Purpose:
    Implement the iterative solver for the PageRank eigenproblem using the Power Method.

Main Function:
    - compute_pagerank(P: csr_matrix, v: np.ndarray, tol: float = 1e-6, max_iter: int = 100)
      -> Tuple[np.ndarray, List[float]]

Behavior:
    - Initializes a uniform rank vector.
    - Iteratively updates and normalizes.
    - Tracks L1 residual at each iteration for convergence diagnostics.
"""

from typing import Tuple, List
import numpy as np
from scipy.sparse import csr_matrix
from utils import normalize_vector, residual


def compute_pagerank(
    P: csr_matrix,
    v: np.ndarray,
    tol: float = 1e-6,
    max_iter: int = 100
) -> Tuple[np.ndarray, List[float]]:
    """
    Compute PageRank scores using the Power Method for the eigenproblem:
        r = M @ r, where M = alpha * P.T + (1-alpha) * v

    Args:
        P: Transition probability matrix (stochastic, columns sum to 1).
        v: Teleportation vector (sum to 1).
        tol: Convergence tolerance for L1 residual.
        max_iter: Maximum number of iterations.

    Returns:
        r: Final PageRank vector (L1-normalized).
        residuals: List of L1 residuals per iteration.

    Raises:
        ValueError: If dimensions of P and v mismatch.
    """
    # Validate inputs
    n = P.shape[0]
    if v.shape[0] != n:
        raise ValueError(f"Dimension mismatch: P is {n}x{n}, but v has length {v.shape[0]}")

    # Construct the Google matrix operator via a linear combination
    # Note: We assume P is already the modified matrix M (with teleportation included),
    #       or user can build M beforehand. Here we directly apply P as the full operator.
    M = P

    # Initialize rank vector uniformly
    r = np.ones(n, dtype=float) / n
    residuals: List[float] = []

    # Power iteration
    for k in range(1, max_iter + 1):
        r_prev = r.copy()
        # Multiply and normalize
        r = M.dot(r_prev)
        r = normalize_vector(r)

        # Compute L1 residual
        res = residual(r, r_prev)
        residuals.append(res)

        # Check convergence
        if res < tol:
            break

    return r, residuals