

test_case = int(input())

while test_case > 0:

    r, c, s = map(int, input().split())

    arr = []
    
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            x = max(i - s + 1, 1)
            y = max(j - s + 1, 1)
            u = min(i, r - s + 1)
            v = min(j, c - s + 1)
            arr.append((u - x + 1) * (v - y + 1))
    
    arr.sort(reverse=True)
    n = int(input())
    
    arr2 = list(map(int, input().split()))
    arr2.sort(reverse=True)
    
    output = 0

    for i in range(n):
        output += arr2[i] * arr[i]
    
    print(output)

    test_case-=1