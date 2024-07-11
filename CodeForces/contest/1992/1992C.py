
test_case = int(input())

while test_case:
    n, m, k = map(int, input().split())
    
    per = [0] * n
    
    for i in range(n - m):
        per[i] = n - i
    
    for i in range(n - m, n):
        per[i] = i - (n - m) + 1
    
    print(" ".join(map(str, per)))
    
    test_case -= 1


