# Project Euler #1: Multiples of 3 and 5
#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

import sys

#in Hackerrank
input = [int(line) for line in sys.stdin.readlines()]
print(input)
#[2, 10, 100]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

input=["2","10","100"]
print(input[0])

t=int(input[0])
for a0 in range(t):
    n = int(input[1+ a0])
    print(n)

input=[2,10,100]
t=input[0]
for a0 in range(t):
    n = input[1+ a0]
    print(n)

input=[2,10,100]
t=input[0]
for a0 in range(t):
    n = input[1+ a0]
    print(f"n= {n}")
    sum = 0
    for i in range(n-1):
        if (i+1) % 3 == 0 or (i+1) % 5 == 0:
            print(i+1)
            sum += (i+1)
    print(f"sum= {sum}")

input=[2,10,100]
t=input[0]
for a0 in range(t):
    print(f"n= {input[1+ a0]}")
    sum = 0
    for i in range(input[1+ a0] -1):
        sum += ((i+1) % 3 == 0 or (i+1) % 5 == 0) * (i+1)
    print(f"sum= {sum}")

for i in range(10):
    print(i)

########################
#V1
import sys

#input=[2,10,100]
input = [int(line) for line in sys.stdin.readlines()]
t=input[0]
for a0 in range(t):
    #n = input[1+ a0]
    sum = 0
    for i in range(input[1+ a0] -1):
        if (i+1) % 3 == 0 or (i+1) % 5 == 0:
            sum += (i+1)
    print(sum)

#########################
#V2 Success
input=[3,10,100,4]
t=input[0]
for a0 in range(t):
    #n = int(input().strip()) -1
    n = input[1+ a0] -1
    sum=0
    N3 = n// 3
    sum += 3*(N3*(1+N3)//2)
    N5 = n// 5
    sum += 5*(N5*(1+N5)//2)
    N15 = n// 15
    sum -= 15*(N15*(1+N15)//2)
    print(sum)