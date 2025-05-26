
# https://codeforces.com/problemset/problem/1811/B

test_case = int(input())

while test_case:

    n,x1,y1,x2,y2 = map(int,input().split())

    x_min = min(x1-1, n-x1,y1-1,n-y1)
    y_min = min(x2-1, n-x2,y2-1,n-y2)
    print(abs(x_min-y_min))

    test_case-=1

# 5
# 2 1 1 2 2
# =>min(0 1 0 1) 0 
# =>min(1 0 1 0) 0
# >> 0
# 4 1 4 3 3
# =>min(0 3 3 0) 0 
# =>min(2 2 2 1) 1
# >> 1
# 8 1 3 4 6
# =>min(0 7 2 5) 0 
# =>min(3 4 5 2) 2
# >> 2
# 100 10 20 50 100
# 1000000000 123456789 987654321 998244353 500000004
