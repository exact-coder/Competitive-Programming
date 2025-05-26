
# https://codeforces.com/problemset/problem/1955/B

test_case = int(input())


while test_case:
    n,c,d = map(int,input().split(" "))
    matrix_list = list(map(int,input().split(" ")))

    sort_mx = sorted(matrix_list)
    mx = []
    mx2 =[]

    for i in range(n):
        mx.append(sort_mx[0]+(i*d))

    for j in range(n):
        for k in range(n):
            mx2.append(mx[j]+(k*c))
    sort_mx2 = sorted(mx2)
    if sort_mx == sort_mx2:
        print("YES")
    else:
        print("NO")

    test_case -=1




""" while test_case:
    n,c,d = map(int,input().split(" "))
    matrix_list = list(map(int,input().split(" ")))

    min_val = min(matrix_list)
    matrix_list.remove(min_val)
    c_val =(min_val + c)
    d_val = (min_val+d)
    for i in range(n*n):
        if c_val in matrix_list:
            matrix_list.remove(c_val)
            c_val= min_val + (i*c)
        if d_val in matrix_list:
            matrix_list.remove(d_val)
            d_val= min_val + (i*d)
        # min_val = min(matrix_list)
    if matrix_list:
        print("NO")
    else:
        print("YES")

    test_case -=1
 """
