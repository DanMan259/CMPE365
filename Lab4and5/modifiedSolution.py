#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:45:39 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. 
The algorithms were based upon the pseudo code provided in the definition of the Lab.

This file reflects the same algorithms but they are modified to count operations instead of results. 
This will require matplotlib to be installed

"""

import random
import math
# Change this line to zero if you dont have matplotlib to plot the results
PLOT = 1

def createSet_OBJ(array):
    return {"set": array[:], "sum": sum(array)}

def BFI_Subset_Sum(S, k):
    count = 0
    subsets = []
    subsets.append(createSet_OBJ([]))
    for value in S["set"]:
        newSubsets = []
        for subset in subsets:
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
            count += 1
            if newSubsets[-1]["sum"] ==  k:
                return count
        subsets += newSubsets
        count += 1
    return count

def BFI_Subset_Sum_Modified(S):
    subsets = []
    subsets.append(createSet_OBJ([]))
    for value in S["set"]:
        newSubsets = []
        for subset in subsets:
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
        subsets += newSubsets
    return subsets

def BFI_Subset_Sum_Modified_Count(S):
    count = 0
    subsets = []
    subsets.append(createSet_OBJ([]))
    for value in S["set"]:
        newSubsets = []
        for subset in subsets:
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
            count += 1
        subsets += newSubsets
        count += 1
    return count

def HS_Subset_Sum(S, k):
    count = 0
    S_left = BFI_Subset_Sum_Modified(createSet_OBJ(S["set"][:len(S["set"])//2]))
    count += 1
    count += BFI_Subset_Sum_Modified_Count(createSet_OBJ(S["set"][:len(S["set"])//2]))
    S_right = BFI_Subset_Sum_Modified(createSet_OBJ(S["set"][len(S["set"])//2:]))
    count += 1
    count += BFI_Subset_Sum_Modified_Count(createSet_OBJ(S["set"][len(S["set"])//2:]))
    for obj in S_left:
        count += 1
        if obj['sum'] == k:
            return count
    for obj in S_right:
        count += 1
        if obj['sum'] == k:
            return count
    S_left.sort(key=lambda x:x["sum"])
    count += 3 * len(S_left) * math.log2(len(S_left))
    S_right.sort(key=lambda x:x["sum"])
    count += 3 * len(S_right) * math.log2(len(S_right))
    Pointers = Pair_Sum(S_left, S_right, k)
    count += Pair_Sum_Count(S_left, S_right, k)
    if Pointers:
        return count
    return count

def Pair_Sum(Values_1, Values_2, k):
    p1 = 1 
    p2 = len(Values_2)-1
    while (p1 < len(Values_1) and p2 >= 0):
        t = Values_1[p1]["sum"]+Values_2[p2]["sum"]
        if (t==k):
            return (p1,p2)
        elif t < k:
            p1 += 1
        else:
            p2 -= 1
    return ()

def Pair_Sum_Count(Values_1, Values_2, k):
    count = 0
    p1 = 1 
    p2 = len(Values_2)-1
    while (p1 < len(Values_1) and p2 >= 0):
        t = Values_1[p1]["sum"]+Values_2[p2]["sum"]
        count += 2
        if (t==k):
            return count
        elif t < k:
            p1 += 1
        else:
            p2 -= 1
    return count

if __name__ == '__main__':
    # This section calculates the averages
    bfiSetAverages= []
    hsSetAverages= []
    for n in range(4, 16):
        bfNAverage = 0
        hsNAverage = 0
        for _ in range (1, 21):
            S = createSet_OBJ([random.randint(1, 1000) for __ in range(n)])
            kSet = [random.randint(500, 1500) for __ in range(20)]
            bfTSum = 0
            hsTSum = 0
            for k in kSet:
                bfTSum += BFI_Subset_Sum(S, k)
                hsTSum += HS_Subset_Sum(S, k)   
            bfNAverage += bfTSum / len(kSet)
            hsNAverage += hsTSum / len(kSet)
        bfiSetAverages.append(bfNAverage/n)
        hsSetAverages.append(hsNAverage/n)
    
    # This section plots the results
    if PLOT:
        import matplotlib.pyplot as plt
        x_axis = list(range(4, 16)) 
        plt.plot(x_axis, bfiSetAverages, label="BFI")
        plt.plot(x_axis, list(map(lambda n: 2 ** n, x_axis)), label="2^n")
        plt.plot(x_axis, hsSetAverages, label="Horowitz Sahni") 
        plt.plot(x_axis, list(map(lambda n: 5*n * (2 ** (n / 2)), x_axis)), label="5*n*2^(n/2)") 
        plt.legend()
        plt.xlabel('Sets')
        plt.ylabel('Number of Operations') 
        plt.title('Subset Sum algorithm analysis') 
        plt.show()
