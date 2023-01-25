
a = list(input())
b = list(input())
output = []

for i in range(len(a)):
    if(a[i] != b[i]):
        output.append("1")
    else:
        output.append("0")
print("".join(output))