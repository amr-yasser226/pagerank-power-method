import matplotlib.pyplot as plt
import numpy as np

def normalize(r):
    return r / np.sum(r)

def plot_residuals(residuals, title, path):
    plt.figure()
    plt.plot(range(1, len(residuals)+1), residuals, marker='o')
    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('L1 Residual')
    plt.title(title)
    plt.grid(True)
    plt.savefig(path)
    plt.close()
