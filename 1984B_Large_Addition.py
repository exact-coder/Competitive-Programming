""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1984/B
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    num = input()

    if num[-1] == "9" or num[0] != '1':
        print("NO")
    else:
        check = 1
        for i in range(len(num)-1):
            if num[i] == "0":
                check=0
        if check: print("YES")
        else: print("NO")

    tc-=1




