
# https://codeforces.com/problemset/problem/1945/B

test_case = int(input())

while(test_case):
    a,b,m = map(int,input().split())

    total_fireworks= (m//a+1) + (m//b+1)
    print(total_fireworks)

    test_case-=1
