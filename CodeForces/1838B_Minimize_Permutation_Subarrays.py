""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1838/B
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:

    n = int(input())
    n_list = list(map(int,input().split()))

    for i in range(n):
        if n_list[i] == 1:
            a = i+1
        if n_list[i] == 2:
            b = i+1
        if n_list[i] == n:
            c = i+1
        
    if (c>b and b>a) or (a>b and b>c):
        print(b,c)
    elif (a>b and c>b and c>a) or (b>a and b>c and a>c):
        print(a,c)
    else:
        print(1,1)
    # print("A: ",a," B: ",b," C: ",c)
        

    test_case-=1

""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1838/B
Give Time to Time , It can hill everything.
*******************************"""

# test_case = int(input())

# while test_case:

#     n = int(input())
#     n_list = list(map(int,input().split()))

#     for i in range(n):
#         if n_list[i] == 1:
#             a = i
#         if n_list[i] == 2:
#             b = i
#         if n_list[i] == n:
#             c = i
        
#     if (a<c and c<b or b<c and c<a):
#         print(1,1)
#     elif a<b and b<c:
#         print(b+1,c+1)
#     elif b<a and a<c:
#         print(a+1,c+1)
#     elif c<a and a<b:
#         print(c+1,a+1)
#     elif c<b and b<a:
#         print(c+1,b+1)
#     # print("A: ",a," B: ",b," C: ",c)
        


#     test_case-=1