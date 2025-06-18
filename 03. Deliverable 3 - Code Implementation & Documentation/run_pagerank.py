"""
run_pagerank.py

Purpose:
    Example usage script that ties together the graph loader, matrix builder,
    power method, and plotting utilities to compute and visualize PageRank.

Usage:
    python run_pagerank.py <input_path> [--format edgelist|adjlist] [--alpha ALPHA] [--tol TOL] [--max_iter MAX_ITER]
"""
import argparse
import os

from graph_loader import load_edge_list, load_adjacency_list
from matrix_builder import build_matrix
from power_method import compute_pagerank
from utils import plot_convergence


def main():
    parser = argparse.ArgumentParser(
        description='Compute PageRank on a graph via the Power Method'
    )
    # Input file as a positional argument
    parser.add_argument(
        'input_path',
        help='Path to graph file (edge list or adjacency list)'
    )
    parser.add_argument(
        '--format', '-f', choices=['edgelist', 'adjlist'], default='edgelist',
        help='Input file format (default: edgelist)'
    )
    parser.add_argument(
        '--alpha', '-a', type=float, default=0.85,
        help='Damping factor (default: 0.85)'
    )
    parser.add_argument(
        '--tol', '-t', type=float, default=1e-6,
        help='Convergence tolerance (L1 residual, default: 1e-6)'
    )
    parser.add_argument(
        '--max_iter', '-m', type=int, default=100,
        help='Maximum number of iterations (default: 100)'
    )
    args = parser.parse_args()

    input_file = args.input_path

    if not os.path.isfile(input_file):
        parser.error(f"Input file not found: {input_file}")

    # Load edges based on chosen format
    if args.format == 'edgelist':
        edges = load_edge_list(input_file)
    else:
        adj = load_adjacency_list(input_file)
        edges = [(u, v) for u, nbrs in adj.items() for v in nbrs]

    # Build transition matrix and teleport vector
    P, v = build_matrix(edges, alpha=args.alpha)

    # Execute Power Method
    ranks, residuals = compute_pagerank(P, v, tol=args.tol, max_iter=args.max_iter)

    # Output top 10 nodes by PageRank
    ranked_indices = ranks.argsort()[::-1]
    print("Top 10 nodes by PageRank:")
    for idx in ranked_indices[:10]:
        print(f"Node {idx}: {ranks[idx]:.6f}")

    # Plot convergence history
    plot_convergence(residuals)


if __name__ == '__main__':
    main()
