#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    res = ""
    upper = True
    for i in range(len(s)):
        if(s[i]==" "):
            upper = True
        if(upper and s[i]!=" "):
            res +=s[i].upper()
            upper = False
        else:
            res += s[i]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()