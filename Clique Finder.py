#This was an attempt to write code to find all size 36 cliques in 
#the {0,2} intersection graph of the 8 elements subsets of {0,1, ..., 35}
#It doesn't work because the memory runs out, but one can alter the code so
#that it works for smaller numbers. We do it for size 3 cliques in the {0,2} intersection
#graph of 5 element subsets {0,1, ..., 11}.

import networkx as nx
import itertools
import matplotlib.pyplot as plt

TupleSubsets = set(itertools.combinations(set(list(range(10))), 5)) #set of size k subsets of an n element set
ListSubsets = list() #prepare to change TupleSubsets to a list

#change type from tuple to set

for x in TupleSubsets:
    x = set(x) 
    ListSubsets.append(x)

JGraph=nx.Graph() #this JGraph is our graph

for x in ListSubsets:
    for y in ListSubsets:
        if len(x & y) == 0:
            JGraph.add_edge(str(x),str(y)) #adding edges if the intersection is size 0
        if len(x & y) == 2:
            JGraph.add_edge(str(x),str(y)) #adding edges if the intersection is size 2
         #cardinality of x intersection y
        #     edge = (x, y)
        #     JGraph.add_edge(*edge)


def enumerate_all_cliques_size_k(G, k): #counting all the cliques in G of size k
    i = 0
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) == k:
            i += 1
        elif len(clique) > k:
            return i
    return i

print(enumerate_all_cliques_size_k(JGraph, 3)) 

# nx.draw(JGraph)
# plt.show()
# CliqueNumber = nx.graph_clique_number(JGraph)
# print(CliqueNumber)

# G=nx.Graph()

# #adding one node:
# G.add_node("a")
# #a list of nodes:
# G.add_nodes_from(["b", "c"])

# G.add_edge(1,2)
# edge = ("d","e")
# G.add_edge(*edge)
# edge = ("a","b")
# G.add_edge(*edge)
# G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

# print("Nodes of the graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())

# nx.draw(G)
# plt.show()

#a list of nodes

# G = nx.barbell_graph(m1=5, m2=1)
# nx.find_cliques(G)

# list(nx.find_cliques(G))