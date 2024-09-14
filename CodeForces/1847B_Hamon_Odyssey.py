""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1847/B
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:
    n = int(input())
    n_arr = list(map(int,input().split()))
    
    output = []

    cur = n_arr[0]
    part = 1
    
    for i in range(n):
        cur &= n_arr[i]
        if cur == 0:
            if i == n-1:
                break
            part += 1
            cur = n_arr[i + 1]
    
    if cur != 0:
        part -= 1
    
    part = max(part, 1)
    output.append(part)

    for r in output:
        print(r)


    test_case-=1







