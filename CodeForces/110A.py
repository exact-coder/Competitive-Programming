

inputNum = input()
totalLuckyNumber = 0

for i  in range(len(inputNum)):
    singledigit = int(inputNum[i])

    if(singledigit == 4 or singledigit == 7):
        totalLuckyNumber += 1
    
if(totalLuckyNumber == 4 or totalLuckyNumber == 7):
    print("YES")
else:
    print("NO")
