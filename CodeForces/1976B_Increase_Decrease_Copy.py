""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1976/B
Give Time to Time , It can hill everything.
*******************************"""

tc = int(input())
# 1
# 2
# 1 3

while tc:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    tot = 1
    for i in range(n):
        tot += abs(a[i] - b[i])

    mn = float('inf')
    for i in range(n):
        if a[i] <= b[n] and b[n] <= b[i]:
            mn = 0
        if a[i] >= b[n] and b[n] >= b[i]:
            mn = 0

    for i in range(n):
        if a[i] <= b[n] and a[i] <= b[i]:
            mn = min(mn, abs(b[n] - b[i]))
        if a[i] >= b[n] and a[i] >= b[i]:
            mn = min(mn, abs(b[n] - b[i]))

    for i in range(n):
        mn = min(mn, abs(b[n] - a[i]))

    print(tot + mn)


    tc-=1





