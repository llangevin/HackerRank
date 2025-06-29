# Project Euler #5: Smallest multiple
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys

ppcm_list=[1,2]
for n in range(3, 41):
    ppcm = n * (n - 1)
    i = n - 2
    while i >= 1:
        if ppcm % i != 0:
            ppcm_increment = ppcm
            while ppcm % i != 0:
                ppcm += ppcm_increment
        i -= 1
    ppcm_list.append(ppcm)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(ppcm_list[n-1])