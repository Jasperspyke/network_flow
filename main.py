import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

iterations = 10

idx = [0, 1, 2, 3, 4]
temp = [0.0, 0.0, 300.0, 0.0, 0.0]
alpha = 0.001


def heat_flow(temp0, temp1):
    return round(temp0 + alpha * (temp1 - temp0), 4), round(temp1 - alpha * (temp1 - temp0), 4)

# Update temperature of nodes over n time steps
for i in range(iterations):
    g = 'G' + str(i)
    g = nx.Graph()
    adjacency = [(2, x) for x in range(len(idx))]
    adjacency.append((3, 4))
    g.add_edges_from(adjacency)
    all_edges = list(g.edges())
    for edge in all_edges:
        y0, y1 = heat_flow(temp[edge[0]], temp[edge[1]])
        temp[edge[0]] = y0
        temp[edge[1]] = y1



# Set nodes to reflect temperature
f = nx.Graph()
f.add_nodes_from(temp)
all_temp_edges = []
for edge in all_edges:
    all_temp_edges.append((temp[edge[0]], temp[edge[1]]))
f.add_edges_from(all_temp_edges)


# Remove self-edges
for edge in all_edges:
    if edge[0] == edge[1]:
        g.remove_edge(*edge)
for edge in all_temp_edges:
    if edge[0] == edge[1]:
        f.remove_edge(*edge)

# plot the graph
nx.draw(f, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()