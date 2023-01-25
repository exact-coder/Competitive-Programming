
inputLen = int(input())
word = input()
antonLen = 0
dinakLen = 0

for i in range(inputLen):
    if(word[i] == "A"):
        antonLen += 1
    elif(word[i] == "D"):
        dinakLen += 1
if(antonLen == dinakLen):
    print("Friendship")
elif(antonLen > dinakLen):
    print("Anton")
elif(antonLen < dinakLen):
    print("Danik")
