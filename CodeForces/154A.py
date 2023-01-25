
""" 8 5
10 9 8 7 7 7 5 5 """



""" totalParticipant,minPassValue = input().split()

passParticipant = 0

totalparticipantScore = list(map(int,input().split()))

for i in range(int(totalParticipant)):
    if(totalparticipantScore[i] >= totalparticipantScore[int(minPassValue - 1)] and totalparticipantScore[i] != 0) :
        passParticipant += 1

print(passParticipant) """

n, k=input().split()

Adda=0
num = list(map(int, input().split()))
for i in range(int(n)):
    if num[i]>= num[int(k)-1] and num[i]!=0:
        Adda+=1

print(Adda)
