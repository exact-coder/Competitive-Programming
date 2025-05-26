# https://codeforces.com/problemset/problem/1954/A

test_case= int(input())

while test_case:
    n_parts,m_alice,k_bob = map(int,input().split())

    if m_alice == 1:
        print("NO")
    else:
        seal_val = (n_parts+(m_alice-1))/(m_alice)
        print("Seal Value:",seal_val)
        seal_val=n_parts-seal_val
        if(k_bob>=seal_val):
            print("NO")
        else:
            print("YES")

    test_case-=1
# 11 5 2
# NO found
# YES expected