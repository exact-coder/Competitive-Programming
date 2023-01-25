
n = int(input())
volume =  list(input().split())
total = 0.0
for i in range(n):
    total += int(volume[i])

output = total / n
print("{:.12f}".format(output))
