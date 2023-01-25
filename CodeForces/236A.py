
name = input()
setName = set(name)
makeStr = "".join(setName)
lenName = len(makeStr)

if(lenName % 2 == 0):
    print("CHAT WITH HER!")
elif(lenName % 2 == 1):
    print("IGNORE HIM!")
