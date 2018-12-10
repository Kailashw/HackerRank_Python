#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

condition_1 = N%2 > 0
condition_2 = 2<=N<=5
condition_3 = 6<=N<=20
condition_4 = N>20

if condition_1:
    print('Weird')
else:
    if condition_2:
        print('Not Weird')
    elif condition_3:
        print('Weird')
    else:
        print('Not Weird')


