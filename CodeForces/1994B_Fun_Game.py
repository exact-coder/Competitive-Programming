""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1994/B
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n = int(input())
    s = list(input())
    t = list(input())

    f = 0
    for i in range(n):
        if(s[i] == "1"): f = 1
        if(s[i] == "0" and t[i] == "1" and f==0):
            print("NO")
            break;
    else:
        print("YES")
    


    tc-=1



