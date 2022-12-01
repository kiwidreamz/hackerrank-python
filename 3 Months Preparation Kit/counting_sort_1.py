#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    
    list_of_zeros = [0] * 100
    
    for value in arr:
        list_of_zeros[value] = int(list_of_zeros[value]) +1
        
    return list_of_zeros

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
