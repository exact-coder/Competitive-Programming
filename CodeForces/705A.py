
n = int(input())
arr = []
for i in range(n): 
    if i % 2 == 0:
        arr.append("I hate")
    else:
        arr.append("I love")
    if i >= 0 and n != 1 and i != n -1 :
        arr.append(" that ")
otuput = "".join(arr)

print(otuput + " it")