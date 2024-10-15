""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1982/C
Give Time to Time , It can hill everything.
*******************************"""




tc = int(input())


while tc:
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    
    sum_ = 0
    ans = 0
    start = 0
    
    for i in range(n):
        if a[i] > r:
            sum_ = 0
            start = i + 1
            continue
        sum_ += a[i]
        while sum_ > r:
            sum_ -= a[start]
            start += 1
        if 1 <= sum_ <= r:
            ans += 1
            sum_ = 0
            start = i + 1
    
    print(ans)

    tc-=1



