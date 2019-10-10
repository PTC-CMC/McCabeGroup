import networkx as nx
import pdb

import scripts.itp_utils as itp_utils

itpfile = open('ucer2.itp','r').readlines()
itpfile = itp_utils.remove_comments(itpfile)
bonds = itp_utils.read_section('bonds', itpfile)
pairs = itp_utils.read_section('pairs', itpfile) # For verification


# Make a Network X graph by adding edges for each bond
bondgraph = nx.Graph()
for line in bonds:
    first = line.split()[0]
    second = line.split()[1]
    bondgraph.add_edge(first,second)
# Cool, we are definitely getting all the bonds here


count =0 
# all pairs is actually a set of quadruples corresponding to the atoms (and
# the ones in between) that make the pair
all_quadruples = set()
all_pairs = set()
for n1 in bondgraph.nodes_iter():
    for n2 in bondgraph.nodes_iter():
        path = nx.shortest_path(bondgraph, n1,n2)
        if len(path) == 4:
            pair = (sorted((n1,n2))[0], sorted((n1,n2))[1])
            if pair not in all_pairs:
                all_pairs.add(pair)
                count+=1
#print(count)
#print(len(all_pairs))
print('[ pairs ]')
for pair in sorted(all_pairs):
    print("{:>5s}{:>5s}{:>5s}".format(pair[0], pair[1], '1'))
