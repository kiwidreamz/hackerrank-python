#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    negative_count = 0
    positive_count = 0
    zeros_count = 0
    
    for i in arr:
        if i < 0:
            negative_count +=1
        elif i > 0:
            positive_count +=1
        else:
            zeros_count +=1
    
    positive = positive_count / n
    negative = negative_count / n
    zeros = zeros_count / n
    
    
    print("{:.6f}".format(positive))
    print("{:.6f}".format(negative))
    print("{:.6f}".format(zeros))

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)