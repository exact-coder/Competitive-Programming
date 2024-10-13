""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/contest/2022/problem/0
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n,r = map(int,input().split())
    a_li = list(map(int,input().split()))
    happy=0

    for i in range(n):
        if a_li[i] >= 2 and r >0:
            for j in range(a_li[i]//2):
                happy +=2
                r-=1
                a_li[i]-=2
        elif (r>0 and not a_li[-1]) or r>1:
            happy+=1
            r-=1
    print(happy)







    tc-=1





