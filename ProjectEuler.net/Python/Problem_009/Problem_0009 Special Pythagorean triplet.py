#Project Euler #9: Special Pythagorean triplet
#https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=truev
#Accepted

#!/bin/python3

import sys

count=0
n_list=[-1] * 3000
for a in range(1,1000):
    for b in range(a, 1500):
        if (a**2+b**2)**0.5 == int((a**2+b**2)**0.5):
            a_b_c=a+b+int((a**2+b**2)**0.5)
            if a_b_c<=3000:
                abc=a * b * (int((a ** 2 + b ** 2) ** 0.5))
                count +=1
                if abc>n_list[a_b_c-1]:
                    n_list[a_b_c-1]=abc

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(n_list[n-1])