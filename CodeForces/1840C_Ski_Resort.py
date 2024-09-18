""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1840/C
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:

    n,k,q = map(int,input().split())
    n_list = list(map(int,input().split()))

    output =0

    consecutive = 0

    for i in range(n):
        if n_list[i] <=q:
            consecutive+=1
            if i == n-1 or n_list[i+1] > q:
                if consecutive >=k:
                    temp = consecutive-k+1
                    add = (temp*(temp+1))/2
                    output+=add
                consecutive=0
    print(int(output))

    test_case-=1