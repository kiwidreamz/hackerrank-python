#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    
    if len(s) == 1:
        if s[0] == d:
            return 1
        else:
            return 0
        
    result = 0
    
    try:
        for i in range(len(s)-1):
            batch = 0
            
            for j in range(m):
                batch = batch + s[i+j]
                
            if batch == d:
                result = result +1
    except IndexError: 
        return result
            
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
