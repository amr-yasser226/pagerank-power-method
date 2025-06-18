'''
graph_loader.py

Purpose:
    Read and parse graph data from various formats, with validation,
    comment/blank-line support, and conversion utilities.

Main Functions:
    - load_edge_list(path: str, directed: bool = True) -> List[Tuple[int, int]]
    - load_adjacency_list(path: str) -> Dict[int, List[int]]
    - graph_to_edge_list(graph: nx.Graph) -> List[Tuple[int, int]]
'''

import os
from typing import List, Tuple, Dict, Union
import networkx as nx


def load_edge_list(
    path: str,
    directed: bool = True
) -> List[Tuple[int, int]]:
    """
    Load edges from a text file where each non-comment line has two ints: u v.

    Args:
        path: File path to read.
        directed: If True, returns edges for a DiGraph; else for an undirected Graph.

    Returns:
        List of (source, target) integer tuples.

    Raises:
        FileNotFoundError: If the file is missing.
        ValueError: On malformed lines.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Edge list file not found: {path}")

    edges: List[Tuple[int, int]] = []
    with open(path, 'r') as f:
        for lineno, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            parts = stripped.split()
            if len(parts) != 2:
                raise ValueError(f"Invalid format on line {lineno}: '{stripped}'")
            try:
                u, v = map(int, parts)
            except ValueError:
                raise ValueError(f"Non-integer node ID on line {lineno}: '{stripped}'")
            edges.append((u, v))
    return edges


def load_adjacency_list(
    path: str
) -> Dict[int, List[int]]:
    """
    Load a node-to-neighbors mapping from a text file: u v1 v2 ...

    Args:
        path: File path to read.

    Returns:
        Dict mapping node ID to list of neighbor IDs.

    Raises:
        FileNotFoundError: If the file is missing.
        ValueError: On malformed lines.
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
                raise ValueError(f"Invalid format on line {lineno}: '{stripped}'")
            adjacency[node] = neighbors
    return adjacency


def graph_to_edge_list(
    graph: Union[nx.Graph, nx.DiGraph]
) -> List[Tuple[int, int]]:
    """
    Convert a NetworkX graph to an edge-list of integer tuples.

    Args:
        graph: A networkx.Graph or networkx.DiGraph.

    Returns:
        List of (source, target) integer tuples.

    Raises:
        TypeError: If not a NetworkX graph instance.
        ValueError: If graph contains non-integer nodes.
    """
    if not isinstance(graph, (nx.Graph, nx.DiGraph)):
        raise TypeError("Input must be a networkx.Graph or DiGraph.")

    edges: List[Tuple[int, int]] = []
    for u, v in graph.edges():
        try:
            u_i, v_i = int(u), int(v)
        except (ValueError, TypeError):
            raise ValueError(f"Non-integer node ID in edge: ({u}, {v})")
        edges.append((u_i, v_i))
    return edges
