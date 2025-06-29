#Project Euler #8: Largest product in a series
#https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true

n=10
k=5 #1<=k<=7
num=3675356291 #k<=n<=1000

for i in range(0,n-k+1):
    print(i)
    print((num%10**(n-i))//10**(k-i))

print(num%10**10) #3675356291
print((num%10**10)//10**5) #36753
print(num//10**5) #36753

print(num%10**9) #675356291
print((num%10**9)//10**4) #67535

print(num%10**8) #75356291
print((num%10**8)//10**3) #75356

print(num%10**7) #5356291
print((num%10**7)//10**2) #53562

print(num%10**6) #356291
print((num%10**6)//10**1) #35629

print(num%10**5) #56291
print((num%10**5)//10**0) #56291

num_k=36753
#num_kj=num_k
num_k_prod=1
for j in range(0,k):
    num_kj=num_k//10**j
    num_1=num_kj%10
    num_k_prod *=num_1
    print(num_kj)
    print(num_1)
    print(num_k_prod)

n=10
k=5 #1<=k<=7
num=3675356291 #k<=n<=1000

max_num_prod=0
for i in range(0,n-k+1):
    num_k=(num%10**(n-i))//10**(k-i)
    num_k_prod = 1
    if num_k>=10**(k-1):
        for j in range(0, k):
            num_kj = num_k // 10 ** j
            num_1 = num_kj % 10
            num_k_prod *= num_1
        if num_k_prod > max_num_prod:
            max_num_prod = num_k_prod

#cant handle 0
#character
n=10
k=5 #1<=k<=7
num=3675356291 #k<=n<=1000
num_text=str(num)

max_num_prod=0
for i in range(0,n-k+1):
    print(i)
    print(num_text[i:(i+k)])
    num_k_prod = 1
    for j in (num_text[i:(i+k)]):
        print(j)
        num_k_prod *= int(j)
    if num_k_prod > max_num_prod:
        max_num_prod = num_k_prod

def gpkcdndn(n,k,num):
    num_text = str(num)
    max_num_prod = 0
    for i in range(0, n - k + 1):
        num_k_prod = 1
        for j in (num_text[i:(i + k)]):
            num_k_prod *= int(j)
        if num_k_prod > max_num_prod:
            max_num_prod = num_k_prod
    return(max_num_prod)

gpkcdndn(10,5,3675356291)
gpkcdndn(10,5,2709360626)