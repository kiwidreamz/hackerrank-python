#!/bin/python3

import math
import os
import random
import re
import sys

def palindromeIndex(s):
    # Only gets 12 out of 15 correct
    if s == s[::-1]:
        return -1
    
    for i in range(len(s)):
        new = s[:i] + s[i+1:]
        if new == new[::-1]:
            return i
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
