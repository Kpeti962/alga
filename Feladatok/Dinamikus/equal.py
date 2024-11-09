#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    minimum_csoki = min(arr)
    
    rounds = float('inf')
    
    
    for target in range(minimum_csoki, minimum_csoki - 5, -1):
        operations = 0
        
      
        for csoki in arr:
            diff = csoki - target
            if diff > 0:
                operations += diff // 5 + (diff % 5) // 2 + (diff % 5) % 2
        
       
        rounds = min(rounds, operations)
    return rounds


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

## lefutott