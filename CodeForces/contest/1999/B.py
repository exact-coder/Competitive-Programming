

test_case = int(input())

while test_case:

    a1,a2,b1,b2 = map(int,input().split(" "))
    output = 0
    
    r_arr = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for i in r_arr:
        suneet = 0
        slavic = 0
        
        if i[0] > i[1]:
            suneet += 1
        elif i[0] < i[1]:
            slavic += 1
            
        if i[2] > i[3]:
            suneet += 1
        elif i[2] < i[3]:
            slavic += 1
        
        if suneet > slavic:
            output += 1
    print(output)

    test_case -=1

