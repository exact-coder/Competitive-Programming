""" ******************************
Username: Jahid_hasan_Akash
Problem: 1858C
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:

    n = int(input().strip())
    visited = [0] * (n + 1)
    print(1, end=" ")

    for i in range(2, n + 1):
        j = i
        if visited[j] != 1:
            while j <= n:
                print(j, end=" ")
                visited[j] = 1
                j *= 2
    print()

    test_case-=1


