#!/bin/python3

import math
import os
import random
import re
import sys

# My solution only works for 6/9 test cases as I do not implement my own sorting algorithm but use the built-in python sorted() method

def bigSorting(unsorted):
    soorted = []
    result = []

    for i in unsorted:
        soorted.append(int(i))

    done = sorted(soorted)

    for i in done:
        result.append(str(i))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
