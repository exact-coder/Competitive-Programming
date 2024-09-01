

test_case = int(input())


while test_case:

    a = list(input())

    if len(a) >= 3:
        if a[0] == '1' and a[1] == '0' and (a[2] >= '2' or (len(a) >= 4 and a[2] >= '1')):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

    test_case-=1




