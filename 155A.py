
totalContest = int(input())
contestScoure = list(input().split())
output = 0


for j in range(totalContest-1):
    if int(contestScoure[j]) < int(contestScoure[j+1]):
        output +=1

if output == 0 and totalContest > 1:
    output +=1
print(output)

