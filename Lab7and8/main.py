#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:58:05 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. 
The algorithms were based upon the pseudo code provided in the definition of the Lab.

This file has the solution in a non-modified format
"""

import collections
import heapq

class HuffMan:
    def __init__(self, txt):
        self.genMappings(txt)
    def genMappings(self, txt):
        symbolFreq = collections.defaultdict(int)
        for char in txt:
            symbolFreq[char] += 1
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
    def encode(self, txt):
        encodedStr = []
        for char in txt:
            encodedStr.append(self.mappings[char])
        return ''.join(encodedStr)
    def decode(self, encodedTxt):
        decodedTxt = []
        encodedChar = ""
        for bit in encodedTxt:
            encodedChar += bit
            if encodedChar in self.reverseMappings:
                decodedTxt.append(self.reverseMappings[encodedChar])
                encodedChar = ""
        return ''.join(decodedTxt)


if __name__ == '__main__':
    txt = "I love to test!"
    huffman = HuffMan(txt)
    encodedTxt = huffman.encode(txt)
    decodedTxt = huffman.decode(encodedTxt)
    print("Original: " + txt)
    print("Encoded Text: " + encodedTxt)
    print("Decoded Text: " + decodedTxt)
    print ("Is the decoded same as the original: "+str(txt == decodedTxt))
