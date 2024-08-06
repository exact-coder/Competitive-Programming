
test_case = int(input())

while test_case:
    a = list(input().strip())
    b = list(input().strip())
    
    j = 0
    n, m = len(a), len(b)
    
    for i in range(n):
        if j < m and (a[i] == b[j] or a[i] == '?'):
            a[i] = b[j]
            j += 1
    
    for i in range(n):
        if a[i] == '?':
            a[i] = 'a'
    
    if j == m:
        print("YES")
        print("".join(a))
    else:
        print("NO")

    test_case -= 1