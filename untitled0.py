# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:51:30 2023

@author: adfw980
"""

import networkx as nx


import matplotlib.pyplot as plt

G=nx.Graph()

G.add_nodes_from([
    
    (1, {"name":"A"}),
    (2, {"name":"B"}),
    (3, {"name":"C"}),
    (4, {"name":"D"}),
    (5, {"name":"E"}),
    (6, {"name":"F"}),
    (7, {"name":"G"}),
    (8, {"name":"H"}),
    
    ])

G.add_edges_from([(1,2), (1,3),(2,3), (3,4), (3,5), (4,6), (6,7), (6,8) ])

nx.degree_centrality(G)

#The node with the highest degree of centrality is 3 or C

nx.betweenness_centrality(G)

#The node with the highest betweeness centrality is 3 or C

G[1][3]['weight'] = 3
G[3][5]['weight'] = 4

nx.betweenness_centrality(G)

positions = nx.spring_layout(G)

nx.draw(G,pos=positions)

nx.draw_networkx(G)

nx.draw(G,pos=positions)
nx.draw_networkx_labels(G,pos=positions)
plt.draw() 

#Coauthorship Graph Analysis

G2=nx.read_graphml("netScience.graphml")

[len(c) for c in sorted(nx.connected_components(G2), key=len, reverse=True)]

Gc = max(nx.biconnected_components(G2), key=len)

nx.betweenness_centrality(G2)

