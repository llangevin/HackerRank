#Project Euler #8: Largest product in a series
#https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys

def gpkcdndn(n,k,num):
    num_text = str(num)
    max_num_prod = 0
    for i in range(0, n - k + 1):
        num_k_prod = 1
        for j in (num_text[i:(i + k)]):
            num_k_prod *= int(j)
        if num_k_prod > max_num_prod:
            max_num_prod = num_k_prod
    return(max_num_prod)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(gpkcdndn(n,k,num))