# https://codeforces.com/problemset/problem/1971/C


test_case = int(input())

while(test_case):
    a,b,c,d= map(int,input().split())

    max_val =max(a,b)
    min_val = min(a,b)

    checker = 0

    for i in range(min_val,max_val):
        if(c == i):
            checker+=1
        if(d == i):
            checker+=1
    
    if(checker == 1):
        print("YES")
    else:
        print("NO")

    test_case-=1