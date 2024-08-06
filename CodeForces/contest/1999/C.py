

test_case = int(input())

for t in range(test_case):

    n, s, m = map(int, input().split())
    arr = []
    
    for k in range(n):
        l, r = map(int, input().split())
        arr.append((l, r))
    
    arr.sort()
    arr_inn = arr[0][0]
    
    if arr_inn >= s:
        print("Yes")
        continue
    l_ele = arr[0][1]
    
    for i in range(1, n):
        if arr[i][0] > l_ele:
            if arr[i][0] - l_ele >= s:
                print("Yes")
                break
        l_ele = max(l_ele, arr[i][1])
        
    else:
        if m - l_ele >= s:
            print("Yes")
        else:
            print("No")









