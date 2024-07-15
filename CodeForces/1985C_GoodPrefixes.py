
# https://codeforces.com/problemset/problem/1985/C

test_case = int(input())

while test_case:
    n = int(input())
    int_list = list(map(int,input().split()))
    max_item = -1e9
    sum_of_element = 0
    total_good_arr =0

    for i in range(n):
        sum_of_element+= int_list[i]
        max_item = max(max_item,int_list[i])
        if(sum_of_element-max_item == max_item):
            total_good_arr+=1
    print(total_good_arr)

    test_case-=1



