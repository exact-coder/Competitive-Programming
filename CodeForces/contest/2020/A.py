""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/2020/A
Give Time to Time , It can hill everything.
*******************************"""

tc = int(input())


while tc:
    n,k = map(int,input().split())
    cnt =0

    if k == 1:
        print(n)
	
    while n:
        cnt += n%k
        n//=k
    print(cnt)
    tc-=1