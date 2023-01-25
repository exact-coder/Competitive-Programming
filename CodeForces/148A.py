
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
arr= []

for i in range(1,d+1):
    if i % k == 0:
        arr.append(i)
    elif i % l == 0:
        arr.append(i)
    elif i % m == 0:
        arr.append(i)
    elif i % n == 0:
        arr.append(i)

print(len(arr))


