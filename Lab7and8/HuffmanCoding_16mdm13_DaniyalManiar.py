#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:58:05 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. 
The algorithms were based upon the description provided in lecture.

This file has the solution in a non-modified format
"""
# Import the required packages
import heapq
import os

class HuffMan:
    def __init__(self, path): # Initialize the class based on whether a file or directory path is passed
        self.defaultDict() # Make a default printables dictionary 
        if (os.path.isdir(path)): # If directory then read each file to gen Frequency Dictionary
            for file in os.listdir(path):
                self.generateFreqDict(self.readFile(path + file))
        elif (os.path.isfile(path)): # If file then read each file to gen Frequency Dictionary
            self.generateFreqDict(self.readFile(path))
        else: # Incorrect File Path
            print ("Incorrect File path")
            return
        self.genMappings() #Generate Mappings based on frequency of characters
    def defaultDict(self): # Make a default printables dictionary 
        self.symbolFreq = {}
        self.symbolFreq[chr(10)] = 0
        for asciiCode in range(32, 127):
            self.symbolFreq[chr(asciiCode)] = 0
    def generateFreqDict(self, text): # Use text to gen Frequency Dictionary
        for char in text:
            if char in self.symbolFreq:
                self.symbolFreq[char] += 1
    def genMappings(self): # Huffman Algorithm to make mappings using heap
        heap = [[self.symbolFreq[key], [[key, ""]]] for key in self.symbolFreq]
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
    def encode(self, text): # Encode text based upon mappings
        encodedStr = []
        for char in text:
            if char in self.mappings:
                encodedStr.append(self.mappings[char])
        return ''.join(encodedStr)
    def decode(self, encodedText): # Decode text based upon mappings
        decodedText = []
        encodedChar = ""
        for bit in encodedText:
            encodedChar += bit
            if encodedChar in self.reverseMappings:
                decodedText.append(self.reverseMappings[encodedChar])
                encodedChar = ""
        return ''.join(decodedText)
    def readFile(self, filePath): # Read a file
        file = open(filePath, "r")
        return file.read()
    def writeFile(self, text, filePath): # Write a file
        file = open(filePath, "w")
        file.write(text)
        file.close()       

if __name__ == '__main__':
    # Part 1
    pathToFiles = './Part1/'
    FileToGenMappings = "File1"
    FileToEncode = 'File2'
    huffMan = HuffMan(pathToFiles + FileToGenMappings + ".txt")
    huffMan.writeFile(huffMan.encode(huffMan.readFile(pathToFiles + FileToEncode + ".txt")), pathToFiles + FileToEncode + "Encoded.txt")
    huffMan.writeFile(huffMan.decode(huffMan.readFile(pathToFiles + FileToEncode + "Encoded.txt")), pathToFiles + FileToEncode +"Decoded.txt")
    open(pathToFiles+'Part1Mappings.txt', "w").close()
    file = open(pathToFiles+'Part1Mappings.txt', "a")
    for key in huffMan.mappings:
        file.write(key+'\t'+huffMan.mappings[key]+'\n')
    file.close() 
    # Part 2
    pathToFiles = "./Part2/"
    FilesToEncode = ['Data/Earth','Data/Mystery','Data/Myths','Data/Simak','Data/Wodehouse']
    results = [0]*3
    for num in range (1,4):
        DirToGenMappings = "Canonical Collection " + str(num) + "/"
        huffMan = HuffMan(pathToFiles + DirToGenMappings)
        for file in FilesToEncode:
            encodedTxt = huffMan.encode(huffMan.readFile(pathToFiles + file + ".txt"))
            results[num-1] += len(encodedTxt)
            huffMan.writeFile(encodedTxt, pathToFiles + file + str(num) + "Encoded.txt")
            huffMan.writeFile(huffMan.decode(huffMan.readFile(pathToFiles + file + str(num) + "Encoded.txt")), pathToFiles + file + str(num) + "Decoded.txt")
    print("The best Canonical Collection to encode the files with is "+str(results.index(min(results))+1))