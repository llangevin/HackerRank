#Project Euler #3: Largest prime factor
#https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys
import math

N=1000000
potential=[]
for i in range(25,N+1,2):
    if i % 2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0:
        potential.append(i)

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for i in potential:
    sqrt=int(math.sqrt(i))
    j=5
    prime_ind=1
    while j <= sqrt:
        if i%j==0 or i%(j+2)==0:
            prime_ind=0
            break
        else: j +=6
    if prime_ind == 1:
        prime_numbers.append(i)

def mine_lpf(n):
    if n<=1000000:
        if n not in prime_numbers:
            prime_factors_potential = [num for num in prime_numbers if num <= n//2]
            index = len(prime_factors_potential) - 1
            while index >= 0:
                if n % prime_factors_potential[index] == 0:
                    return prime_factors_potential[index]
                    index = -1
                else:
                    index -= 1
        else:
            return n
    else:
        prime_factors=[]
        i=0
        nn=n
        while prime_numbers[i]!=prime_numbers[-1]:
            if nn%prime_numbers[i]==0:
                prime_factors.append(prime_numbers[i])
                nn=nn//prime_numbers[i]
            else:
                i+=1
        if nn==1:
            return max(prime_factors)
        elif n!=nn:
            return nn
        else: #prime number
            return n

t = int(input().strip())
for a0 in range(t):
    numm = int(input().strip())
    print(mine_lpf(numm))
