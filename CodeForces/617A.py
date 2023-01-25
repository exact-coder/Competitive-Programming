

totalRoad = int(input())
mininmumMove = 0

if totalRoad % 5 == 0:
    x = totalRoad // 5
    mininmumMove = x
else:
    mininmumMove = totalRoad // 5
    mininmumMove += 1

print(mininmumMove)
