

test_case = int(input())

while test_case:

    n,k = map(int,input().split())
    a_arr = list(map(int,input().split()))
    b_arr = list(map(int,input().split()))
    output =[]

    ord = list(range(n))
    ord.sort(key=lambda i: a_arr[i], reverse=True)
    
    need = (n - 1) // 2 + 1
    low, high = 0, int(1e10)
    
    while low < high:
        mid = (low + high + 1) // 2
        ok = False
        
        for i in ord:
            if b_arr[i] == 1:
                if a_arr[i] + k >= mid:
                    ok = True
                x = mid - a_arr[i] - k
                rem = need
                for j in ord:
                    if j == i:
                        continue
                    if rem == 0:
                        break
                    if a_arr[j] >= x:
                        rem -= 1
                if rem == 0:
                    ok = True
                break
        
        for i in ord:
            if b_arr[i] == 0:
                rem = need
                sum_ = 0
                x = mid - a_arr[i]
                for j in ord:
                    if j == i:
                        continue
                    if rem == 0:
                        break
                    if a_arr[j] >= x:
                        rem -= 1
                    elif b_arr[j]:
                        sum_ += x - a_arr[j]
                        rem -= 1
                if rem == 0 and sum_ <= k:
                    ok = True
                break
        
        if ok:
            low = mid
        else:
            high = mid - 1
    
    output.append(str(low))

    print('\n'.join(output))


    test_case-=1


