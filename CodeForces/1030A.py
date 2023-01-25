
totalPeople = int(input())

peopleResponse = input().split()
isHard = False

for i in range(totalPeople):
    if(int(peopleResponse[i]) == 1):
        isHard = True
        break
if(isHard):
    print("HARD")
else:
    print("EASY")
