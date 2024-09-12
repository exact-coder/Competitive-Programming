""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1844/B
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:

    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(1, 2)
    else:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        arr[2],arr[-1]= arr[-1],arr[2]
        arr[0], arr[1] = arr[1], arr[0]
        arr[n//2], arr[1] = arr[1],arr[n//2]
        print(" ".join(map(str,arr)))

    test_case -=1

