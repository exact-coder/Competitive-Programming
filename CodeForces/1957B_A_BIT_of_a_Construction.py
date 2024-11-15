""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1957/B
Give Time to Time , It can hill everything.
*******************************"""

import math
tc = int(input())

def log2Power(k):
    x = int(math.log2(k))
    return pow(2,x)


while tc:
    n, k = map(int,input().split())
    x = log2Power(k)

    if n== 1:
        print(k)
    else:
        print(x,k-x,"0 " * (n-2))

    tc-=1





