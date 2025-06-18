'''
utils.py

Purpose:
    Helper routines for PageRank implementation and diagnostics.

Main Functions:
    - normalize_vector(x: np.ndarray) -> np.ndarray
    - compute_residual(prev: np.ndarray, curr: np.ndarray) -> float
    - plot_residuals(history: List[float], title: str = 'Power Method Convergence',
                     path: Optional[str] = None) -> None

Notes:
    Uses matplotlib for plotting convergence curves. If `path` is provided,
    saves the figure to file, otherwise displays it interactively.
'''

from typing import List, Optional
import numpy as np
import matplotlib.pyplot as plt


def normalize_vector(x: np.ndarray) -> np.ndarray:
    """
    Normalize a vector using the L1 norm so its entries sum to 1.

    Args:
        x: Input vector.

    Returns:
        A vector scaled such that sum(abs(x)) == 1.

    Raises:
        ValueError: If the input is the zero vector.
    """
    norm = np.linalg.norm(x, 1)
    if norm == 0:
        raise ValueError("Cannot normalize zero vector using L1 norm.")
    return x / norm


def compute_residual(prev: np.ndarray, curr: np.ndarray) -> float:
    """
    Compute the L1 residual between two vectors: ||curr - prev||_1.

    Args:
        prev: Previous iteration vector.
        curr: Current iteration vector.

    Returns:
        L1 norm of the difference.
    """
    return np.linalg.norm(curr - prev, 1)


def plot_residuals(
    history: List[float],
    title: str = 'Power Method Convergence',
    path: Optional[str] = None
) -> None:
    """
    Plot the convergence history of residuals over iterations.

    Args:
        history: List of L1 residuals per iteration.
        title: Plot title.
        path: Optional file path to save the figure. If None, displays interactively.

    Raises:
        ValueError: If history is empty.
    """
    if not history:
        raise ValueError("Convergence history is empty; nothing to plot.")

    iterations = list(range(1, len(history) + 1))
    plt.figure()
    plt.plot(iterations, history, marker='o')
    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('L1 Residual')
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()

    if path:
        plt.savefig(path)
        plt.close()
    else:
        plt.show()
        plt.close()
