#Project Euler #7: 10001st prime
#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true

def prime_n(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i <= n:
        if n%i==0 or n%(i+2) == 0:
            return False
        i +=6
    return True

prime_number_list=[2,3]
n=5
while len(prime_number_list)<=10:
    if not (n%2==0 or n%3==0):
        i=5
        while i*i<=n:
            if not (n%i==0 or n%(i+2) == 0):
                i +=6
        prime_number_list.append(n)
        len_list=len(prime_number_list)
        n +=2

prime_number_list=[2,3]
n=5
while len(prime_number_list)<1001:
    if n%2==0 or n%3==0:
        n += 2
    else:
        i=5
        prime=1
        while i*i <= n:
            if n%i==0 or n%(i+2) == 0:
                prime=0
                i=n
            i +=6
        if prime==1:
            prime_number_list.append(n)
        n += 2

print(prime_number_list[0])