

totalRoom = int(input())
totalEmptyRoom = 0

for i in range(totalRoom):
    p,q = input().split()
    compare = int(q) - int(p)
    if(compare >=2):
        totalEmptyRoom += 1
print(totalEmptyRoom)
