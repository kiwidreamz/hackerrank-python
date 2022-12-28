#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    a = [0] * 200000
    
    for i in range(len(arr)):
        bird = arr[i]
        a[bird] = a[bird] + 1
    
    index_max = max(range(len(a)), key=a.__getitem__)
    
    return index_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
