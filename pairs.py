#!/bin/python3

import math
import os
import random
import re
import sys

def pairs(k, arr):
    counter = 0
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        if num + k in freq:
            counter += freq[num]
            
    # Works but solves 13/17 cases (times out)
    """
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] - arr[i] == k:
                counter +=1
    """
                
    return counter
	
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
