#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    primary = 0
    secondary = 0
    
    for i in range(len(arr)):
        primary = primary + arr[i][i]
            
    for j in range(len(arr)):
        secondary = secondary + arr[j][len(arr)-j-1]
        
    return abs(primary - secondary)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
