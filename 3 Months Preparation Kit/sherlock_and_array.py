#!/bin/python3

import math
import os
import random
import re
import sys

def balancedSums(arr):
        
    left_sum = 0
    right_sum = sum(arr)

    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return "YES"
        left_sum += arr[i]

    return "NO"
    
    # basic version that times out
    """
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return "YES"
        
    return "NO"
    """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
