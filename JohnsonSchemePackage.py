#The goal of this Python code is to make a general package for handling Johnson Schemes and the EKR theorem.
#Currently this counts the number of size i cliques in J(n,k)


import networkx as nx #the network x package is used for graph theory
import itertools #to do set theory
import matplotlib.pyplot as plt #to plot graphs
import numpy as np #numpy is the standard math package for Python

print("-----")
print("Enter the integer n in the Johnson Scheme J(n,k):")
n = input()
n = int(n)
print("-----")
print("Enter the integer k in the Johnson Scheme J(n,k):")
k = input()
k = int(k)
print("-----")
print("Enter the integer i for which you want to find how many size cliques there are in J(n,k):")
i = input()
i = int(i)

def js_parameters(n,k):
    TupleSubsets = set(itertools.combinations(set(list(range(n))), k)) #set of size k subsets of an n element set
    ListSubsets = list() #prepare to change TupleSubsets to a list
    for x in TupleSubsets:
        x = set(x) 
        ListSubsets.append(x)
    return ListSubsets

ListSubsets = js_parameters(n,k) #This gives the set of k-subsets of size n


JGraph=nx.Graph() #set up our graph

for x in ListSubsets:
    for y in ListSubsets:
        if len(x & y) == i:
            JGraph.add_edge(str(x),str(y)) #adding edges if the intersection is size i

def enumerate_all_cliques_size_k(G, k): #counting all the cliques in G of size k
    i = 0
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) == k:
            i += 1
        elif len(clique) > k:
            return i
    return i

print("-----")
print("The number of size " + str(i) + " cliques in J(" + str(n) + "," + str(k) + ") is :")
print(enumerate_all_cliques_size_k(JGraph, i)) 

