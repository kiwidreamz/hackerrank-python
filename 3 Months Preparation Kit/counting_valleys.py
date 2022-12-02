#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    
    counter = 0
    entering = False
    valleys = 0
    
    for i in range(steps):
        if path[i] == "U":
            counter +=1
        elif path[i] == "D":
            counter -=1
        
        if counter < 0:
            entering = True
        
        if counter == 0 and entering == True:
            valleys += 1
            entering = False
    
    return valleys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
