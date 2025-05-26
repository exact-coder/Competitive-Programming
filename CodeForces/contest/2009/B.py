""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/contests/2009/B
Give Time to Time , It can hill everything.
*******************************"""


test_case = int(input())


for i in range(test_case):
    n = int(input())
    output = []
    arr =[]

    for i in range(n):
        b_l = list(input())
        arr.append(b_l)

    for i in range(len(arr)-1,-1,-1):
        for j in range(4):
            if arr[i][j] == "#":
                output.append(j+1)

    print(" ".join(map(str,output)))


    test_case-=1


