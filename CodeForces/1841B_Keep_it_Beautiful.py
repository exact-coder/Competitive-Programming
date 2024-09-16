""" ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1841/B
Give Time to Time , It can hill everything.
*******************************"""

test_case = int(input())

while test_case:
    q = int(input())
    q_list = list(map(int,input().split()))
    output = []
    temp = []
    broken = False

    #  Function check list sorted or not
    def is_sorted(l):
        return all(a <= b for a, b in zip(l, l[1:]))

    for i in range(q):
        temp.append(q_list[i])
        if is_sorted(temp):
            output.append(1)
        else:
            if broken:
                if q_list[i] < temp[-2]:
                    output.append(0)
                    temp.pop()
                else:
                    if q_list[i] > q_list[0]:
                        output.append(0)
                        temp.pop()
                    else:
                        output.append(1)
            else:
                if q_list[i] <= q_list[0]:
                    output.append(1)
                    broken=True
                else:
                    temp.pop()
                    output.append(0)

    print("".join(map(str,output)))

    test_case-=1



