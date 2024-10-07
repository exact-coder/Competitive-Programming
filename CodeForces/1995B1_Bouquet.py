""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1995/B1
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())
from bisect import bisect_right


while tc:
    n,m = map(int,input().split())
    bouquet = sorted(list(map(int,input().split())))
    pre = [0] * n
    pre[0] = bouquet[0]
    for i in range(1, n):
        pre[i] = pre[i - 1] + bouquet[i]
    
    ans = 0
    for i in range(n):
        temp = (0 if i == 0 else pre[i - 1]) + m
        idx1 = bisect_right(bouquet, bouquet[i] + 1) - 1
        idx2 = bisect_right(pre, temp) - 1
        
        if idx2 < i:
            continue
        if idx2 <= idx1:
            ans = max(ans, pre[idx2] - (0 if i == 0 else pre[i - 1]))
        else:
            ans = max(ans, pre[idx1] - (0 if i == 0 else pre[i - 1]))
    
    print(ans)
    

        
    tc-=1





