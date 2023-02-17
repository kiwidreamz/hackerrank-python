#!/bin/python3

import math
import os
import random
import re
import sys

def gamingArray(arr):
    
    peak = 0
    bob = False

    for a in arr:
        if a > peak:
            bob = not bob
            peak = a
            
    return 'BOB' if bob else 'ANDY'
    
    # my solution that times out for 4 tests
    """
    counter = 0
    
    while arr:
        max_index = arr.index(max(arr))
        arr = arr[:max_index]
        counter += 1

    if counter % 2 == 0:
        return "ANDY"
    else:
        return "BOB"
    """
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
