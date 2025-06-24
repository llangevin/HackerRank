#Project Euler #4: Largest palindrome product
#https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true

test=111111
digit=[]
while test>=10:
    digit.append(test % 10)
    test=test//10
digit.append(test)
if len(digit)==6:
    if digit[0]==digit[5] and digit[1]==digit[4] and digit[2]==digit[3]:
        print(True)
    else:
        print(False)
else:
    if digit[0] == digit[4] and digit[1] == digit[3]:
        print(True)
    else:
        print(False)

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

palindrome_check(12345)
palindrome_check(123456)
palindrome_check(10101)
palindrome_check(10001)
palindrome_check(111111)
palindrome_check(110011)
palindrome_check(100001)
palindrome_check(999999)
palindrome_check(900009)

#product of two 3-digit numbers
for i in range(1,4):
    for j in range(i,4):
        print(f"i={i}, j={j}")

palindrome_list=[]
for i in range(100,1000):
    for j in range(i,1000):
        if palindrome_check(i*j) and i*j>=101101:
            palindrome_list.append(i*j)

palindrome_list.sort()

n=101102
n=101110
n=800000
print([num for num in palindrome_list if num < n][-1])
#prime_factors_potential = [num for num in prime_numbers if num <= n//2]

#final
#Success

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