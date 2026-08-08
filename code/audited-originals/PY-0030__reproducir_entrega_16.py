import networkx as nx
G=nx.DiGraph([(0,1),(0,2),(1,3),(2,3)])
print("DAG:",nx.is_directed_acyclic_graph(G))
print("topological orders exist:",list(nx.topological_sort(G)))
