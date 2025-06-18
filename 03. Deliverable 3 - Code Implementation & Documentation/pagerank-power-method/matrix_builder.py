'''
matrix_builder.py

Purpose:
    Construct the stochastic transition matrix and teleportation vector for PageRank,
    handling dangling nodes and damping factor.

Main Function:
    build_matrix(
        edges: List[Tuple[int, int]],
        alpha: float = 0.85
    ) -> Tuple[csr_matrix, np.ndarray]

Features:
    - Infers node set from edge list.
    - Builds column-stochastic P^T (sparse) with dangling nodes as zero columns.
    - Creates uniform teleportation vector v (dense).

Usage:
    P, v = build_matrix(edges, alpha=0.85)
    # Then compute PageRank via r = alpha*P@r + (1-alpha)*v
'''

from typing import List, Tuple
import numpy as np
from scipy.sparse import csr_matrix


def build_matrix(
    edges: List[Tuple[int, int]],
    alpha: float = 0.85
) -> Tuple[csr_matrix, np.ndarray]:
    """
    Build the PageRank transition operator components:
        P: column-stochastic sparse matrix (transpose of transition matrix)
        v: uniform teleportation vector

    Args:
        edges: List of directed edges (src, dst), zero-indexed.
        alpha: Damping factor in [0,1]; only validated here.

    Returns:
        P: csr_matrix, shape (n, n), columns sum to 1 for non-dangling nodes.
        v: np.ndarray, shape (n,), teleportation vector summing to 1.

    Raises:
        ValueError: If edges list is empty or alpha out of [0,1].
    """
    # Validate alpha
    if not 0.0 <= alpha <= 1.0:
        raise ValueError(f"Damping factor alpha must be in [0,1], got {alpha}")

    # Infer node set
    nodes = {u for u, _ in edges} | {v for _, v in edges}
    if not nodes:
        raise ValueError("Edge list is empty; cannot infer number of nodes.")
    n = max(nodes) + 1

    # Compute out-degrees
    out_degree = np.zeros(n, dtype=float)
    for src, _ in edges:
        out_degree[src] += 1

    # Assemble sparse P^T
    rows, cols, data = [], [], []
    for src, dst in edges:
        if out_degree[src] > 0:
            rows.append(dst)
            cols.append(src)
            data.append(1.0 / out_degree[src])

    P = csr_matrix((data, (rows, cols)), shape=(n, n))

    # Handle dangling nodes: columns with zero sum get uniform distribution
    dangling = np.where(out_degree == 0)[0]
    if dangling.size > 0:
        # For each dangling node j, set P[:, j] = 1/n
        for j in dangling:
            P[:, j] = np.ones(n) / n

    # Teleportation vector
    v = np.ones(n, dtype=float) / n

    return P, v
