""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/contest/2019/problem/A
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [0] * n
    selected = [False] * n  
    
    dp[0] = arr[0]
    selected[0] = True
    
    if arr[1] > arr[0]:
        dp[1] = arr[1]
        selected[1] = True
    else:
        dp[1] = dp[0]
        selected[1] = False
    
    for i in range(2, n):
        if arr[i] + dp[i-2] > dp[i-1]:
            dp[i] = arr[i] + dp[i-2]
            selected[i] = True
        else:
            dp[i] = dp[i-1]
            selected[i] = False

    temp = []
    i = n - 1
    while i >= 0:
        if selected[i]:
            temp.append(arr[i])
            i -= 2  
        else:
            i -= 1
    maxItem = max(temp)
    print(maxItem+len(temp))

    tc-=1


