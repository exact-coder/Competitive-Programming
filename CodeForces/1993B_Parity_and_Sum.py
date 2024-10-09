""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1993/B
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())

def func(even,odd):
    n1 = len(even)
    n2 = len(odd)
    mx = odd[-1]
    ans =0
    for i in range(n1):
        if even[i] > mx:
            return (n1 + 1)
        else:
            ans+=1
            mx += even[i]
    return ans


while tc:
    n = int(input())
    arr = list(map(int,input().split()))
    
    even =[]
    odd =[]

    for i in range(n):
        if arr[i] % 2:
            odd.append(arr[i])
        else:
            even.append(arr[i])

    if (len(even) ==0 or len(odd) ==0):
        print(0)
    else:
        even.sort()
        odd.sort()
        output = func(even,odd)
        print(output)

    tc-=1



