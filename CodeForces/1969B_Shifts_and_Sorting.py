
# https://codeforces.com/problemset/problem/1969/B

test_case = int(input())

while test_case:
    bin_str = list(input())
    n = len(bin_str)
    current =0
    output_num = 0
    for i in range(n):
        if bin_str[i] == "1":
            current+=1
        elif current != 0:
            output_num+= current+1

    print(output_num)


    test_case-=1

