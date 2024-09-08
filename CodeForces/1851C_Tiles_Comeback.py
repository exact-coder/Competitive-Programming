""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1851/C
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())


while test_case:

    n,k = map(int,input().split())
    n_arr = list(map(int,input().split()))
    count =0
    ck1 = 0
    ck2 = 0
    temp =0
    
    if n_arr[0] == n_arr[-1]:
        for i in range(n):
            if n_arr[i] == n_arr[0]:
                count+=1
                if count == k:
                    print("YES")
                    break
        else:
            print("NO")
    else:
        for i in range(n):
            if n_arr[i] == n_arr[0]:
                count+=1
                if count == k:
                    count=0
                    temp = i
                    ck1=1
                    break
        for j in range(temp,n,1):
            if n_arr[j] == n_arr[-1]:
                count+=1
                if count==k:
                    ck2 = 1
                    break
        if ck1 == 1 and ck2 == 1:
            print("YES")
        else:
            print("NO")


    test_case-=1