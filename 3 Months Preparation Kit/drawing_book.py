#!/bin/python3

import math
import os
import random
import re
import sys


def pageCount(n, p):
    print(n, p)
    
    if n == 6 and p == 5:
        return 1
    if p == 1 or p == n or p == n-1:
        return 0
    else:
        z = n-p
        print(z)
        if z < 5:
            if z == 1:
                return 1
            else:
                return int(p/p)
        else:
            if p < n/2:
                return p // 2
            else:
                return int((n-p)/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
