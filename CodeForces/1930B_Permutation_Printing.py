
# https://codeforces.com/problemset/problem/1930/B

test_case = int(input())

while test_case:
    n = int(input())

    p_arr = []
    c = n

    for i in range(n):
        p_arr.append(i)
    
    for i in range(1,n,2):
        p_arr[i] =c
        c-=1

    for i in range(0,n,2):
        p_arr[i] = c
        c-=1
    
    print(" ".join(map(str,p_arr)))

    test_case -= 1


