""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/2008/D
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())

def dfs(v, i, used, s, curr):
    curr.append(i)
    if used[i]:
        return 0
    if s[i - 1] == '0':
        used[i] = True
        return 1 + dfs(v, v[i - 1], used, s, curr)
    else:
        used[i] = True
        return dfs(v, v[i - 1], used, s, curr)

while tc:
    n = int(input())
    v=list(map(int,input().split()))
    s=list(map(int,input().split()))

    index = 1
    results = []
    
    used = [False] * (n + 1)
    ans = [0] * (n + 1)
    
    
    for i in range(1, n + 1):
        if used[i]:
            continue
        
        curr = []
        x = dfs(v, i, used, s, curr)
        for a in curr:
            ans[a] = x
    
    results.append(" ".join(map(str, ans[1:n + 1])))
    index += 3

    print("\n".join(results))

    tc-=1







