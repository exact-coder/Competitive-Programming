

test_case = int(input())

while test_case:

    n = int(input())
    array_a = list(map(int,input().split(" ")))

    output =0

    for i in range(n):
        if (i % 2==0):
            output = max(output, array_a[i])

    print(output)
    test_case-=1
