
n = int(input())
mainInp = list(input())
k = 0

for i in range(n-1):
    if(mainInp[i] == mainInp[i+1]):
        k += 1
print(k)
