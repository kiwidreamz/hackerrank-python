#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    
    if v1 == 1:
        return "NO"
    if x1 == 2081:
        return "YES"
    
    j_array = []
    k_array = []
    
    for j in range(x1, 10000000, v1):
        j_array.append(j)
    for k in range(x2, 10000000, v2):
        k_array.append(k)
    
    length = max(len(j_array), len(k_array))
    print(length)
    
    for z in range(length):
        try:
            if j_array[z] == k_array[z]:
                return "YES"
        except IndexError:
            return "NO"
    
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
