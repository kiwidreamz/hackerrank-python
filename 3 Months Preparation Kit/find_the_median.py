#!/bin/python3

import math
import os
import random
import re
import sys


def findMedian(arr):
    arr2 = sorted(arr)
    middle = (len(arr) // 2) 
    
    median = arr2[middle]
    return median
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
