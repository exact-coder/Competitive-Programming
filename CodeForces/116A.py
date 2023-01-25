

stops = int(input())

totalPassenger = []
lastEnter = 0

for i  in range(stops):
    enterExit = input().split()
    Enter = int(enterExit[1])
    existPassenger = lastEnter + Enter
    Exit = int(enterExit[0])
    expass = existPassenger - Exit
    totalPassenger.append(expass)
    lastEnter = expass


output = max(totalPassenger)

print(output)


""" 4
0 3
2 5
4 2
4 0 """
