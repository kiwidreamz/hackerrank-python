#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    
    my_set = list(set(a))
    print(my_set)
    return 2*sum(my_set)-sum(a)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
