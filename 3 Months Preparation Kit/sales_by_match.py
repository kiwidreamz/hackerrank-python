#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    
    pairs = 0
    
    for i in range(n):
        for j in range(1, n):
            if ar[i] == ar[j] and ar[i]>0 and ar[j]>0 and i != j:
                ar[i] = 0
                ar[j] = 0
                pairs +=1
                
    return pairs
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
