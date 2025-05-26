
# https://codeforces.com/contest/1992/problem/B


test_case = int(input())

while test_case:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    operations = 0
    for i in range(k - 1):
        if a[i] == 1:
            operations += 1
        else:
            operations += 2 * a[i] - 1
    print(operations)


    test_case-=1


