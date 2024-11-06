""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1975/C
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n = int(input())
    a = list(map(int,input().split()))
    ans=[]
    for i in range(n-1):
        ans.append(min(a[i],a[i+1]))
    
    for i in range(n-2):
        ans.append(min(a[i],a[i+2]))
    print(max(ans))

    tc-=1






