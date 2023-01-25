

numArr = []
finalArr = []
inp = input()
for i in range(len(inp)):
    if (inp[i] != "+"):
        numArr.append(int(inp[i]))

sortArr = sorted(numArr)

for j in range(len(sortArr)):
    finalArr.append(str(sortArr[j]))
    
print("+".join(finalArr))


