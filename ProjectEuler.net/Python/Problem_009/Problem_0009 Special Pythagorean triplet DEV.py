#Project Euler #9: Special Pythagorean triplet
#https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=truev

n=12
for a in range(1,3):
    for b in range(a+1,6):
        for c in range(b+1,7):
            pt = False
            a_b_c=a+b+c
            if a**2+b**2==c**2:
                pt=True
            print(f"a={a}, b={b}, c={c}, a_b_c={a_b_c}, pt={pt}")

count=0
#1204 max cases
n_list=[-1] * 3000
for a in range(1,1000):
    for b in range(a, 1500):
        if (a**2+b**2)**0.5 == int((a**2+b**2)**0.5):
            a_b_c=a+b+int((a**2+b**2)**0.5)
            if a_b_c<=3000:
                abc=a * b * (int((a ** 2 + b ** 2) ** 0.5))
                count +=1
                print(f"a={a}, b={b}, c={int((a**2+b**2)**0.5)}, a_b_c={a_b_c}, abc={abc}, count={count}")
                if abc>n_list[a_b_c-1]:
                    n_list[a_b_c-1]=abc