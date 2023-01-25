
a,b = input().split()


for i in range(int(a)):
    for j in range(int(b)):
        if i % 2 != 0:
            if i % 4 == 0:
                j[0] = '#'
            else:
                j[j-1] = '#'
            print(".")
        else:
            print("#")
    print()
