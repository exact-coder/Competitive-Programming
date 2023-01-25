

student,render = map(int, input().split())
studentinp = list(input())

for i in range(render):
    val = 1
    while val < student:
        if (studentinp[val -1 ] == "B" and studentinp[val] == "G"):
            studentinp[val -1], studentinp[val] = studentinp[val], studentinp[val -1]
            val += 1
        val+= 1

finalOutput = ''.join(studentinp)
print(finalOutput)


