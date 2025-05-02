"""
utils.py

Purpose:
    Collection of helper routines for PageRank implementation.

Main Functions:
    - normalize_vector(x: np.ndarray) -> np.ndarray
    - residual(prev: np.ndarray, curr: np.ndarray) -> float
    - plot_convergence(history: List[float]) -> None

Notes:
    Uses matplotlib for plotting convergence curves.
"""

from typing import List
import numpy as np
import matplotlib.pyplot as plt


def normalize_vector(x: np.ndarray) -> np.ndarray:
    """
    Normalize a vector using L1 norm so that its entries sum to 1.

    Args:
        x: Input vector.

    Returns:
        A normalized vector where sum(abs(x)) == 1.
    """
    norm = np.linalg.norm(x, 1)
    if norm == 0:
        raise ValueError("Cannot normalize zero vector using L1 norm.")
    return x / norm


def residual(prev: np.ndarray, curr: np.ndarray) -> float:
    """
    Compute the L1 residual between two vectors: ||curr - prev||_1.

    Args:
        prev: Previous iteration vector.
        curr: Current iteration vector.

    Returns:
        L1 norm of the difference.
    """
    return np.linalg.norm(curr - prev, 1)


def plot_convergence(history: List[float]) -> None:
    """
    Plot the convergence history of residuals over iterations.

    Args:
        history: List of residuals recorded per iteration.
    """
    if not history:
        raise ValueError("Convergence history is empty; nothing to plot.")

    iterations = range(1, len(history) + 1)
    plt.figure()
    plt.plot(iterations, history, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('L1 Residual')
    plt.title('Power Method Convergence')
    plt.grid(True)
    plt.tight_layout()
    plt.show()