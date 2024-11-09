#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stoneDivision' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER_ARRAY s
#

def stoneDivision(n, s):
    memo = {};

    def max_rakod(halmaz_meret):
 
        if halmaz_meret in memo:
            return memo[halmaz_meret];
        

        max_rakod_szam = 0;
        
      
        for x in s:
            if halmaz_meret % x == 0 and x < halmaz_meret:
                halmaz_szam = halmaz_meret // x;
                moves = halmaz_szam * max_rakod(x) + 1;
                max_rakod_szam = max(max_rakod_szam, moves);
        
        memo[halmaz_meret] = max_rakod_szam;
        return max_rakod_szam;

    return max_rakod(n);



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s)

        fptr.write(str(result) + '\n')

    fptr.close()
