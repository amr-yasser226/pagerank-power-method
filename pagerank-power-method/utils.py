import matplotlib.pyplot as plt
import numpy as np

def plot_residuals(residuals, title="Residuals", save_path=None):
    """Plots the L1 residuals over iterations, automatically adjusting y-scale."""
    residuals = np.array(residuals)
    iterations = np.arange(1, len(residuals) + 1)

    plt.figure()
    plt.plot(iterations, residuals, marker='o', label="Residuals")

    if np.all(residuals > 0):
        plt.yscale("log")
    else:
        plt.yscale("linear")
        zero_indices = np.where(residuals == 0)[0]
        if len(zero_indices) > 0:
            plt.scatter(zero_indices + 1, residuals[zero_indices], color='red', label="Zero Residuals", zorder=5)

    plt.xlabel("Iteration")
    plt.ylabel("L1 Residual")
    plt.title(title)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.close()
