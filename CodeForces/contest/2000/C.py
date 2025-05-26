

test_case = int(input())


while test_case:

    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):

        query = input()

        position_map = {}
        
        if len(query) != n:
            print("NO")
            continue

        visited = [False] * 27
        valid = True
        char_map = {}

        for i in range(n):
            char_index = ord(query[i]) - ord('a')
            
            if not visited[char_index]:
                if arr[i] in position_map:
                    valid = False
                    
                position_map[arr[i]] = True
                visited[char_index] = True
                char_map[char_index] = arr[i]
            
            valid &= (char_map[char_index] == arr[i])

        if valid:
            print("YES")
        else:
            print("NO")


    test_case-=1






