#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    
    counter = 0
    chunks = [s[i:i+3] for i in range(0, len(s), 3)]
    
    for triple in chunks:
        if triple[0] == "S":
            pass
        else:
            counter +=1
                
        if triple[1] == "O":
            pass
        else:
            counter +=1
        
        if triple[2] == "S":
            pass
        else:
            counter +=1
        
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
