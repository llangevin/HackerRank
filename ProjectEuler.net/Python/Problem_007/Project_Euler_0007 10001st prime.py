#Project Euler #7: 10001st prime
#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys

prime_number_list=[2,3]
n=5
while len(prime_number_list)<10000:
    if n%2==0 or n%3==0:
        n += 2
    else:
        i=5
        prime=1
        while i*i <= n:
            if n%i==0 or n%(i+2) == 0:
                prime=0
                i=n
            i +=6
        if prime==1:
            prime_number_list.append(n)
        n += 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_number_list[n-1])