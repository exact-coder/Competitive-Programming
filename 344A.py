
totalMagnet = int(input())
magnetList = []
output = 0
for i in range(totalMagnet):
    singleMag = input()
    magnetList.append(singleMag)

for i in range(len(magnetList) - 1 ):
    firstMag = magnetList[i]
    nextMag = magnetList[i + 1]
    if(firstMag == nextMag):
        output += 1
    elif(firstMag != nextMag):
        pass
print(output)



""" Test: #1, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
6
10
10
10
01
10
10
Output
3
Answer
3
Checker Log
ok 1 number(s): "3"
Test: #2, time: 124 ms., memory: 4 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
4
01
01
10
10
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #3, time: 122 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
1
10
Output
1
Answer
1
Checker Log
ok 1 number(s): "1"
Test: #4, time: 124 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
2
01
10
Output
2
Answer
2
Checker Log
ok 1 number(s): "2"
Test: #5, time: 154 ms., memory: 0 KB, exit code: 0, checker exit code: 1, verdict: WRONG_ANSWER
Input
2
10
10
Output
2
Answer
1
Checker Log
wrong answer 1st numbers differ - expected: '1', found: '2' """
