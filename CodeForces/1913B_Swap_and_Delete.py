
# https://codeforces.com/problemset/problem/1913/B

test_case = int(input())

while test_case:

    s = input()
    one = 0
    zero = 0

    for i in s:
        if i == "1": one+=1
        if i == "0": zero+=1
    
    for j in s:
        if j == "1": 
            if zero>0:zero-=1
            else:break
        else:
            if one>0: one -=1
            else: break
    
    print(one+zero)


    test_case-=1

# 4
# 0
# 011
# 0101110001
# 111100