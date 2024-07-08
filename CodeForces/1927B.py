
# https://codeforces.com/problemset/problem/1927/B

def lost_string(ls_length,ls):
    output = ""

    count = [0] *26

    for i in ls:
        count_char = chr(count.index(i) + ord("a"))
        output += count_char
        count[count.index(i)] += 1
    return output

test_case = int(input())

while test_case:
    ls_length = int(input())

    ls = list(map(int,input().split()))
    print(lost_string(ls_length,ls))
    test_case-=1

