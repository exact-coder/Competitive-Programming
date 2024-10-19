""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1979/C
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())

def gcd(num1,num2):
    for i in range(1, min(num1, num2)):
        if num1 % i == 0 and num2 % i == 0:
            res = i
    return res
    
while tc:
    n = int(input())
    arr = list(map(int,input().split()))
    lc = arr[0]
    for i in range(1,n):
        lc = lc*((arr[i])//gcd(lc,arr[i]))
    ans =[]
    sum_a =0
    minn=1e12
    for i in range(n):
        ans.append(lc//arr[i])
        sum_a+=ans[i]
        minn = min(minn,arr[i]*ans[i])
    if sum_a < minn:
        output =[]
        for i in range(n):
            output.append(ans[i])
        print(" ".join(map(str,output)))
    else:
        print(-1)



    tc-=1





