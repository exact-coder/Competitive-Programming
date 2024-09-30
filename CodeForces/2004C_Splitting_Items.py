""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/2004/C
Give Time to Time , It can hill everything.
*******************************"""


tc = int(input())


while tc:
    n,k= map(int,input().split())
    n_l = list(map(int,input().split()))
    n_list = sorted(n_l)
    alice = 0
    bob = 0
    turn = 0
    
    for i in range(n - 1, -1, -1):
        if turn == 0:
            alice += n_list[i]
        else:
            extra = n_list[i + 1] - n_list[i] if i < n - 1 else 0
            if extra <= k:
                n_list[i] += extra
                k -= extra
            else:
                n_list[i] += k
                k = 0
            bob += n_list[i]
            
        turn ^= 1
    
    print(abs(alice - bob))
    

    tc-=1


