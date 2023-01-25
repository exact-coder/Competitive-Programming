

allInput = input().split()

initialPriceOfBanana = int(allInput[0])
totalAmountSoldierHave = int(allInput[1])
howManyBananaWantsToBuy = int(allInput[2])
totalCost = 0

for i in range(1,howManyBananaWantsToBuy+ 1):
    bananaCost = initialPriceOfBanana * i
    totalCost += bananaCost
borrowMoney = totalCost - totalAmountSoldierHave
if(totalCost <= totalAmountSoldierHave):
    borrowMoney = 0
print(borrowMoney)
