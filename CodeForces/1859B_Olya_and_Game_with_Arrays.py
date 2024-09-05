""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1859/B
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:

    n = int(input())
    temp = []
    min2 = 1e9
    min1 = 1e9

    for a in range(n):
        m = int(input())
        arr = list(map(int,input().split()))
        a_s =sorted(arr)
        temp.append(a_s)
    
    for i in range(len(temp)):
        min2 = min(temp[i][1],min2)
        min1 = min(temp[i][0],min1)
    
    output =0
    count = 0
    for j in range(len(temp)):
        if temp[j][1] == min2 and count == 0: count+=1
        else: output += temp[j][1]

    output+=min1
    print(output)

    test_case-=1

