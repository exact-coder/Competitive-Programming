# https://codeforces.com/problemset/problem/1986/B

test_case = int(input())
while test_case > 0:
    n, m = map(int, input().split())
    matrix = [[int(x) for x in input().split()] for y in range(n)]

    # print("matrix",matrix)

    stabilized = True

    while stabilized:
        stabilized = False
        for i in range(n):
            for j in range(m):
                up = matrix[i-1][j] if i > 0 else 0
                left = matrix[i][j-1] if j > 0 else 0
                down = matrix[i+1][j] if i < n-1 else 0
                right = matrix[i][j+1] if j < m-1 else 0

                max_neighbor = max(up, down, left, right)

                if matrix[i][j] > max_neighbor:
                    matrix[i][j] = max_neighbor
                    stabilized = True

    for row in matrix:
        print(" ".join(map(str, row)))
    test_case -= 1


