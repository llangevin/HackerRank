#Project Euler #3: Largest prime factor
#https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true

import sys
import math
#from math import sqrt
#print(int(sqrt(49)))

#list of prime numbers
prime_numbers = [2]
for x in range(3, 1000, 2):
    for y in range(2,(int(math.sqrt(x)) +1)+1):
        if x % y == 0 and x != y:
                break
        elif int(math.sqrt(x)) +1 == y:
            prime_numbers.append(x)

print(prime_numbers)
print(len(prime_numbers))


n=24
if n in prime_numbers:
    print(n)
else:
    prime_factors_potential = [num for num in prime_numbers if num <= n//2]
    print(prime_factors_potential)
    index = len(prime_factors_potential) - 1
    while index > 0:
        if n % prime_factors_potential[index] == 0:
            print(prime_factors_potential[index])
            index = 0
        else:
            index -= 1

#V1
#list of prime numbers
prime_numbers = [2]
for x in range(3, 100000, 2):
    for y in range(2,(int(math.sqrt(x)) +1)+1):
        if x % y == 0 and x != y:
                break
        elif int(math.sqrt(x)) +1 == y:
            prime_numbers.append(x)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n in prime_numbers:
        print(n)
    else:
        prime_factors_potential = [num for num in prime_numbers if num <= n//2]
        index = len(prime_factors_potential) - 1
        while index > 0:
            if n % prime_factors_potential[index] == 0:
                print(prime_factors_potential[index])
                index = 0
            else:
                index -= 1

##############
#
#25,35,49
#list of prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13]
for x in range(17, 20, 2):
    print(f"x= {x}")
    if x % 2 != 0:
        for y in range(3,int(math.sqrt(x))+1):
            print(f"y= {y}")
            if x % y == 0 and x != y:
                    break
            elif int(math.sqrt(x))  == y:
                prime_numbers.append(x)

print(prime_numbers)
print(len(prime_numbers))

for i in range(3,6,2):
    print(i)

#Trial Division Method:
x=17
print(f"x: {x}")
sqrt=int(math.sqrt(x)) + 1*(int(math.sqrt(x)) % 2 != 0)
print(f"sqrt: {sqrt}")
if x % 2 !=0 and x % 5 !=0:
    for y in range(3,sqrt,2):
        last_value = list(range(3,sqrt,2))[-1]
        print(f"last_value: {last_value}")
        print(f"y: {y}")
        if x % y == 0 and x != y:
            print("break")
            break
        elif last_value  == y:
            print(f"prime number: {x}")

x=37
print(f"x: {x}")
sqrt=int(math.sqrt(x)) + 1*(int(math.sqrt(x)) % 2 != 0)
print(f"sqrt: {sqrt}")
if x % 2 !=0 and x % 5 !=0:
    for y in range(3,sqrt,2):
        last_value = list(range(3,sqrt,2))[-1]
        print(f"last_value: {last_value}")
        print(f"y: {y}")
        if x % y == 0 and x != y:
            print("break")
            break
        elif last_value  == y:
            print(f"prime number: {x}")

prime_numbers = [2, 3, 5, 7, 11, 13]
for x in range(17, 100, 2):
    sqrt=int(math.sqrt(x)) + 1*(int(math.sqrt(x)) % 2 != 0)
    if x % 2 !=0 and x % 5 !=0:
        for y in range(3,sqrt,2):
            last_value = list(range(3,sqrt,2))[-1]
            if x % y == 0 and x != y:
                break
            elif last_value  == y:
                prime_numbers.append(x)

print(prime_numbers)
print(len(prime_numbers))

#sum of digits
number=12345
for digit in str(number):
    print(digit)

number //= 10
print(number)

#the sum of digits of a number
def sum_digits_iterative(number):
    digit_sum = 0
    while number > 0:
        digit = number % 10  # Extract the last digit
        digit_sum += digit   # Add to the sum
        number //= 10        # Remove the last digit (integer division)
    return digit_sum

prime_numbers = [2, 3, 5, 7, 11, 13]
for x in range(17, 100, 2):
    sqrt=int(math.sqrt(x)) + 1*(int(math.sqrt(x)) % 2 != 0)
    if x % 2 !=0 and x % 5 !=0 and sum_digits_iterative != 3:
        for y in range(3,sqrt,2):
            last_value = list(range(3,sqrt,2))[-1]
            if x % y == 0 and x != y:
                break
            elif last_value  == y:
                prime_numbers.append(x)

print(prime_numbers)
print(len(prime_numbers))

x=1701117049
if x % 2 !=0 and x % 5 !=0 and sum_digits_iterative(x) != 3:
    sqrt=int(math.sqrt(x)) + 1*(int(math.sqrt(x)) % 2 != 0)
    for y in range(3,sqrt,2):
        last_value = list(range(3,sqrt,2))[-1]
        if x % y == 0 and x != y:
            break
        elif last_value  == y:
             print(f"prime number: {x}")

#Define function to determine if a number >= 10 is prime or not
def prime_number(x):
    if x % 2 !=0 and x % 5 !=0 and sum_digits_iterative(x) != 3:
        sqrt_x=int(math.sqrt(x)) + 1*(int(math.sqrt(x)) % 2 != 0)
        for y in range(3,sqrt_x,2):
            last_value = list(range(3,sqrt_x,2))[-1]
            if x % y == 0 and x != y:
                return False
                #break
            elif last_value  == y:
                return True
    else:
        return False

prime_number(1701117049)
prime_number(999983)

import sys

#t = int(input().strip())
#for a0 in range(t):
#    n = int(input().strip())

n=100
prime_found=0
i=0
if prime_number(n):
    print(n)
else:
    start_number=n//2
    if start_number % 2 == 0:
        start_number -= 1
    print(f"start_number={start_number}")
    for i in range(start_number,1,-2):
        print(f"i={i}")
        if (prime_number(i) or i in (1,2,3,5,7)) and n%i==0:
            print(i)
            prime_found +=1
            break
    if i==3 and prime_found == 0:
        print(2)

print(int(math.sqrt(1000000000000)))
#1000000
prime_number(5)

for i in range(7, 1, -2):
    print(i)

#v3
#potential prime numbers <= N above 10
import sys
import math
N=100
#for i in range(11,N+1,2):
for i in range(25,N+1,2):
    if i % 2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0: #and i % 11 !=0
            #and sum_digits_iterative(i) != 3 and ((i+1) % 6 ==0 or (i-1) % 6 ==0)):
        potential +=1
        #print(i)
print(potential)

N=1000000
#potential=[2,3,5,7]
potential=[]
#for i in range(11,N+1,2):
for i in range(25,N+1,2):
    if i % 2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0: #and i % 11 !=0
            #and sum_digits_iterative(i) != 3 and ((i+1) % 6 ==0 or (i-1) % 6 ==0)):
        potential.append(i)
        #print(i)
#print(potential)

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
#potential=[10,11,12,13,14,15,16,17]
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

#There are 78,498 prime numbers between 1 and 1,000,000
print(prime_numbers)
print(len(prime_numbers))

#t = int(input().strip())
#for a0 in range(t):
    #n = int(input().strip())
test_prime=[10,11,16,1000000,999999]
test_prime=[10,11,16,999999,1000000,1000001,1000002,1000003,600851475143, 999966000557, 999999999998,1000000000000]
for n in test_prime:
    if n not in prime_numbers:
        prime_factors_potential = [num for num in prime_numbers if num <= n//2]
        index = len(prime_factors_potential) - 1
        while index >= 0:
            if n % prime_factors_potential[index] == 0:
                print(prime_factors_potential[index])
                index = -1
            else:
                index -= 1
    else:
        print(n)

#tests
#1000001: 101 x 9901
#1000002: 2 x 3 x 166667
#1000003: prime number
#999999999998: 2 x 2969 x 168406871
#1000000000000: 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 5 x 5 x 5 x 5 x 5 x 5 x 5 x 5 x 5 x 5 x 5 x 5
test_prime=[999999999998]
for n in test_prime:
    prime_factors=[]
    i=0
    nn=n
    while prime_numbers[i]!=prime_numbers[-1]:
        if nn%prime_numbers[i]==0:
            prime_factors.append(prime_numbers[i])
            nn=int(nn/prime_numbers[i])
        else:
            i+=1
    if nn==1:
        print(max(prime_factors))
    elif n!=nn:
        print(nn)
    else: #prime number
        print(n)

print(prime_factors)

for n in test_prime:
    if n not in prime_numbers:
        prime_factors_potential = [num for num in prime_numbers if num <= n//2]
        index = len(prime_factors_potential) - 1
        while index >= 0:
            if n % prime_factors_potential[index] == 0:
                print(prime_factors_potential[index])
                index = -1
            else:
                index -= 1
    else:
        print(n)

test_primes=[10,11,16,999999,1000000,1000001,1000002,1000003,600851475143, 999966000557, 999999999998,1000000000000]
t = len(test_primes)
for a0 in range(t):
    #n = int(input().strip())
    n=test_primes[a0]
    if n<=1000000:
        if n not in prime_numbers:
            prime_factors_potential = [num for num in prime_numbers if num <= n//2]
            index = len(prime_factors_potential) - 1
            while index >= 0:
                if n % prime_factors_potential[index] == 0:
                    print(prime_factors_potential[index])
                    index = -1
                else:
                    index -= 1
        else:
            print(n)
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
            print(max(prime_factors))
        elif n!=nn:
            print(nn)
        else: #prime number
            print(n)

test_primes=[999999999997,99999999993,9999999991,999999999993,999999999991,99999999997,999999999745,9999999997,999999999989,999999999983]
#test cases 2
'''
--> Output:
181587071
108577633
100003
211371803
1000003
5882352941
199999999949
769230769
999999999989
4366812227
'''

test_primes=[45182,28,70,359,71,77,977,77777777]
'''
41
7
7
359
71
11
977
137
'''

for k in test_prime:
    print(k)

print(k!=test_prime[-1])

for k in range(0,len(test_prime)):
    print(k)
    print(test_prime[k])
    print(test_prime[k]!=test_prime[-1])

print(len(test_prime))

#v4
#https://mathworld.wolfram.com/DirectSearchFactorization.html

def is_prime(m):
    if m <= 1:
        return False
    if m <= 3:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False
    i = 5
    while i * i <= m:
        if m % i == 0 or m % (i + 2) == 0:
            return False
        i += 6
    return True

is_prime(11)

prime_valid=[]
for p in range(1,1000000):
    if is_prime(p):
        prime_valid.append(p)

print(len(prime_valid))

prime_check=[]
for i in prime_numbers:
    if i not in prime_valid:
        prime_check.append(i)

len(prime_chack)


n = 1000000000000
i = 2
while i * i < n:
    while n%i == 0:
        n = n // i
    i = i + 1
print(n)

#Validations
#Gimini solution
def largest_prime_factor(n):
    """
    Finds the largest prime factor of a given number.

    Args:
        n: The number to find the largest prime factor of.

    Returns:
        The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(600851475143))

#Final
#Success

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