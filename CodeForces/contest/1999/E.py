import math

test_case = int(input())

while test_case:
    left, right = map(int, input().split())
    p = int(math.log2(left) / math.log2(3)) + 1
    output = 0
    output += (2 * p)
    
    while right > left:
        k = int(math.log2(right) / math.log2(3))
        max_p_of_3 = 3 ** k
        count = right - max(max_p_of_3, left + 1)
        output += ((k + 1) * (count + 1))
        right = max_p_of_3 - 1
    
    print(output)

    test_case-=1