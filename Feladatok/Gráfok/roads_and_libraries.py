#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib;

    graf = [[] for _ in range(n + 1)]
    for u, v in cities:
        graf[u].append(v);
        graf[v].append(u);

    def kereses(csomopont, latogatott):
        stack = [csomopont]
        component_size = 0;
        while stack:
            current = stack.pop();
            if not latogatott[current]:
                latogatott[current] = True;
                component_size += 1;
                for szomszed in graf[current]:
                    if not latogatott[szomszed]:
                        stack.append(szomszed);
        return component_size;

    latogatott = [False] * (n + 1)
    fullKoltseg = 0;

    for city in range(1, n + 1):
        if not latogatott[city]:
            component_size = kereses(city, latogatott);
            component_cost = c_lib + (component_size - 1) * c_road;
            fullKoltseg += component_cost;

    return fullKoltseg;



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
