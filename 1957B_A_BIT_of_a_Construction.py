""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1957/B
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n, k = map(int,input().split())
    mx = -1
    st = 0
    for i in range(31):
        if (k & (1 << i)):
            mx = i
            st += 1

    if n == 1 or mx + 1 == st:
        print(k, end=" ")
        print("0 " * (n - 1), end="")
        print()
    else:
        val = (1 << mx) - 1
        extra = k - val

        print(val, extra, end=" ")
        print("0 " * (n - 2), end="")
        print()

    tc-=1





