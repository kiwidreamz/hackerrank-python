#!/bin/python3

import math
import os
import random
import re
import sys

def gridChallenge(grid):
    new = []
    trial = []
    
    for i in grid:
        j = ''.join(sorted(i))
        new.append(j)
    print(new)
    
    for k in range(len(new[0])):
        bud = []
        for l in range(len(new)):
            bud.append(new[l][k])
        trial.append(''.join(bud))
    
    for z in trial:
        y = ''.join(sorted(z))
        if z != y:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
