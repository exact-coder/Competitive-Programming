
# https://codeforces.com/problemset/problem/1883/C

test_case = int(input())

while test_case:
    n,k = map(int, input().split())
    n_arr = list(map(int,input().split()))
    even =0 
    output = k

    for i in range(n):
        if n_arr[i] % 2 == 0:even += 1
        if n_arr[i] % k == 0: output = 0
        output = min(output, k - n_arr[i] % k)
    
    if k == 4:
        if even >= 2:
            output = 0
        elif even == 1:
            output = min(output, 1)
        else:
            output = min(output, 2)
    
    print(output)

    test_case-=1



