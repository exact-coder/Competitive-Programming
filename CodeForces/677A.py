

totalFnd,requiredHeight = input().split()

allFndHeight = input().split()
width = 0

for i in range(int(totalFnd)):
    singleFnd = int(allFndHeight[i])
    if(singleFnd > int(requiredHeight)):
        width += 2
    elif(singleFnd <= int(requiredHeight)):
        width += 1
print(width)



