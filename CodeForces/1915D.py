
# https://codeforces.com/problemset/problem/1915/D

test_case = int(input())

while test_case:

    n = int(input())
    s = input()
    x = ""
    for i in range(n):
        if s[i] == 'a' or s[i] == 'e':
            x += 'V'
        else:
            x += 'C'
    
    for i in range(n-1, 0, -1):
        if i > 2 and x[i] == 'V' and x[i-1] == 'C':
            s = s[:i-1] + "." + s[i-1:]
            i -= 1
        if i > 3 and x[i] == 'C' and x[i-1] == 'V' and x[i-2] == 'C':
            if s[:i-2] + "." + s[i-2:] :
                s = s[:i-2] + s[i-2:]
            else:
                s = s[:i-2] + "." + s[i-2:]
            i -= 2
        
    
    print(s)

    test_case-=1

