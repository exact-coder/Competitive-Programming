

test_case = int(input())

while test_case:
    n = int(input())
    s = input()
    t = input()
    results = []
    
    f = 0
    for i in range(n):
        if s[i] == '.' or t[i] == '.':
            f = 1
    if not f:
        results.append(0)
        continue
    ans = 0
    cnt = [0] * (n + 2)
    c = 0
    for i in range(n):
        if s[i] == '.':
            c += 1
        if t[i] == '.':
            c += 1
        cnt[i] = c
    
    for i in range(1, n - 1):
        l = cnt[i - 1]
        r = cnt[n - 1] - l - 2
        if s[i] == '.' and t[i - 1] == 'x' and t[i + 1] == 'x' and l > 0 and r > 0 and t[i] == '.':
            ans += 1
        if t[i] == '.' and s[i - 1] == 'x' and s[i + 1] == 'x' and l > 0 and r > 0 and s[i] == '.':
            ans += 1
    
    results.append(ans)

    for result in results:
        print(result)

    test_case-=1


