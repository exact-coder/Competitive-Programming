""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1973/A
Give Time to Time , It can hill everything.
*******************************"""




import math

test_case = int(input())


while test_case:
    p1,p2,p3 = map(int,input().split())

    maxPQ = []
    if p1>0:
        maxPQ.append(p1)
    if p2>0:
        maxPQ.append(p2)
    if p3>0:
        maxPQ.append(p3)

    while(len(maxPQ)>1):
        first = maxPQ
        
    test_case-=1


# https://codeforces.com/problemset/problem/1834/B
# https://codeforces.com/problemset/problem/1831/B
# https://codeforces.com/problemset/problem/1825/B


