#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:58:05 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. 
The algorithms were based upon the pseudo code provided in the definition of the Lab.

This file has the solution in a non-modified format
"""

import heapq

class HuffMan:
    def __init__(self, filePath):
        txt = self.readFile(filePath)
        self.genMappings(txt)
    def generateFreqDict(self, text):
        symbolFreq = {}
        symbolFreq[chr(10)] = 0
        for asciiCode in range(32, 127):
            symbolFreq[chr(asciiCode)] = 0            
        for char in text:
            symbolFreq[char] += 1
        return symbolFreq
    def genMappings(self, text):
        symbolFreq = self.generateFreqDict(text)
        heap = [[symbolFreq[key], [[key, ""]]] for key in symbolFreq]
        heapq.heapify(heap)
        while len(heap) > 1:
            lower = heapq.heappop(heap)
            higher = heapq.heappop(heap)
            for charSet in lower[1]:
                charSet[1] = '0' + charSet[1]
            for charSet in higher[1]:
                charSet[1] = '1' + charSet[1]
            heapq.heappush(heap, [lower[0] + higher[0], lower[1] + higher[1]])
        completedMap = heapq.heappop(heap)[1]
        self.mappings = {charPair[0]:charPair[1] for charPair in completedMap}
        self.reverseMappings = {charPair[1]:charPair[0] for charPair in completedMap}
    def encode(self, text):
        encodedStr = []
        for char in text:
            encodedStr.append(self.mappings[char])
        return ''.join(encodedStr)
    def decode(self, encodedText):
        decodedText = []
        encodedChar = ""
        for bit in encodedText:
            encodedChar += bit
            if encodedChar in self.reverseMappings:
                decodedText.append(self.reverseMappings[encodedChar])
                encodedChar = ""
        return ''.join(decodedText)
    def readFile(self, filePath):
        file = open(filePath, "r")
        return file.read()
    def writeFile(self, text, filePath):
        file = open(filePath, "w")
        file.write(text)
        file.close()       

if __name__ == '__main__':
    pathToFiles = './Part1/'
    FileToGenMappings = "File1"
    FileToEncode = 'File2'
    huffMan = HuffMan(pathToFiles + FileToGenMappings + ".txt")
    huffMan.writeFile(huffMan.encode(huffMan.readFile(pathToFiles + FileToEncode + ".txt")), pathToFiles + FileToEncode + "Encoded.txt")
    huffMan.writeFile(huffMan.decode(huffMan.readFile(pathToFiles + FileToEncode + "Encoded.txt")), pathToFiles + FileToEncode +"Decoded.txt")
