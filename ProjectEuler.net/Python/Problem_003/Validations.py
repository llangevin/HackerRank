#Validations
#Prime Numbers
#Gimini Solution

import math

def is_prime(number):
    """
    Checks if a given number is a prime number.

    Args:
        number: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    # We only need to check up to the square root because if a number 'n'
    # has a divisor 'd' greater than its square root, then it must also
    # have a divisor 'n/d' which is less than its square root.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # If divisible, it's not prime

    return True  # If no divisors found, it's prime

import sys
import math

N=1000000
#potential=[2,3,5,7]
potential=[]
#for i in range(11,N+1,2):
for i in range(25,N+1,2):
    if i % 2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0: #and i % 11 !=0
            #and sum_digits_iterative(i) != 3 and ((i+1) % 6 ==0 or (i-1) % 6 ==0)):
        potential.append(i)

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

prime_valid=[]
for p in range(1,1000000):
    if is_prime(p):
        prime_valid.append(p)

print(len(prime_valid))

prime_check=[]
for i in prime_numbers:
    if i not in prime_valid:
        prime_check.append(i)

len(prime_check)

prime_check2=[]
for i in prime_valid:
    if i not in prime_numbers:
        prime_check2.append(i)

len(prime_check2)

#Largest Prime Factor
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
#6857
print(largest_prime_factor(10))

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

mine_lpf(600851475143)
#6857
mine_lpf(10)
mine_lpf(11)
mine_lpf(16)
mine_lpf(1048576)

compare_jj=[]
for jj in range(3000000,4000000):
    if mine_lpf(jj) != largest_prime_factor(jj):
        compare_jj.append(jj)

print(len(compare_jj))
print(compare_jj)
#no diff: 1:3000000

mine_lpf(10)
largest_prime_factor(10)
print(mine_lpf(10) != largest_prime_factor(10))
print(mine_lpf(10) == largest_prime_factor(10))
print(mine_lpf(11) != largest_prime_factor(11))
print(mine_lpf(11) == largest_prime_factor(11))
print(mine_lpf(16) != largest_prime_factor(16))
print(mine_lpf(16) == largest_prime_factor(16))

mine_lpf_n=[]
for iii in range(10,21):
    mine_lpf_n.append(mine_lfp(iii))

largest_prime_factor_n=[]
for iii in range(10,21):
    largest_prime_factor_n.append(largest_prime_factor(iii))