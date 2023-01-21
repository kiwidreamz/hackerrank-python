#!/bin/python3

import math
import os
import random
import re
import sys

def anagram(s):
    counter = 0
    
    if len(s)%2 == 1:
        return -1
    
    length = int(len(s)/2)
    first = sorted(s[0:length])
    second = sorted(s[length:])
    
    if first == second:
        return 0
    
    unique_chars = list(set(second))
    
    for c in unique_chars:
        counter += max(second.count(c) - first.count(c), 0)
        
    """
    try:
        for i in range(length):
            for j in range(length):
                if first[i] == second[j]:
                    first = first[:i] + first[(i+1):]
                    second = second[:j] + second[(j+1):]
                    i = i - 1
                    j = j - 1

    except IndexError:
        pass
        
    try:
        for i in range(length):
            if first[i] != second[i]:
                counter = counter +1
    except:
        IndexError          
    #print("'end'", first, second)
    
    if counter:
        return counter
    else:
        return 0
    """

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
