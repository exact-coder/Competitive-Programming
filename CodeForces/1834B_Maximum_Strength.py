""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1834/B
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    
    l,r = input().split()
    
    cnt = len(r) - len(l)
    s = '0' * cnt + l
    s+=l

    indx =-1
    for i in range(len(r)):
        if s[i] != r[i]:
            indx=i
            break
    if indx == -1:
        print(0)
    else:
        length = len(r)-indx-1
        output = 9*length
        val = abs(int(r[indx])-int(s[indx]))
        output+=val
        print(output)

    tc-=1

