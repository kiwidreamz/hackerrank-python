#!/bin/python3

import math
import os
import random
import re
import sys

def getSum(n):
    summ = 0
    for i in range(len(n)):
        summ = summ + n[i]
    n = [int(x) for x in str(summ)]
    return n

def superDigit(n, k):
    digit_sum = 0
    for c in n:
        digit_sum = (digit_sum + int(c)) % 9
    digit_sum = (digit_sum * k) % 9
    return digit_sum if digit_sum != 0 else 9
    
    # Initial correct version that uses too much memory
    """
    n = [int(x) for x in n] * k
    
    while len(n) > 1:
        n = getSum(n)
        
    return n[0]
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
