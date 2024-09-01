

test_case = int(input())


while test_case:

    seats = int(input())
    seats_arr = list(map(int,input().split()))

    visited = [False] * (seats + 2) 

    is_valid = True
    
    for i in range(seats):
        visited[seats_arr[i]] = True
        if i > 0 and not visited[seats_arr[i] - 1] and not visited[seats_arr[i] + 1]:
            is_valid = False

    if is_valid:
        print("YES")
    else:
        print("NO")


    test_case-=1

