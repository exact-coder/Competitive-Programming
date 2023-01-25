
guestName = input()
hostName = input()
shuffledName = input()
sortedName = sorted(guestName + hostName)
sortedShuffled = sorted(shuffledName)

if(sortedName == sortedShuffled):
    print("YES")
else:
    print("NO")
