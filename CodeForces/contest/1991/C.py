
test_case = int(input())

while test_case:
    n = int(input())
    arr = list(map(int,input().split()))

    output_list = []
    
    while max(arr) > 0:
        if len(output_list) >= 40:
            output_list.append(-1)
            break

        non_zero = [x for x in arr if x != 0]
        if len(non_zero) > 1 and (non_zero[0] % 2) != (non_zero[1] % 2):
            output_list.append(-1)
            break
        
        min_value = min(arr)
        max_value = max(arr)
        x = (min_value + max_value) // 2
        output_list.append(x)
        arr = [abs(a - x) for a in arr]

    if (-1) in output_list:
        print(-1)
    else:
        print(len(output_list))
        print(" ".join(map(str, output_list[0:])))

    test_case-=1


