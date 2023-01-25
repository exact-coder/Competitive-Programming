""" input
3
1 1 0
1 1 1
1 0 0
output
2
input
2
1 0 0
0 1 1
output
1
"""
problems = (input())
k = 0
for i in range(int(problems)):
    solution = list(map(int,input().split()))
    if sum(solution) >= 2:
        k += 1
print(k)







