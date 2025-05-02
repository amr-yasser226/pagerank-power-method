"""
graph_loader.py

Purpose:
    Read and parse graph input from multiple sources, with basic file validation
    and support for comments/blank lines.

Main Functions:
    - load_edge_list(path: str) -> List[Tuple[int, int]]
    - load_adjacency_list(path: str) -> Dict[int, List[int]]
    - load_networkx_graph(nx_graph: networkx.DiGraph) -> List[Tuple[int, int]]
"""

import os
from typing import List, Tuple, Dict
import networkx as nx


def load_edge_list(path: str) -> List[Tuple[int, int]]:
    """
    Load edges from a text file containing one edge per line.
    Lines beginning with '#' or blank lines are ignored.

    Args:
        path: Path to the edge list file.

    Returns:
        A list of (source, target) integer tuples.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If a line cannot be parsed into two integers.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Edge list file not found: {path}")

    edges: List[Tuple[int, int]] = []
    with open(path, 'r') as f:
        for lineno, line in enumerate(f, start=1):
            stripped = line.strip()
            # Skip comments and empty lines
            if not stripped or stripped.startswith('#'):
                continue
            parts = stripped.split()
            if len(parts) != 2:
                raise ValueError(f"Invalid edge format on line {lineno}: '{line.strip()}'")
            try:
                u, v = int(parts[0]), int(parts[1])
            except ValueError:
                raise ValueError(f"Non-integer node ID on line {lineno}: '{line.strip()}'")
            edges.append((u, v))
    return edges


def load_adjacency_list(path: str) -> Dict[int, List[int]]:
    """
    Load an adjacency list from a text file where each line represents a node
    and its neighbors, e.g., 'u v1 v2 v3'.
    Lines beginning with '#' or blank lines are ignored.

    Args:
        path: Path to the adjacency list file.

    Returns:
        A dict mapping each node ID to a list of neighbor IDs.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If a line cannot be parsed correctly.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Adjacency list file not found: {path}")

    adjacency: Dict[int, List[int]] = {}
    with open(path, 'r') as f:
        for lineno, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            parts = stripped.split()
            try:
                node = int(parts[0])
                neighbors = [int(p) for p in parts[1:]]
            except ValueError:
                raise ValueError(f"Invalid format on line {lineno}: '{line.strip()}'")
            adjacency[node] = neighbors
    return adjacency


def load_networkx_graph(nx_graph: nx.DiGraph) -> List[Tuple[int, int]]:
    """
    Convert an existing NetworkX DiGraph to a list of edge tuples.

    Args:
        nx_graph: A pre-loaded NetworkX directed graph.

    Returns:
        A list of (source, target) integer tuples.

    Raises:
        TypeError: If input is not a NetworkX DiGraph.
    """
    if not isinstance(nx_graph, nx.DiGraph):
        raise TypeError("Input graph must be a networkx.DiGraph instance.")
    # Ensure node IDs are integers
    edges = []
    for u, v in nx_graph.edges():
        try:
            u_int, v_int = int(u), int(v)
        except ValueError:
            raise ValueError(f"Non-integer node ID in graph edges: ({u}, {v})")
        edges.append((u_int, v_int))
    return edges