
# https://codeforces.com/problemset/problem/1975/B

test_case = int(input())

while test_case:

    arr_len = int(input())
    a_arr = list(map(int,input().split()))

    a_arr_sorted = sorted(a_arr)
    b_arr=[]
    output=0

    for i in range(arr_len):
        if(a_arr_sorted[i] % a_arr_sorted[0] !=0):
            b_arr.append(a_arr_sorted[i])
    
    for j in range(len(b_arr)):
        if(b_arr[j] % b_arr[0] != 0):
            output+=1
    
    if output > 0:
        print("NO")
    else:
        print("YES")

    test_case-=1