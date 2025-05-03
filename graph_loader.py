import networkx as nx

def load_edge_list(file_path, directed=True):
    if directed:
        G = nx.read_edgelist(file_path, create_using=nx.DiGraph(), nodetype=int)
    else:
        G = nx.read_edgelist(file_path, create_using=nx.Graph(), nodetype=int)
    return G
