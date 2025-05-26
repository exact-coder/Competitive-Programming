# https://codeforces.com/problemset/problem/1918/B

test_case = int(input())

while test_case:

    n= int(input())

    arr_a = list(map(int,input().split()))
    arr_b = list(map(int,input().split()))
    temp_arr = {}

    for i in range(n):
        temp_arr[arr_a[i]] = arr_b[i]
    
    arr_a.sort()

    print(" ".join(map(str, arr_a)))
    print(" ".join(map(str, [temp_arr[j] for j in arr_a])))


    test_case -= 1




