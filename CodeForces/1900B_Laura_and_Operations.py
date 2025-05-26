
# https://codeforces.com/problemset/problem/1900/B

test_case = int(input())

while test_case:

    a,b,c = map(int,input().split())
    one=0
    two =0
    three =0

    if(abs(b-c) %2 == 0):
        one=1

    if(abs(a-c) %2 == 0):
        two=1

    if(abs(a-b) %2 == 0):
        three=1

    print(one," ", two," ",three)

    test_case -=1

