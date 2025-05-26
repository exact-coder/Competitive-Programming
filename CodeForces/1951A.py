# https://codeforces.com/problemset/problem/1951/A

test_case = int(input())

while(test_case):
    n_lamp = int(input())
    bin_con = list(map(int,input()))
    on_lamp_index =[]

    for i in range(n_lamp):
        if bin_con[i] ==1:
            on_lamp_index.append(i)
    if(len(on_lamp_index) %2 != 0):
        print("NO")
    elif(len(on_lamp_index) == 2 and on_lamp_index[1] - on_lamp_index[0] ==1):
        print("NO")
    else:
        print("YES")


    test_case-=1