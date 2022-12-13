#!/bin/python3

import math
import os
import random
import re
import sys

def check(k, A, B):
    for i in range(len(A)):
        if A[i] + B[i] >= k:
            pass
        else:
            return False
    return True

def twoArrays(k, A, B):

    initial = check(k, A, B)
    if initial:
        return "YES"
   
    sorted_a = sorted(A)
    sorted_b = sorted(B, reverse=True)
    
    for i in range(len(A)):
        if sorted_a[i] + sorted_b[i] < k:
            return "NO"
        
    return "YES"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
