

""" tanyaInput = input().split() # taking two input
totalSubtractNum = int(tanyaInput[1]) #how many time value decrease that making intiger
firstInp = tanyaInput[0] #Tanya's number

for i in range(totalSubtractNum):
    lastindex = firstInp[-1] # taking last index of the number
    firstInpInt = int(firstInp) #convert the number into intiger
    if(int(lastindex) > 0):
        firstInpInt -= 1
        firstInp = str(firstInpInt)
    elif(int(lastindex) == 0):
        res = firstInpInt // 10
        firstInp = str(res)

print(int(firstInp)) """

n,k = map(int,input().split())

for i in range(k):
    if(n % 10 == 0):
        n = n // 10
    else:
        n -= 1

print(n)



