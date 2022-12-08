#!/bin/python3

import math
import os
import random
import re
import sys


def flippingMatrix(matrix):
    
    m = len(matrix)
    n = m // 2
    result = 0
    
    for i in range(n):
        for j in range(n):
            first = matrix[i][j]
            second = matrix[i][m-j-1]
            third = matrix[m-i-1][m-j-1]
            fourth = matrix[m-i-1][j]
            maximum = max(first, second, third, fourth)
            
            result += maximum
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    q = int(input().strip())
    
    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
