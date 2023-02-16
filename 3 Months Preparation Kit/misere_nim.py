#!/bin/python3

import math
import os
import random
import re
import sys

def misereNim(s):
    
    if all(pile == 1 for pile in s):
        nim_sum = 0
        for pile in s:
            nim_sum ^= pile
        return "First" if nim_sum == 0 or all(pile > 1 for pile in s) else "Second"
    
    bitwise = 0
    
    for i in s:
        bitwise = bitwise ^ i
        
    if bitwise != 0:
        return "First"
    else:
        return "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
