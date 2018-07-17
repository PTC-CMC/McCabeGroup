import ecer2 as ecer2
import networkx as nx
import pdb
from collections import OrderedDict
from oset import oset
cmpd = ecer2.ecer2()

bg = cmpd.bond_graph
# need to actualy make a networkx graph
# Create a relationship dictionary between the bondgraph and an arbitray node
relationship_dict = OrderedDict()
pairs = oset()
G = nx.Graph()
for i, node in enumerate(cmpd.particles()):
    relationship_dict[node]= i 
    G.add_node(i)
for edge in bg.edges():
    G.add_edge(relationship_dict[edge[0]], relationship_dict[edge[1]], weight=1)
for i, node1 in enumerate(G.nodes()):
    for j, node2 in enumerate(G.nodes()):
        pathlength = nx.shortest_path_length(G, node1, node2)
        if pathlength == 3:
            pairs.add((min(node1,node2), max(node1,node2)))
for (first, second) in pairs:
    print("{}\t{}\t1".format(first+1,second+1))
