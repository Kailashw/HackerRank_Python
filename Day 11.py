#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

def _getCurrentSum(mat,r,c):
    sum = 0
    sum+=mat[r-1][c-1]
    sum+=mat[r-1][c]
    sum+=mat[r-1][c+1]
    sum+=mat[r][c]
    sum+=mat[r+1][c-1]
    sum+=mat[r+1][c]
    sum+=mat[r+1][c+1]
    return sum


max_sum = -63
for i in range(1,5):
    for j in range(1,5):
        current_sum = _getCurrentSum(arr,i,j)
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)


