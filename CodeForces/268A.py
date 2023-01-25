
totalGames = int(input())
matchingUniform = 0
firstUni = []
lastUni = []
for i in range(totalGames):
    uniform = list(input().split())
    firstUni.append(uniform[0])
    lastUni.append(uniform[1])

for j in range(totalGames):
    for k in range(len(lastUni)):
        if(firstUni[j] == lastUni[k]):
            matchingUniform += 1
print(matchingUniform)