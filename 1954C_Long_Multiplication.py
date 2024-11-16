""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1954/C
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    x = list(input())
    y = list(input())

    check = 0

    for i in range(len(x)):
        a = int(x[i])
        b = int(y[i])

        if a == b:
            continue
        if check == 0:
            if a < b:
                x[i], y[i] = y[i], x[i]
            check = 1
        else:
            if a > b:
                x[i], y[i] = y[i], x[i]

    print(''.join(x))
    print(''.join(y))


    tc-=1







