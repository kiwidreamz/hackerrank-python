#!/bin/python3

import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    all_positive = []
    mini = 1000000000
    sortedd = sorted(arr)
    
    for i in range(len(sortedd)-1):
        difference = sortedd[i+1] - sortedd[i]
        if difference < mini:
            mini = difference
    
    return mini  
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
