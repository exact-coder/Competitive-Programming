""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1982/C
Give Time to Time , It can hill everything.
*******************************"""



tc = int(input())


while tc:
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    
    total = 0
    output = 0
    
    for i in range(n):
        total+=a[i]
        if a[i] > r:
            total =0
        elif a[i] >= l and a[i] <= r:
            output+=1
            total=0
        elif total >= l and total <= r:
            output+=1
            total=0
        
    print(output)

    tc-=1



