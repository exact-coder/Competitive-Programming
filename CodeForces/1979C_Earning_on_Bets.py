""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1979/C
Give Time to Time , It can hill everything.
*******************************"""
from math import gcd
from functools import reduce


tc = int(input())

# def gcd(num1,num2):
#     for i in range(1, min(num1, num2)):
#         if num1 % i == 0 and num2 % i == 0:
#             res = i
#     return res

def lcm(x, *xs):
    return reduce(lambda a, b: a * b // gcd(a, b), (x,) + xs)

    
while tc:
    n = int(input())
    arr = list(map(int, input().split()))

    x = arr[0]
    for i in range(1, n):
        x = lcm(x, arr[i])
    
    a = [x // arr[i] for i in range(n)]
    if sum(a) >= x:
        print("-1")
        continue
    
    print(" ".join(map(str, a)))


    tc-=1










