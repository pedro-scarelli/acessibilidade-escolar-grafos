import networkx as nx
from networkx.algorithms.connectivity import local_node_connectivity

# 1. Lista de adjacência representando ruas
streets = [('A', 'B'), ('A', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'F'), 
           ('D', 'I'), ('D', 'J'), ('E', 'F'), ('F', 'L'), ('G', 'H'), ('G', 'K'), 
           ('H', 'W'), ('I', 'L'), ('I', 'M'), ('J', 'O'), ('J', 'N'), ('K', 'S'), 
           ('K', 'W'), ('L', 'R'), ('M', 'P'), ('N', 'O'), ('N', 'P'), ('P', 'V'), 
           ('Q', 'V'), ('Q', 'U'), ('S', 'T'), ('R', 'U'), ('R', 'W'), ('T', 'U')]

# 2. Criando o grafo
G = nx.Graph()
G.add_edges_from(streets)

# 3. Conectividade inicial
print("Conectividade inicial:")
print("Julia -> Escola:", local_node_connectivity(G, 'A', 'U'))
print("Rafaela -> Escola:", local_node_connectivity(G, 'O', 'U'))
print("Antonio -> Escola:", local_node_connectivity(G, 'G', 'U'))

# 4. Simulando alagamentos
blocked_streets = [('R', 'U'), ('R', 'W'), ('T', 'U')]
G.remove_edges_from(blocked_streets)

# 5. Conectividade após bloqueios
print("Conectividade após ruas bloqueadas:")
print("Julia -> Escola:", local_node_connectivity(G, 'A', 'U'))
print("Rafaela -> Escola:", local_node_connectivity(G, 'O', 'U'))
print("Antonio -> Escola:", local_node_connectivity(G, 'G', 'U'))
