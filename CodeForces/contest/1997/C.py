

test_case = int(input())


while test_case:
    length = int(input())
    seq = list(input().strip())
    output = 0
    s = []

    for i in range(0, length, 2):
        if seq[i] == '_':
            if i == 0 or seq[i - 1] == ')':
                seq[i] = '('
            else:
                seq[i] = ')'

    for j in range(length):
        if seq[j] == '(':
            s.append(j)
        elif seq[j] == ')':
            if s:
                output += j-s.pop()
    print(output)


    test_case-=1









