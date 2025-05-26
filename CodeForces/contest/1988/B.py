
# https://codeforces.com/contest/1988/problem/B

test_case = int(input())


while test_case:

    n = int(input())
    str_sec = input()
    arr = []
    before = '1'
    for i in range(n):
        if str_sec[i] == '1':
            arr.append(1)
        if str_sec[i] == '0' and before == '1':
            arr.append(0)
        before = str_sec[i]
    n0 = 0
    n1 = 0
    for j in arr:
        if j == 1:
            n1 += 1
        else:
            n0 += 1
    if n0 >= n1:
        print("NO")
    else:
        print("YES")

    test_case-=1







