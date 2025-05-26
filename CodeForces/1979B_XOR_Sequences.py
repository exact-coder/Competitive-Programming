
# https://codeforces.com/problemset/problem/1979/B



test_case = int(input())

while test_case:

    n,m = map(int,input().split())
    count = 0
    while(n or m):
        if(n%2 == m%2):
            count+=1
        else:
            break
        n=n//2
        m=m//2
    ans = 1 << count
    print(ans)

    test_case-=1




    # x, y = map(int, input().split())
    # v = []
    # v1 = []

    # while x > 0:
    #     ok = x % 2
    #     v.append(ok)
    #     x = x // 2
    # while len(v) < 32:
    #     v.append(0)

    # while y > 0:
    #     ok = y % 2
    #     v1.append(ok)
    #     y = y // 2
    # while len(v1) < 32:
    #     v1.append(0)

    # ans = 0
    # for i in range(32):
    #     if v[i] == v1[i]:
    #         ans += 1
    #     else:
    #         break
    # ok = 1 << ans
    # print(ok)



