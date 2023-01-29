#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    
    for i in arr:
        if i in brr:
            brr.remove(i)
    return sorted(list(set(brr)))
    
    
    # First solution that worked for all cases except 3
    """
    a = sorted(arr)
    b = sorted(brr)
    result = []
    
    minimum = min(len(a), len(b))
    
    while len(a) > 0:
        try:
            if a[0] == b[0]:
                b.pop(0)
                a.pop(0)
            else:
                result.append(b[0])
                b.pop(0)
        except IndexError:
            pass
        
    final = list(dict.fromkeys(result))
            
    return final
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
