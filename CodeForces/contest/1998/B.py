

test_case = int(input())

while test_case:
    
    n = int(input())
    n_arr = list(map(int,input().split()))

    output = []

    output.append(' '.join(map(str, n_arr[1:] + [n_arr[0]])))

    print('\n'.join(output))

    test_case-=1





