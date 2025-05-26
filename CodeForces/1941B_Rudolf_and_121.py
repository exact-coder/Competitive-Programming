
# https://codeforces.com/problemset/problem/1941/B

test_case = int(input())

while test_case:
    n = int(input())

    n_ele = list(map(int,input().split()))

    for i in range(1,n-1):
        if(n_ele[i-1]>=0):
            n_ele[i] = n_ele[i] - 2*n_ele[i-1]
            n_ele[i+1] = n_ele[i+1] - n_ele[i-1]
            n_ele[i-1] = 0
        else:
            break
    zero = 0
    for i in range(n):
        if(n_ele[i] !=0):
            zero = 1
            break

    if zero != 0:
        print("NO")
    else:
        print("YES")

    test_case-=1


# while test_case:
#     n = int(input())

#     n_ele = list(map(int,input().split()))

#     for i in range(1,n-1):
#         if n_ele[i] >= 2:
#             for j in range(int(n_ele[i]/2)):
#                 if n_ele[i-1] > 0 and n_ele[i] >=2 and n_ele[i+1] > 0:
#                     n_ele[i-1] -=1
#                     n_ele[i+1] -=1
#                     n_ele[i]-=2
#     if max(n_ele) >0:
#         print("NO")
#     else:
#         print("YES")

    # test_case-=1

# 7
# 5
# 1 3 5 5 2
# 5
# 2 4 4 5 1
# 5
# 0 1 3 3 1
# 6
# 5 6 0 2 3 0
# 4
# 1 2 7 2
# 3
# 7 1 0
# 4
# 1 1 1 1
