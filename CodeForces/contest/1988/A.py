
# https://codeforces.com/contest/1988/problem/0

test_case = int(input())

while test_case:

    n,k = map(int,input().split())
    
    sequence = [n]
    output = 0
    
    while len(sequence) < n:
        current = sequence.pop()
        for i in range(min(k - 1, current - 1)):
            sequence.append(1)
        sequence.append(current - k + 1)
        output += 1
    
    print(output)

    test_case-=1


