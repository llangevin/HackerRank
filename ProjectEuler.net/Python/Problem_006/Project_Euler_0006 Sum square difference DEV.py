#Project Euler #6: Sum square difference
#https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true

#the square of the sum of the first n natural numbers
n=10
sfnnn=(n*(n+1)//2)**2

#the sum of squares of the first n natural numbers
ssfnnn=(n*(n+1)*((2*n)+1)) // 6

print(sfnnn - ssfnnn)