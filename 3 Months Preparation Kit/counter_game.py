#!/bin/python3

import math
import os
import random
import re
import sys

def isPower(n):
    return n & (n - 1) == 0
    
def findLower(n):
    return 2**(n.bit_length() - 1)

def counterGame(n):
    counter = 0
    
    while n > 1:
        if isPower(n):
            n = n // 2
            counter += 1
        else:
            n = n - findLower(n)
            counter += 1
    
    if counter % 2 == 0:
        return "Richard"
    else:
        return "Louise"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
