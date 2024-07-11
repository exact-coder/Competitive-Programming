
# https://codeforces.com/contest/1992/problem/0

test_case = int(input())

while test_case:
    a,b,c = map(int,input().split(" "))


    for i in range(5):
        if a<=b and a<=c:
            a+=1
        elif b<= a and b <=c:
            b+=1
        else:
            c+=1

    print(a*b*c)


    test_case-=1


