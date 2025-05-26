""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/contests/2009/C
Give Time to Time , It can hill everything.
*******************************"""


test_case = int(input())


for i in range(test_case):

    x,y,k = map(int,input().split())

    A = (x+k-1)//k 
    B = (y+k-1)//k 

    if A <= B:print(2*B)
    else: print(2*A-1)


    test_case-=1


