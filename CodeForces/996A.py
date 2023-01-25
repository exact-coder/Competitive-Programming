
withdrawBlance = int(input())
dollarList = [100,20,10,5,1]
countNote = 0

while(withdrawBlance != 0):
    for i in range(len(dollarList)):
        checker = withdrawBlance >= dollarList[i]
        if(checker == True):
            withdraw = withdrawBlance // dollarList[i]
            withdrawBlance = withdrawBlance % dollarList[i]
            countNote += withdraw

print(countNote)
    