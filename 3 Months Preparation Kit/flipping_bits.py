#!/bin/python3

import math
import os
import random
import re
import sys


def flippingBits(n):
    
    return 4294967295 - n
    
    """
    binary = '{:032b}'.format(n)

    b_list = [int(x) for x in binary]
    new_list = []
    
    for i in b_list:
        if i == 0:
            new_list.append(1)
        else:
            new_list.append(0)
            
    s = [str(integer) for integer in new_list]
    res = "".join(s)
    print(int(res))
    
    return int(res)
    """
          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
