


allArr = []


for i in range(5):
    colInput = list(map(int,input().split()))
    allArr.append(colInput)

for j in range(len(allArr)):
    for k in range(len(allArr[j])):
        if allArr[j][k] == 1:
            print(abs(2-j) + abs(2-k))




