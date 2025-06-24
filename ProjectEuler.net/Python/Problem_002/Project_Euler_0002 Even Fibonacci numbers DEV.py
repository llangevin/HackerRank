#Project Euler #2: Even Fibonacci numbers
#https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

fib_test = [2,8,34,144,610,10946]
fib_test[0]
fib_test[1]
fib_test[-1]

#Fibonacci Numbers
fib_numbers=[0,1]
fib_even_numbers=[]
last_fib_numbers = fib_numbers[-1] + fib_numbers[-2]
fib_numbers.append(last_fib_numbers)
print(fib_numbers)

N = 10000
#fib_numbers=[0,1]
fib_even_numbers=[]
second_last_fib_numbers = 0
last_fib_numbers = 1
while last_fib_numbers <= N:
    #fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    temp_fib_numbers = last_fib_numbers
    last_fib_numbers += second_last_fib_numbers
    second_last_fib_numbers = temp_fib_numbers
    #print(last_fib_numbers)
    if last_fib_numbers % 2 == 0:
        fib_even_numbers.append(last_fib_numbers)

print(fib_even_numbers)
print(sum(fib_even_numbers))

#List Comprehensions
N=100
fib_to_sum = [num for num in fib_even_numbers if num < N]
print(fib_to_sum)
print(sum(fib_to_sum))

########################
#V1
#Success
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