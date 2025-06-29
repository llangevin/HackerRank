#Project Euler #6: Sum square difference
#https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sfnnn=(n*(n+1)//2)**2
    ssfnnn=(n*(n+1)*((2*n)+1)) // 6
    print(sfnnn - ssfnnn)