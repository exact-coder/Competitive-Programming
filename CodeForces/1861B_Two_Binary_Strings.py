
# https://codeforces.com/problemset/problem/1861/B


test_case = int(input())


while test_case:

    a = list(input())
    b = list(input())
    # a1 = [ 0 for i in range(total_str) ]
    # b1 = [ 0 for i in range(total_str) ]

    for i in range(len(a)-1):
        if a[i] == b[i] and a[i+1] == b[i+1] and a[i] == "0" and a[i+1] =="1":
            print("YES")
            break
    else:
        print("NO")

    test_case-=1

