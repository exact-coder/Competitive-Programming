""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/contest/2022/problem/B
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n,x = map(int,input().split())
    a_li = sorted(list(map(int,input().split())))
    total_sum = 0
    customer =0

    if a_li[0] == 1:
        print(a_li[-1])
    else:
        for i in range(n):
            total_sum+=a_li[i]
        if total_sum % 2:
            print((total_sum//x)+1)
        else:
            print(total_sum//x)

    







    tc-=1





