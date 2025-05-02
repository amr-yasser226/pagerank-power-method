import networkx as nx
import numpy as np
def load_from_adjacency (path):
    G = nx.read_adjlist(path, create_using=nx.DiGraph)
    return G
def load_from_edgelist(path):
    graph = nx.read_edgelist(path, 
            create_using=nx.DiGraph)
    return graph

