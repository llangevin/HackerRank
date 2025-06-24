# Project Euler #1: Multiples of 3 and 5
#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) -1
    sum=0
    N3 = n// 3
    sum += 3*(N3*(1+N3)//2)
    N5 = n// 5
    sum += 5*(N5*(1+N5)//2)
    N15 = n// 15
    sum -= 15*(N15*(1+N15)//2)
    print(sum)
