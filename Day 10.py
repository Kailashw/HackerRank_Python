#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

# convert to binary
n = bin(n)
# remove first two charcters.
n = n[2:]
# split the input by '0's and all tha tyou are left with is list of 1's 
# and find max len of it
print(max(map(len, n.split('0'))))
