""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1849/B
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:

    n,k = map(int,input().split())
    n_arr = list(map(int,input().split()))
    output =[]
    temp =[]

    for i in range(n):
        mod = n_arr[i] % k
        if mod == 0:
            output.append(i+1)
        else:
            temp.append([i+1, mod])

    temp2 = sorted(temp, key=lambda x: x[1])
    
    for i in temp2:
        output.append(i[0])

    print(" ".join(map(str,output)))

    test_case -=1


