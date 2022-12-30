#!/bin/python3

import math
import os
import random
import re
import sys


def maximumPerimeterTriangle(sticks):
    triangles = []
    max_sum = 0
    ordered_max = []
    
    for i in range(len(sticks)-2):
        for j in range(1, (len(sticks)-1)):
            for k in range(2, (len(sticks))):
                if i != j and j != k and i != k:
                    a = sticks[i]
                    b = sticks[j]
                    c = sticks[k]
                                
                    if a + b > c and b + c > a and c + a > b:
                        triangles.append([a, b, c])
            
    if not triangles:
        return [-1]
            
    for triangle in triangles:
        t_sum = triangle[0] + triangle[1] + triangle[2]
        if t_sum > max_sum:
            max_sum = t_sum
            max_triangle = triangle[0], triangle[1], triangle[2]
    
    sorted_triangle = tuple(sorted(max_triangle))  
    
    return sorted_triangle
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
