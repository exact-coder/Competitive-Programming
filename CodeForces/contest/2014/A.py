""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/contest/2014/problem/A
Give Time to Time , It can hill everything.
*******************************"""



test_case = int(input())


while test_case:

    n,k = map(int,input().split())
    n_list = list(map(int,input().split()))

    output = 0
    gold = 0


    for i in range(n):
        if n_list[i] >=k:
            gold+=n_list[i]
        elif gold > 0 and n_list[i] == 0:
            gold-=1
            output+=1
    
    print(output)

    test_case-=1