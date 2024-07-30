
# https://codeforces.com/problemset/problem/1829/D

test_case = int(input())

def recursive_func(n,m):
    if(n==m):return True
    if(n%3 != 0): return False
    return recursive_func(n//3,m) or recursive_func(2*(n//3),m)


while test_case:
    n,m = map(int,input().split(" "))

    if recursive_func(n,m):
        print("YES")
    else:
        print("NO")

    test_case-=1