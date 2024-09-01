

test_case = int(input().strip())

while test_case:
    n, k = map(int, input().strip().split())
    
    arr = [[float('inf')] * (k + 1) for i in range(n + 1)]
    cost_arr = [[0] * (k + 1) for i in range(n + 1)]
    
    for i in range(1, n + 1):
        a, b = map(int, input().strip().split())
        cost_arr[i][0] = 0
        for p in range(1, k + 1):
            cost_arr[i][p] = float('inf')
            for r in range(0, p + 1):
                c = p - r
                if r > a or c > b:
                    continue
                cost_arr[i][p] = min(cost_arr[i][p], r * b + c * a - r * c)
    
    arr[0][0] = 0
    
    for i in range(n):
        for j in range(k + 1):
            for t in range(j, k + 1):
                arr[i + 1][t] = min(arr[i + 1][t], arr[i][j] + cost_arr[i + 1][t - j])
    
    if arr[n][k] == float('inf'):
        arr[n][k] = -1
    
    print(arr[n][k])

    test_case-=1