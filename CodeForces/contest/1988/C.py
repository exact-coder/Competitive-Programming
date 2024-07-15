
test_case = int(input())


while test_case:

    n = int(input())

    sec_length = 0
    sec = []
    bit_positions = []

    for i in range(61):
        if n & (1 << i):
            sec_length += 1
            bit_positions.append(1 << i)
    sec_length += 1
    sec.append(n)

    for j in bit_positions:
        if n - j > 0:
            sec.append(n - j)
            
    sec.reverse()
    print(len(sec))
    print(*sec)

    test_case-=1




