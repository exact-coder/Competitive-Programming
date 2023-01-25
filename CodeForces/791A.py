

weight = list(input().split())
limakWeight = int(weight[0])
bobWeight = int(weight[1])
year = 0

for i in range(1,bobWeight+1):
    limakWeight *=3
    bobWeight *=2
    year += 1
    if(limakWeight > bobWeight):
        print(year)
        break




