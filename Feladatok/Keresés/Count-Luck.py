#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    n = len(matrix)
    m = len(matrix[0])

    start = None
    cel = None
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 'M':
                start = (x, y)
            elif matrix[x][y] == '*':
                cel = (x, y)
    
    ugrasok = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def joLepes(x, y):
        return 0 <= x < n and 0 <= y < m and matrix[x][y] in ('.', '*')
    

    def bejaras(x, y, visited):
        if (x, y) == cel:
            return 0 

        visited.add((x, y))

        lehetosegek = 0
        for dx, dy in ugrasok:
            nx, ny = x + dx, y + dy
            if joLepes(nx, ny) and (nx, ny) not in visited:
                lehetosegek += 1

        dontesek = 1 if lehetosegek > 1 else 0

        for dx, dy in ugrasok:
            nx, ny = x + dx, y + dy
            if joLepes(nx, ny) and (nx, ny) not in visited:
                dontesek += bejaras(nx, ny, visited)

        return dontesek

    dontesekSzama = bejaras(start[0], start[1], set())
    
    return "Impressed" if dontesekSzama == k else "Oops!"

## 8/4 eset fut le

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
