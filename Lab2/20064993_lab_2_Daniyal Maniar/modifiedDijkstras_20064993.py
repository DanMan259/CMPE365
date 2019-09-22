#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:39:59 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. 
The modified algorithms was based upon the pseudo code provided in the definition of Lab 1.
"""

class graph:
    # This definition of a graph allows to build the network and minimize lookup to each node
    def __init__(self, maxVertex):
        self.maxVertex = maxVertex
        self.vertexs = {}
    def addNode(self, node):
        # This function allows to add a node to network
        self.vertexs[node.name] = node
       
class node:
    # This definition of a node allows to set a name or number for vertex and allow for multiple connections to other nodes
    def __init__(self, name):
        self.name = name
        self.neighbours = []
    def addNeighbours(self, node, dep, arr):
        # This adds a neighbout definition to each node. It includes a departure and arrival time
        self.neighbours.append({"node": node,"departure": dep,"arrival":arr})
        
class dijkstras:

    def __init__(self, graph):
        # This attaches a graph to the algorithm
        self.graph = graph
    def reset(self):
        # This initializes and resets all the required data structures
        self.reached = {}
        self.estimate = {}
        self.candidate = {}
        self.cost = {}
        self.predecessor = {}
        for vertex in self.graph.vertexs:      
            self.reached[vertex] = False
            self.estimate[vertex] = float('inf')
            self.candidate[vertex] = False
            self.cost[vertex] = float('inf')
            self.predecessor[vertex] = None
    def modifiedAlgorithm(self, start, end):
        # This modified algorithm minimizes the time from a starting vertex to destination vertex
        # This algorithm minimizes the arrival time
        self.reset()
        self.cost[start] = 0
        self.reached[start] = True
        for neighbour in self.graph.vertexs[start].neighbours:
            if (self.estimate[neighbour["node"].name] > (neighbour["arrival"])):
                self.estimate[neighbour["node"].name] = neighbour["arrival"]
                self.predecessor[neighbour["node"].name] = {"name":start, "arrival": neighbour["arrival"]}
                self.candidate[neighbour["node"].name] = True
        for _ in range(self.graph.maxVertex):
            best_candidate_estimate = float('inf')
            for vertex in self.graph.vertexs:
                if (self.candidate[vertex] == True) and (self.estimate[vertex] < best_candidate_estimate):
                    v = vertex
                    best_candidate_estimate = self.estimate[vertex]
            self.cost[v] = self.estimate[v]
            self.reached[v] = True
            self.candidate[v] = False
            for neighbour in self.graph.vertexs[v].neighbours:
                if (self.predecessor[v] and (self.predecessor[v]["arrival"] < neighbour["departure"])) or not self.predecessor[v]:
                    if (self.reached[neighbour["node"].name] == False):
                        if (neighbour["arrival"] < self.estimate[neighbour["node"].name]):
                            self.estimate[neighbour["node"].name] = neighbour["arrival"] 
                            self.candidate[neighbour["node"].name] = True
                            self.predecessor[neighbour["node"].name] = {"name":v, "arrival": neighbour["arrival"]}
            if self.reached[end]:
                return self.cost[end]
        return None
    def printSingleOutput(self, startVertex, endingVertex):
        # This prints out the minimal route from a starting to ending vertex. 
        # It uses a predecessor structure to build a route definition.
        self.modifiedAlgorithm(startVertex,endingVertex)
        print ("Optimal route from "+str(startVertex)+" to "+str(endingVertex)+":\n")
        current = endingVertex
        path = []
        while current!= startVertex:
            if not self.predecessor[current]:
                break
            previous = self.predecessor[current]["name"]
            path.append("Fly from "+str(previous)+" to "+str(current)+".")
            current = self.predecessor[current]["name"]
        for i in range(len(path)):
            print(path[len(path)-i-1])
        if not self.predecessor[endingVertex]:
            arrival = "0"
        else:
            arrival = str(self.predecessor[endingVertex]["arrival"])
        print("\nArrive at "+str(endingVertex)+" at time "+arrival+".\n")
    def saveAllOutputs(self):
        # This prints out all of the combinations of starting and ending vertex
        for i in range(self.graph.maxVertex):
            for j in range(self.graph.maxVertex):
                self.printSingleOutput(i,j)

if __name__ == '__main__':
    # Open the file and read the data
    with open("2019_Lab_2_flights_real_data.txt") as f:    
        s = f.read()
        s = s.strip()
        s = s.splitlines()
    # Set the first line to be the size of graph and remove it from the array
    testGraph = graph(int(s.pop(0)))
    # Add all the nodes to the graph
    for i in range(testGraph.maxVertex):
        testGraph.addNode(node(i))
    # Add all the neighbours for each node
    for i in s:
        i = i.split()
        testGraph.vertexs[int(i[0])].addNeighbours(testGraph.vertexs[int(i[1])], int(i[2]), int(i[3]))
    # Initialize the class
    testingAlgo = dijkstras(testGraph)
    # Print Output for test case
    startVertex = 93
    endingVertex = 49
    testingAlgo.printSingleOutput(startVertex,endingVertex)
    #testingAlgo.saveAllOutputs()
    