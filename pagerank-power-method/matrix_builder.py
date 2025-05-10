import numpy as np
import networkx as nx

def build_transition_matrix(G):
    n = len(G)
    A = nx.to_numpy_array(G, dtype=float)
    P = np.zeros_like(A)
    for j in range(n):
        col_sum = A[:, j].sum()
        if col_sum != 0:
            P[:, j] = A[:, j] / col_sum
        else:
            P[:, j] = 1.0 / n  # dangling node
    return P

def build_teleportation_vector(n):
    return np.ones(n) / n
