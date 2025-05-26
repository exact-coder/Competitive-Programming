# https://codeforces.com/problemset/problem/1906/A


s = [input() for _ in range(3)]
# p =[(i, j) for i in range(3) for j in range(3)]
p = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
output = "ZZZ"
# print(s)
# print(p)
for a in p:
    for b in p:
        for c in p:
            if a != b and b != c and a != c and max(abs(a[0] - b[0]), abs(a[1] - b[1])) == 1 and max(abs(c[0] - b[0]), abs(c[1] - b[1])) == 1:
                t = s[a[0]][a[1]] + s[b[0]][b[1]] + s[c[0]][c[1]]
                output = min(output, t)

print(output)



