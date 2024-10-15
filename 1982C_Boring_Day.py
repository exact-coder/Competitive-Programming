""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1982/C
Give Time to Time , It can hill everything.
*******************************"""




tc = int(input())


while tc:
    n,l,r = map(int,input().split())
    v = list(map(int,input().split()))
    
    
    i = 0
    j = 0
    sum_ = 0
    ans = 0
    
    while j != (n + 1):
        if l <= sum_ <= r:
            ans += 1
            sum_ = 0
            i = j
        elif sum_ < l:
            sum_ += v[j]
            j += 1
        else:
            sum_ -= v[i]
            i += 1
    
    print("ans : ",ans)

    tc-=1






