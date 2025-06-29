#Project Euler #10: Summation of primes
#https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys

number_list=[1,2,3,4]
prime_number_sum=[0,2,5,5]
n=5
sum_prime=5
while n <= 1000000:
    if n%2==0 or n%3==0:
        number_list.append(n)
        prime_number_sum.append(sum_prime)
        number_list.append(n + 1)
        prime_number_sum.append(sum_prime)
        n += 2
    else:
        i=5
        prime=1
        while i*i <= n:
            if n%i==0 or n%(i+2) == 0:
                prime=0
                i=n
                number_list.append(n)
                prime_number_sum.append(sum_prime)
                number_list.append(n + 1)
                prime_number_sum.append(sum_prime)
            i +=6
        if prime==1:
            sum_prime +=n
            number_list.append(n)
            prime_number_sum.append(sum_prime)
            number_list.append(n+1)
            prime_number_sum.append(sum_prime)
        n += 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_number_sum[n-1])