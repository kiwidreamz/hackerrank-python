#!/bin/python3

import math
import os
import random
import re
import sys

def maxMin(k, arr):
    result = 1000000000
    s = sorted(arr)
    sk = len(arr)-k+1
    
    for j in range(sk):
        difference = s[j+k-1] - s[j]
        if difference < result:
            result = difference
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
