#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:03:37 2019

@author: Daniyal Maniar
"""

class graph:
    def __init__(self, maxVertex):
        self.maxVertex = maxVertex
        self.vertexs = {}
        self.head = None
    def setHead(self, node):
        self.head = node
        self.vertexs[node.name] = node
    def addNode(self, node):
        self.vertexs[node.name] = node
        
class node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
    def addNeighbours(self, node, weight):
        self.neighbours.append({"node": node,"weight": weight})
        
class dijkstras:
    def __init__(self, graph):
        self.graph = graph
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
    def algorithm(self):
        self.cost[self.graph.head.name] = 0
        self.reached[self.graph.head.name] = True
        for neighbour in self.graph.head.neighbours:
            self.estimate[neighbour["node"].name] = neighbour["weight"]
            self.candidate[neighbour["node"].name] = True
        while not self.allReached():
            best_candidate_estimate = float('inf')
            for vertex in self.graph.vertexs:
                if (self.candidate[vertex] == True) and (self.estimate[vertex] < best_candidate_estimate):
                    v = vertex
                    best_candidate_estimate = self.estimate[vertex]
            self.cost[v] = self.estimate[v]
            self.reached[v] = True
            self.candidate[v] = False
            for neighbour in self.graph.vertexs[v].neighbours:
                if (neighbour["weight"] > 0) and (self.reached[neighbour["node"].name] == False):
                    if ((self.cost[v] + neighbour["weight"]) < self.estimate[neighbour["node"].name]):
                        self.estimate[neighbour["node"].name] = self.cost[v] + neighbour["weight"]
                        self.candidate[neighbour["node"].name] = True
                        self.predecessor[neighbour["node"].name] = v
    def allReached(self):
        for i in self.reached:
            if not self.reached[i]:
                return False
        return True
    def highestCost(self):
        self.algorithm()
        max = {}
        for i in self.cost:
            if (not max) or (max["cost"] < self.cost[i]):
                max["vertex"] = i
                max["cost"] = self.cost[i]
        return max
    
    
if __name__ == '__main__':
    #Get resuls for each test file
    testFiles = ["Dijkstra_Data_6.txt", "Dijkstra_Data_100.txt", "Dijkstra_Data_200.txt", "Dijkstra_Data_400.txt","Dijkstra_Data_800.txt","Dijkstra_Data_1600.txt"]
    for file in testFiles:
        with open(file) as f:    
            s = f.read()
            s = s.strip()
            s = s.splitlines()
        #set the first line to be the size of graph
        testGraph = graph(int(s[0]))
        #remove the first line
        vertexs = int(s.pop(0))
        #Add all the nodes to the graph
        for i in range(vertexs):
            if i == 0:
                head = node(i)
                testGraph.setHead(head)
                testGraph.addNode(head)
            else:
                testGraph.addNode(node(i))
        #Add all the neighbours for each node
        for fromVertex, val in enumerate(s):
            val = val.split()
            for toVertex, weight in enumerate(val):        
                if weight != '0':
                    testGraph.vertexs[int(fromVertex)].addNeighbours(testGraph.vertexs[int(toVertex)], int(weight))
        #Initialize the class
        testingAlgo = dijkstras(testGraph)
        #Get the highest cost for the test case
        result = testingAlgo.highestCost()
        print ("For "+file+" the furthest vertex from vertex 0 is vertex "+str(result["vertex"])+" which has a cost of "+str(result["cost"])+".")
    