import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3,4,5,6])
G.remove_node(2)
G.add_edge(1,3)
G.add_edges_from([(1,4),(4,5), (6,3), (6,5),(6,4)])
nx.diametr(G)
G.number_of_nodes()
G.number_of_edges()
nx.density(G)
nx.average_clustering(G)
deg = nx.degree_centrality(G)

for node in G.nodes():
    print(node, G.degree(node))

for node_id in sorted(deg, key = deg.get, reverse = True):
    print(node_id, deg[node_id])

nx.write_gexf(G,'graph.gexf')

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color = "red", node_size = 50)
nx.draw_networkx_edges(G, pos, edge_color = "yellow")
plt.axis("off")
plt.show()
plt.savefig("graph.png")
nx.draw_networkx_labels(G, pos, font_size = 10)
