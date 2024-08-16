# Graph-isomorphism
a program to find and plot all possible non-isomorphic graphs


The overall process involves generating all possible adjacency matrices for graphs with n vertices, then testing each matrix under an isomorphism check function. If a graph is not isomorphic with others, it is added to the final list and eventually drawn.

Adjacency Matrix Formation Function: This function stores each matrix in a two-dimensional list and fills its elements with 0s and 1s. It saves all permutations of these in a list named graphs.

Degree Sequences Function: Utilizing the sum of columns in the adjacency matrix, this function creates a list containing degree sequences of the graph.

Vertex Permutation Function: By employing methods from the itertools module, this function generates all vertex permutations of the graph.

Check Isomorphism Function: This function takes two adjacency lists as input and checks the conditions for isomorphism using the previous two functions. That is, if the degree sequences for two graphs match and all possible permutations of the two graphs match using vertex_permutation, the function declares the graphs isomorphic and returns True. If the graphs are not isomorphic, it outputs False.

Finally, the program iterates through all adjacency matrices with n vertices using two nested loops, executing the check algorithm on them. It then draws each graph one by one using the networkx and matplotlib modules.

Execution Method: To test execution initially, set n=4 and display a non-isomorphic graph with others at each iteration. Clicking the cross at the top of the drawing page will move you to the next shape until no other non-isomorphic graphs exist. For n=7, we can simply change the value of n defined at the beginning of the code. However, note that there is no polynomial time algorithm for this problem so we set n=4 for simplification.
