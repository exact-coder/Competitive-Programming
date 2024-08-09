
# https://codeforces.com/problemset/problem/1970/A1

s = input()
arr = []
val = 0

for i in range(len(s)):
  arr.append((val, -i, s[i]))
  if s[i] == '(':
    val += 1
  else:
    val -= 1

arr.sort()

print("".join(j[2] for j in arr))