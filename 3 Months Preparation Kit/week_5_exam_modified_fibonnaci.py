#!/bin/python3

import math
import os
import random
import re
import sys


def fibonacciModified(t1, t2, n):
    
    for i in range(n-2):
        temp = t1 + (t2*t2)
        t1 = t2
        t2 = temp

    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
