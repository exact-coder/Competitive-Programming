
# https://codeforces.com/problemset/problem/1968/C
 
test_case = int(input())
 
while test_case:
 
    n= int(input())
    arr = list(map(int,input().split(" ")))
    output_arr = []
    output_arr.append(501)
 
    for i in range(n-1):
        output_arr.append(output_arr[i]+arr[i])
 
    print(output_arr)
 
 
    test_case -= 1
 




