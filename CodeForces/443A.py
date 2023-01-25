
myInput = input().split(',')
finalOutput = []
for i in myInput:
    s = i.strip ()
    sc = s.strip ('{')
    scc = sc.strip ('}')
    if scc not in finalOutput:
        finalOutput.append(scc)
# print(finalOutput)
if(len(finalOutput) == 1 and finalOutput[0] == ''):
    print(0)
else:
    print(len(finalOutput))