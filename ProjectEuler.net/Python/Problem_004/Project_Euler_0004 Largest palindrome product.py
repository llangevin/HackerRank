#Project Euler #4: Largest palindrome product
#https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true
#Accepted

#!/bin/python3

import sys

def palindrome_check(n):
    digits = []
    while n >= 10:
        digits.append(n % 10)
        n = n // 10
    digits.append(n)
    if len(digits) == 6:
        if digits[0] == digits[5] and digits[1] == digits[4] and digits[2] == digits[3]:
            return True
        else:
            return False
    else:
        if digits[0] == digits[4] and digits[1] == digits[3]:
            return True
        else:
            return False

palindrome_list=[]
for i in range(100,1000):
    for j in range(i,1000):
        if palindrome_check(i*j) and i*j>=101101:
            palindrome_list.append(i*j)

palindrome_list.sort()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print([num for num in palindrome_list if num < n][-1])
