# https://codeforces.com/problemset/problem/1941/C

test_case = int(input())

while(test_case):

    string_len = int(input())
    ugly_str = input()
    beautiful_str_count = 0

    for i in range(string_len):
        
        if ugly_str[i:i+3] == "map":
            beautiful_str_count+=1
        elif ugly_str[i:i+3] == "pie":
            beautiful_str_count+=1
        if ugly_str[i:i+5]== "mapie":
            beautiful_str_count-=1
    print(beautiful_str_count)
        
    test_case-=1