#!/bin/python3

import math
import os
import random
import re
import sys

def sumXor(n):
    counter = 0
    
    if n == 0:
        return 1
    
    if n > 100:
        result = 1
        while n:
            b = n&1
            n >>= 1
            if b == 0:
                result *= 2
        return result
    
    else:
        for i in range(n):
            if i + n == i ^ n:
                counter += 1
            
    return counter
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
