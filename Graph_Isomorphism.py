import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


n = 4
edges = list(itertools.combinations(range(n), 2))
graphs = []
for i in range(len(edges) + 1):
    for j in itertools.combinations(edges, i):
        graph = [[0] * n for _ in range(n)]
        for edge in j:
            graph[edge[0]][edge[1]] = 1
            graph[edge[1]][edge[0]] = 1
        graphs.append(graph)

for graph in graphs:
    graph=np.array(graph)
    
def vertex_permutations(adj_matrix):
    all = []
    idx = list(range(len(adj_matrix)))
    possible_idx_combinations = [
        list(i) for i in itertools.permutations(idx, len(idx))
    ]
    for comb_index in possible_idx_combinations:
        t = adj_matrix
        t = t[comb_index]
        t = np.transpose(np.transpose(t)[comb_index])
        all.append({"perm_vertex":comb_index,"adj_matrix": t})

    return all

def degree_sequences(adj_matrix):
    degree_sequence = []
    for vertex in range(len(adj_matrix)):
        degree_sequence.append(sum(adj_matrix[vertex]))
    degree_sequence.sort(reverse=True)
    return degree_sequence

def check_isomorphism(adj_1, adj_2):
    degree_sequence_1 = degree_sequences(adj_1)
    degree_sequence_2 = degree_sequences(adj_2)
    if np.array_equal(degree_sequence_1, degree_sequence_2) == False:
        return False
    else:
        for adj_matrix in list(
                map(lambda matrix: matrix["adj_matrix"],
                    vertex_permutations(adj_2))):
            if np.array_equal(adj_1, adj_matrix) == True:
                return True
    return False

list_non_iso=[]

for x in graphs:
    for i in range (graphs.index(x),len(graphs)):
        if i != graphs.index(x):

            if check_isomorphism(np.array(x),np.array(graphs[i]))==False  :
                list_non_iso.append(graphs[i])
   
            else:
             while graphs[i] in list_non_iso:
                 list_non_iso.remove(graphs[i])
f=[]                 
for i in range(n):
    f.append([0]*n)
list_non_iso.append(f)
    

                              
final_list=[]
for i in list_non_iso:
    if i not in final_list:
        final_list.append(i)
    
             
for elements in final_list:

    g=nx.Graph(np.array(elements))
    nx.draw(g)
    plt.show()
