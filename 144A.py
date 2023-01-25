
soldierLen = int(input())
totalSoldier = list(map(int,input().split()))
second = 0
""" firstInd = totalSoldier[0]
lastInd = totalSoldier[-1] """
maxVal = max(totalSoldier)
minVal = min(totalSoldier)

while totalSoldier[0] != maxVal or totalSoldier[-1] != minVal:
    for i in range(soldierLen - 1):
        if totalSoldier[i] < totalSoldier[i + 1]:
            totalSoldier[i], totalSoldier[i + 1] = totalSoldier[i + 1], totalSoldier[i]
            second += 1
print(second)
