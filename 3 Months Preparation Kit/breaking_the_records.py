#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    #print(scores)
    
    lower = 0 
    higher = 0
    
    smallest = scores[0]
    largest = scores[0]
    #print(smallest, largest)
    
    for i in scores:
        print(i)
        if i < smallest:
            lower = lower + 1
            smallest = i
        if i > largest:
            higher = higher + 1
            largest = i
            
    return (higher, lower)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
