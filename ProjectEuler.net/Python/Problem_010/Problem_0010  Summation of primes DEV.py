#Project Euler #10: Summation of primes
#https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true

prime_number_list=[2,3]
prime_number_sum=[2,5]
n=5
sum_prime=5
#while len(prime_number_list)<10000:
while n <= 20:
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
            sum_prime +=n
            prime_number_sum.append(sum_prime)
        n += 2

#[1,2,3, 4]
#[2,3,5, 7]
#[2,5,10,17]

nn=10
prime_number_list_n = [num for num in prime_number_list if num <= nn]
print(len(prime_number_list_n))
print(prime_number_sum[len(prime_number_list_n)-1])

###
number_list=[1,2,3,4]
prime_number_list=[2,3]
prime_number_sum=[0,2,5,5]
n=5
sum_prime=5
#while len(prime_number_list)<10000:
while n <= 100:
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
            prime_number_list.append(n)
            sum_prime +=n
            number_list.append(n)
            prime_number_sum.append(sum_prime)
            number_list.append(n+1)
            prime_number_sum.append(sum_prime)
        n += 2

#[1,2,3,4,5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
#[2,3,5,7,11,13,17,19]
#[0,2,5,5,10,10,17,17,17,17,28,28,41,41,41,41,58,58,77,77]
nn=10
print(prime_number_sum[nn-1])