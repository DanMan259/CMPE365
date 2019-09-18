#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:39:59 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. The modified algorithms was based upon the pseudo code provided for Lab 1:
"""

class graph:
    def __init__(self, maxVertex):
        self.maxVertex = maxVertex
        self.vertexs = {}
    def addNode(self, node):
        self.vertexs[node.name] = node
       
class node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
    def addNeighbours(self, node, dep, arr):
        self.neighbours.append({"node": node,"departure": dep,"arrival":arr})
        
class dijkstras:
    def __init__(self, graph):
        self.graph = graph
        self.reset()
    def reset(self):
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
        self.reset()
        result = self.modifiedAlgorithm(startVertex,endingVertex)
        print ("Optimal route from "+str(startVertex)+" to "+str(endingVertex)+" which costs "+str(result)+" :\n")
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
        events = []
        for i in range(self.graph.maxVertex):
            for j in range(self.graph.maxVertex):
                events.append({"start":i,"end":j})
        resultString = ""
        for event in events:
            startVertex = event["start"]
            endingVertex = event["end"]
            print ("To:" +str(startVertex)+" From: "+str(endingVertex))
            self.reset()
            self.modifiedAlgorithm(startVertex,endingVertex)
            resultString += "Optimal Route from "+str(startVertex)+" to "+str(endingVertex)+"\n"
            current = endingVertex
            path = []
            while current!= startVertex:
                if not self.predecessor[current]:
                    break
                previous = self.predecessor[current]["name"]
                path.append("Fly from "+str(previous)+" to "+str(current)+"\n")
                current = self.predecessor[current]["name"]
            for i in range(len(path)):
                resultString += path[len(path)-i-1]
            if not self.predecessor[endingVertex]:
                arrival = "0"
            else:
                arrival = str(self.predecessor[endingVertex]["arrival"])
            resultString += "Arrive at "+str(endingVertex)+" at time "+arrival+"\n\n"
        text_file = open("TestOutput2.txt", "w")
        text_file.truncate(0)
        text_file.write(resultString)
        text_file.close()


                
if __name__ == '__main__':
    with open("2019_Lab_2_flights_real_data.txt") as f:    
        s = f.read()
        s = s.strip()
        s = s.splitlines()
    #set the first line to be the size of graph
    testGraph = graph(int(s[0]))
    #remove the first line
    vertexs = int(s.pop(0))
    #Add all the nodes to the graph
    for i in range(vertexs):
        testGraph.addNode(node(i))
    #Add all the neighbours for each node
    for i in s:
        i = i.split()
        testGraph.vertexs[int(i[0])].addNeighbours(testGraph.vertexs[int(i[1])], int(i[2]), int(i[3]))
    #Initialize the class
    testingAlgo = dijkstras(testGraph)
    #Print Output for test case
    startVertex = 93
    endingVertex = 49
    testingAlgo.printSingleOutput(startVertex,endingVertex)
    #testingAlgo.saveAllOutputs()
    