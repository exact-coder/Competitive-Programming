
# https://codeforces.com/problemset/problem/1931/C

test_case = int(input())

while test_case:

    arr_size = int(input())
    arr = list(map(int,input().split(" ")))

    first = 0
    output = 0
    last = arr_size -1

    while(arr_size> first and arr[first] == arr[0]):
        first+=1
    
    while(last >= 0 and arr[last] == arr[arr_size - 1]):
        last -=1
    
    if (arr_size > first and last >=0 and arr[0] != arr[arr_size-1]):
        makeAllF = arr_size - first
        makeAllL = last +1
        output+= min(makeAllF,makeAllL)
    else:
        output += max(0, last - first + 1)

    print(output)

    test_case -=1


