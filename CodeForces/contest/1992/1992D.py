

test_case = int(input())
while test_case:
    casserole, i_piece, f_piece = map(int, input().split())
    monk = input()

    current_piece = i_piece - 1
    w_pieces = 0
    failed_operations = 0

    for i in monk:
        if i == 'L':
            current_piece = i_piece - 1
        elif i == 'W':
            if current_piece <= 0:
                w_pieces += 1
        else:
            if current_piece <= 0:
                failed_operations += 1
        current_piece -= 1

    if w_pieces > f_piece:
        failed_operations += 1

    print("NO" if failed_operations != 0 else "YES")

    test_case-=1


