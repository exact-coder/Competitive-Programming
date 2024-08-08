
# https://codeforces.com/problemset/problem/1894/B
from collections import Counter
test_case = int(input())

for test in range(test_case):
    n = int(input())
    n_arr = list(map(int,input().split()))
    freq = Counter(n_arr)
    ans = [num for num, count in freq.items() if count > 1]

    if len(ans) < 2:
        print("-1")
        continue

    for i in n_arr:
        if i == ans[0]:
            ans[0] = -1
            print("2", end=" ")
        elif i == ans[1]:
            ans[1] = -1
            print("3", end=" ")
        else:
            print("1", end=" ")
    print()





