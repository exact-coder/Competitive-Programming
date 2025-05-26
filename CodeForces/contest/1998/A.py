

test_case = int(input())

while test_case:

    x,y,k = map(int,input().split())
    output = []

    for i in range(k // 2):
        output.append(f"{x - i - 1} {y}")
        output.append(f"{x + i + 1} {y}")
    if k % 2 == 1:
        output.append(f"{x} {y}")

    print("\n".join(output))

    test_case-=1


