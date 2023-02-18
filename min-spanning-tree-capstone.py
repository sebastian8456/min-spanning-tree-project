# Time: 1+ wks
# Project: minimum spanning tree' (graph)
# Difficulty: Hard

# Goal:
    # Create a program which takes a connected, undirected graph with weights and 
        # outputs the minimum spanning tree of the graph 
        # i.e., a subgraph that is a tree, contains all the vertices, and the sum of its weights is the least possible.
    # Automate the creation of a min. spanning tree
    
# Requirements:
    # It must not form a cycle i.e, no edge is traversed twice.
    # There must be no other spanning tree with lesser weight.
    
# Hints:
    # The total number of spanning trees with n vertices that can be created from a complete graph is equal to n(n-2).
    # A minimum spanning tree is a spanning tree in which the sum of the weight of the edges is as minimum as possible.
    # Min. spanning tree algorithms include: Prim's algorithm (adjecency matrix), Kruskal's algorithm
    # In case of undirected graphs, the matrix is symmetric about the diagonal because of every edge (i,j), 
        # there is also an edge (j,i).
    # ! Max. edges to remove are (E-V+1)

import random
import math

#To Do: Make the program clearly state the vertices variable
class Graph:
    def __init__(self, size):
        self.adjMatrix = []
        self.size = size
        for i in range(size):
            self.adjMatrix.append([0 for j in range(size)])
    
    def get_verticies():
        msg = 'How many verticies are in the graph? (1-10): '
        v = input(msg)
        while not (v.isdigit()) or int(v) not in range(1,11):
            v = input(msg)
        return int(v)
    
    def print_graph(self):
        print('Graph:')
        for row in self.adjMatrix:
            print(row)
        print(f'\n')
    
    def create_graph(self):
        for i in range(self.size):
            while True:
                j = random.randint(0,self.size-1)
                if j == i:
                    continue
                if self.adjMatrix[i][j] == 0:
                    self.adjMatrix[i][j] = (random.randint(1,10))
                    self.adjMatrix[j][i] = self.adjMatrix[i][j]
                else:
                    break
    
    def create_min_span_tree(self):
        INF = 9999999
        size = self.size
        t_weight = 0


        mstSet = []
        verticies = [INF for n in range(size)]

        verticies[0] = 0


        # Implementing Prim's algorithm

        for count in range(size):
            low = INF
            for n in range(size):
                if verticies.count(verticies[n]) > 1 and n in mstSet:
                    verticies[n] = INF
                if verticies[n] < low and verticies.index(verticies[n]) not in mstSet:
                    low = verticies[n]

            u = verticies.index(low)
            
            mstSet.append(u)
            # To do: Get the edge to display the proper verticies.
                # G[v2].index(weight)
            if count == 0:
                print('Vertex: 1')
            else:
                weight = self.adjMatrix[mstSet[count]][self.adjMatrix[mstSet[count]].index(low)]
                t_weight += weight
                
                # Add one to make the verticies non-zero digits.
                print(f'Vertex: {mstSet[count] + 1} Edge: {self.adjMatrix[mstSet[count]].index(weight)+1}-{mstSet[count]+1} Weight: {weight}')
                
            for v in range(size):
                if self.adjMatrix[u][v] < verticies[v] and self.adjMatrix[u][v] != 0:
                    verticies[v] = self.adjMatrix[u][v]
        print(f'weight: {t_weight}')

myGraph = Graph(5) # The integer represents the size of the grid
myGraph.create_graph()
myGraph.print_graph()
myGraph.create_min_span_tree()