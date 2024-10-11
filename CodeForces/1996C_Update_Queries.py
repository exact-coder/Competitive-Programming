""" ******************************
Username: JahidHasan90
Problem:  https://codeforces.com/problemset/problem/1986/C
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n,m = map(int,input().split())
    s_str = list(input())
    m_li = sorted(set(list(map(int,input().split()))))
    c_str = sorted(input())

    inx =0
    for i in m_li:
        s_str[i-1] = c_str[inx]
        inx+=1

    print("".join(map(str,s_str)))

    tc-=1




