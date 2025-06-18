import networkx as nx
from matrix_builder import build_transition_matrix, build_teleportation_vector
from power_method import pagerank_power_method
from utils import plot_residuals

G = nx.karate_club_graph().to_directed()
P = build_transition_matrix(G)
v = build_teleportation_vector(len(G))
r, residuals, iters, runtime = pagerank_power_method(P, v)

print(f"Karate Club: {iters} iterations, runtime={runtime:.2f}s, Final residual={residuals[-1]:.2e}")
plot_residuals(residuals, "Karate Club Residuals", "deliverable_4/plots/karate_residuals.png")
