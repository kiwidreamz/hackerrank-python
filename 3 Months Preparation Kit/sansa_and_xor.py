#!/bin/python3

import math
import os
import random
import re
import sys

def sansaXor(arr):
    result = 0
    
    if not len(arr)%2:
        return 0
        
    for i in range(0, len(arr), 2):
        result ^= arr[i]
        
    return result
    
    # brute force mething that times out
    """
    n = len(arr)
    result = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= arr[j]
            result ^= xor
    return result
    """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
