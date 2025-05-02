"""
matrix_builder.py

Purpose:
    Construct the stochastic transition matrix P^T and teleportation vector v
    for PageRank, handling dangling nodes and damping factor.

Main Function:
    - build_matrix(edges: List[Tuple[int, int]], alpha: float)
      -> Tuple[csr_matrix, np.ndarray]

Features:
    - Handles dangling nodes by redistributing probability uniformly.
    - Constructs the Google matrix operator: M = alpha * P^T + (1-alpha) * 1 v^T.
    - Returns P^T (sparse) and v (dense), so compute_pagerank can form M on the fly.
"""

from typing import List, Tuple
import numpy as np
from scipy.sparse import csr_matrix


def build_matrix(
    edges: List[Tuple[int, int]],
    alpha: float = 0.85
) -> Tuple[csr_matrix, np.ndarray]:
    """
    Build the PageRank transition operator.

    Args:
        edges: List of (source, target) edges (0-indexed integers).
        alpha: Damping factor in [0,1].

    Returns:
        P: Sparse matrix of shape (n, n) representing the transpose
           of the stochastic matrix (columns sum to 1 for non-dangling nodes).
        v: Dense teleportation vector of length n (sums to 1).

    Notes:
        - Dangling nodes (zero out-degree) produce zero columns in P.
        - Teleportation vector v is uniform: 1/n per entry.
        - The full PageRank operator M can be formed as:
            M = alpha * P + (1 - alpha) * np.outer(np.ones(n), v)

    Raises:
        ValueError: If alpha is not in [0,1].
    """
    if not (0.0 <= alpha <= 1.0):
        raise ValueError(f"Damping factor alpha must be in [0,1], got {alpha}")

    # Determine number of nodes
    nodes = set(u for u, _ in edges) | set(v for _, v in edges)
    if not nodes:
        raise ValueError("Edges list is empty; cannot infer node set.")
    max_node = max(nodes)
    n = max_node + 1

    # Compute out-degree for each node
    out_degree = np.zeros(n, dtype=float)
    for src, _ in edges:
        out_degree[src] += 1.0

    # Build P (transpose): P[j, i] = 1/out_degree[i] if edge i->j exists
    row_idx = []
    col_idx = []
    data = []
    for src, dst in edges:
        if out_degree[src] > 0:
            row_idx.append(dst)
            col_idx.append(src)
            data.append(1.0 / out_degree[src])

    P = csr_matrix((data, (row_idx, col_idx)), shape=(n, n))

    # Teleportation vector (uniform)
    v = np.ones(n, dtype=float) / n

    return P, v