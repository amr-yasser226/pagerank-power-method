import networkx as nx
from matrix_builder import build_transition_matrix, build_teleportation_vector
from power_method import pagerank_power_method
from utils import plot_residuals
import os

toy_graphs = {
    "Cycle-4": nx.DiGraph([(0,1),(1,2),(2,3),(3,0)]),
    "Star-5": nx.DiGraph([(0,1),(0,2),(0,3),(0,4)]),
    "Complete-5": nx.complete_graph(5).to_directed(),
    "Chain-6": nx.DiGraph([(0,1),(1,2),(2,3),(3,4),(4,5)]),
    "Bipartite-3x3": nx.DiGraph([(i, j+3) for i in range(3) for j in range(3)])
}

os.makedirs("deliverable_4/plots", exist_ok=True)

for name, G in toy_graphs.items():
    P = build_transition_matrix(G)
    v = build_teleportation_vector(len(G))
    r, residuals, iters, runtime = pagerank_power_method(P, v)
    print(f"{name}: {iters} iterations, Final residual={residuals[-1]:.2e}")
    plot_residuals(residuals, f"{name} Residuals", f"deliverable_4/plots/{name}_residuals.png")
