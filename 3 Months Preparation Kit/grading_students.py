#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    
    new_list = []
    
    for grade in grades:
        if grade < 38:
            new_list.append(grade)
        elif (grade+1) % 5 == 0:
            new_list.append(grade+1)
        elif (grade+2) % 5 == 0:
            new_list.append(grade+2)
        else:
            new_list.append(grade)
            
    return new_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
