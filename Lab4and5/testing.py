#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:45:39 2019

@author: daniyal
"""
import matplotlib.pyplot as plt
import random
import math

def createSet_OBJ(array):
    return {"set": array, "sum": sum(array)}

def BFI_Subset_Sum(S, k):
    count = 0
    subsets = []
    subsets.append(createSet_OBJ([]))
    count += 2
    for value in S["set"]:
        count += 1
        newSubsets = []
        for subset in subsets:
            count += 1
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
            count += 2
            if newSubsets[-1]["sum"] ==  k:
                count += 1 
                return count
            count += 1
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
    count += 2
    for value in S["set"]:
        count += 1
        newSubsets = []
        for subset in subsets:
            count += 1
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
            count += 2
        subsets += newSubsets
        count += 1
    return count

def HS_Subset_Sum(S, k):
    count = 0
    S_left = BFI_Subset_Sum_Modified(createSet_OBJ(S["set"][:len(S)//2]))
    count += 2
    count += BFI_Subset_Sum_Modified_Count(createSet_OBJ(S["set"][:len(S)//2]))
    S_right = BFI_Subset_Sum_Modified(createSet_OBJ(S["set"][len(S)//2:]))
    count += 2
    count += BFI_Subset_Sum_Modified_Count(createSet_OBJ(S["set"][len(S)//2:]))
    for obj in S_left:
        count += 2
        if obj['sum'] == k:
            count += 1
            return count
    for obj in S_right:
        count += 2
        if obj['sum'] == k:
            count += 1
            return count
    S_left.sort(key=lambda x:x["sum"])
    count += 3 * len(S_left) * math.log2(len(S_left))
    S_right.sort(key=lambda x:x["sum"])
    count += 3 * len(S_right) * math.log2(len(S_right))
    Pointers = Pair_Sum(S_left, S_right, k)
    count += Pair_Sum_Count(S_left, S_right, k)
    if Pointers:
        count += 1
        return count
    count += 1
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
        count += 1
        if (t==k):
            count += 1
            return count
        elif t < k:
            p1 += 1
        else:
            p2 -= 1
        count += 2
    return count

if __name__ == '__main__':
    bfiSetAverages= []
    hsSetAverages= []
    for n in range(4, 16):
        bfssAverage = 0
        hsssAverage = 0
        for i in range (1, 21):
            array = [random.randint(1, 300) for _ in range(n)]
            S = createSet_OBJ(array)
            kSet = [random.randint(1, 700) for _ in range(10)]
            bfssSum = 0
            hsssSum = 0
            for k in kSet:
                bfssSum += BFI_Subset_Sum(S, k)
                hsssSum += HS_Subset_Sum(S, k)   
            bfssAverage += bfssSum / len(kSet)
            hsssAverage += hsssSum / len(kSet)
        bfiSetAverages.append(bfssAverage/n)
        hsSetAverages.append(hsssAverage/n)
    
    
    
    # X axis values
    x = list(range(4, 16)) 
    # plotting the points
    plt.plot(x, bfiSetAverages, label="BFI")
    plt.plot(x, hsSetAverages, label="Horowitz Sahni") 
    # plot the mathematical models to compare with
    plt.plot(x, list(map(lambda n: 2 ** n, x)), label="2^n")
    plt.plot(x, list(map(lambda n: n * (2 ** (n // 2)), x)), label="n*2^(n/2)") 
    # display the legend
    plt.legend()
    # naming the x axis
    plt.xlabel('Sets')
    # naming the y axis
    plt.ylabel('Number of Operations') 
    # giving a title to my graph
    plt.title('Subset Sum algorithm analysis') 
    # function to show the plot
    plt.show()
