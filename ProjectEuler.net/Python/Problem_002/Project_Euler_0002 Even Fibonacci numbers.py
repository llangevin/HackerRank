#Project Euler #2: Even Fibonacci numbers
#https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
#Accepted

#!/bin/python3

import sys

fib_even_numbers=[]
second_last_fib_numbers = 0
last_fib_numbers = 1
while last_fib_numbers <= 40000000000000000:
    temp_fib_numbers = last_fib_numbers
    last_fib_numbers += second_last_fib_numbers
    second_last_fib_numbers = temp_fib_numbers
    if last_fib_numbers % 2 == 0:
        fib_even_numbers.append(last_fib_numbers)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib_to_sum = [num for num in fib_even_numbers if num < n]
    print(sum(fib_to_sum))
