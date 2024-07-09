
# https://codeforces.com/problemset/problem/1927/B



test_case = int(input())

while test_case:
    ls_length = int(input())

    ls = list(map(int,input().split()))

    output = ""

    count = [0] *26

    for i in ls:
        count_char = chr(count.index(i) + ord("a"))
        output += count_char
        count[count.index(i)] += 1
    print(output)
    test_case-=1

