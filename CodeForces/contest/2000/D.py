

test_case = int(input())


while test_case:

    n = int(input())
    strip_num = list(map(int, input().split()))
    strip_ch = input().strip()
    
    arr = [0] * (n + 1)

    for i in range(1, n + 1):
        arr[i] = arr[i - 1] + strip_num[i - 1]

    k = n
    output = 0

    for i in range(1, n + 1):
        if strip_ch[i - 1] == 'L':
            while k > i and strip_ch[k - 1] != 'R':
                k -= 1
            if k > i:
                output += arr[k] - arr[i - 1]
                k -= 1

    print(output)


    test_case-=1


