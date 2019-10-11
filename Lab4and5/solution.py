#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:24:50 2019

@author: daniyal
"""

def createSet_OBJ(array):
    return {"set": array[:], "sum": sum(array)}

def BFI_Subset_Sum(S, k):
    subsets = []
    subsets.append(createSet_OBJ([]))
    for value in S["set"]:
        newSubsets = []
        for subset in subsets:
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
            if  newSubsets[-1]["sum"] ==  k:
                return True
        subsets += newSubsets
    return False

def BFI_Subset_Sum_Modified(S):
    subsets = []
    subsets.append(createSet_OBJ([]))
    for value in S["set"]:
        newSubsets = []
        for subset in subsets:
            newSubsets.append(createSet_OBJ(subset["set"]+[value]))
        subsets += newSubsets
    return subsets
            
def HS_Subset_Sum(S, k):
    S_left = BFI_Subset_Sum_Modified(createSet_OBJ(S["set"][:len(S)//2]))
    S_right = BFI_Subset_Sum_Modified(createSet_OBJ(S["set"][len(S)//2:]))
    for obj in S_left:
        if obj['sum'] == k:
            return obj['set']
    for obj in S_right:
        if obj['sum'] == k:
            return obj['set']
    S_left.sort(key=lambda x:x["sum"])
    S_right.sort(key=lambda x:x["sum"])
    Pointers = Pair_Sum(S_left, S_right, k)
    if Pointers:
        return S_left[Pointers[0]]["set"]+ S_right[Pointers[1]]["set"]
    return []

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

if __name__ == '__main__':
    # Case 1
    array =  [2,5,9,3,6,8,7,4,5,1]
    print("Use this array:")
    print(array)
    S = createSet_OBJ(array)
    print ("To achieve:")
    k = 16
    print (k)
    if (BFI_Subset_Sum(S, k)):
        result = HS_Subset_Sum(S, k)
    print("Results:")
    print(result)
    print("\n")
    # Case 2
    array =  [2,5,7]
    print("Use this array:")
    print(array)
    S = createSet_OBJ(array)
    print ("To achieve:")
    k = 6
    print (k)
    result = []
    if (BFI_Subset_Sum(S, k)):
        result = HS_Subset_Sum(S, k)
    print("Results")
    print(result)