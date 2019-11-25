#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:52:27 2019

@author: Daniyal Maniar

I certify that this submission contains my own work. 
The algorithms were based upon the description provided in lecture.
This solution was built in discussed in collaboration with other students, but 
was done individually.
"""

def hashFile(lines):
    # This hashes each line of the fileArray
    return [hash(line) for line in lines]

def LCS (lines1, hash1, lines2, hash2):
    # This creates a matrix that will keep track of the paths as we generate the LCS
    matrix = [[[0, [], []] for _ in lines2] for __ in lines1]
    # This is the modified LCS algorithm that keeps track of the matches as it goes
    for i in range(len(lines1)):
        for j in range(len(lines2)):
            if hash1[i] == hash2[j]: # Check if the hashed output is the same
                if lines1[i] == lines2[j]: # To make sure we have the same line and not a fluke
                    matrix[i][j][0] = matrix[i-1][j-1][0] + 1 # Similar to original algorithm
                    matrix[i][j][1] = matrix[i-1][j-1][1] + [i+1] # Buildup the path for file1
                    matrix[i][j][2] = matrix[i-1][j-1][2] + [j+1] # Buildup the path for file2
            else:
                matrix[i][j][0] = max(matrix[i-1][j][0],matrix[i][j-1][0]) # Similar to original algorithm
                if matrix[i][j][0] == matrix[i-1][j][0]: # This if is to copy over the solution of the previous guy
                    matrix[i][j][1] = matrix[i-1][j][1] 
                    matrix[i][j][2] = matrix[i-1][j][2]
                else:
                    matrix[i][j][1] = matrix[i][j-1][1]
                    matrix[i][j][2] = matrix[i][j-1][2]
    # Returns the final row column of matrix that has the built up path of the commonalities
    return matrix[-1][-1]
                
def printM(flag, fileName1, fileName2, r1, r2):
    if flag == 0: # Matches
        print("Match:\t\t"+ fileName1 + ": "+ r1+"\t\t" +fileName2 +": "+ r2)
    elif flag == 1: # Mismatch
        print("Mismatch:\t"+ fileName1 + ": "+ r1+"\t\t"+ fileName2 +": "+ r2)
    
def diffAlgorithm(fileName1, fileName2):
    # Read the file and split into an array of lines
    f1 = open(fileName1, "r").read().split('\n')
    f2 = open(fileName2, "r").read().split('\n')        
    result = LCS(f1, hashFile(f1), f2, hashFile(f2)) # Get the lcs of the files
    l1 = result[1] # list for file 1
    l2 = result[2] # list for file 2
    r1 = [] # list for range outputs of file 1
    r2 = [] # list for range outputs of file 2
    # This section is to buildup the ranges and consecutively check the next one
    if l1[0] == 1:
        r1.append(l1[0])
    if l2[0] == 1:
        r2.append(l2[0])
 
    # A mismatch exists in the beginning
    if len(r1) == 0 and len(r2) == 0:
        printM(1, fileName1, fileName2, "<1.." + str(l1[0] - 1) + ">", "<1.."
                  + str(l2[0] - 1) + ">")
    elif len(r1) == 0:
        printM(1, fileName1, fileName2, "<1.." + str(l1[0] - 1) + ">", "None")
    elif len(r2) == 0:
        printM(1, fileName1, fileName2, "None", "<1.." + str(l2[0] - 1) + ">")
 
    # Iterate common parts of both files
    for idx in range(1, len(l1) - 1):
        r1.append(l1[idx])  
        r2.append(l2[idx])
 
        if (l1[idx + 1] != l1[idx] + 1) or (l2[idx + 1] != l2[idx] + 1):
            printM(0, fileName1, fileName2, "<" + str(r1[0]) + ".." + str(r1[-1]) + ">", "<" +
                    str(r2[0]) + ".." + str(r2[-1]) + ">")
            # Reset the ranges
            r1.clear()
            r2.clear()
            if (l1[idx + 1] != l1[idx] + 1) and (l2[idx + 1] != l2[idx] + 1):
                # Both files mismatched
                printM(1, fileName1, fileName2, "<" + str(l1[idx] + 1) + ".." +
                           str(l1[idx + 1] - 1) + ">", "<" + str(l2[idx] + 1) + ".." +
                          str(l2[idx + 1] - 1) + ">")
            elif l1[idx + 1] != l1[idx] + 1:
                # Only the first file mismatched
                printM(1, fileName1, fileName2, "<" + str(l1[idx] + 1) + ".." +
                          str(l1[idx + 1] - 1) + ">", "None")
            else:
                # Only the second file mismatched
                printM(1, fileName1, fileName2, "None", "<" + str(l2[idx] + 1) + ".." +
                          str(l2[idx + 1] - 1) + ">")
    r1.append(l1[-1])
    r2.append(l2[-1])
 
    # Last block of matches case
    printM(0, fileName1, fileName2, "<" + str(r1[0]) + ".." + str(r1[-1]) + ">", "<" +
              str(r2[0]) + ".." + str(r2[-1]) + ">")
 
    if l1[-1] != len(f1) and l2[-1] != len(f2):
        # Both files mismatched
        printM(1, fileName1, fileName2, "<" + str(l1[-1] + 1) + ".." +
                  str(len(f1)) + ">", "<" + str(l2[-1] + 1) + ".." +
                  str(len(f2)) + ">")
    elif l1[-1] != len(f1):
        # Only the first file mismatched
        printM(1, fileName1, fileName2, "<" + str(l1[-1] + 1) + ".." +
                  str(len(f1)) + ">", "None")
    elif l2[-1] != len(f2):
        # Only the second file mismatched
        printM(1, fileName1, fileName2, "None", "<" + str(l2[-1] + 1) + ".." +
                  str(len(f2)) + ">")
    
   
if __name__ == '__main__':
    # Take user input and run the file
    file1 = input("Path to file 1:\t")
    file2 = input("Path to file 2:\t")
    diffAlgorithm(file1, file2)

    