
""" totalFunction = int(input())
positiveNum = 0
negativeNum = 0

for i in range(1,totalFunction+ 1):
    if(i % 2 == 0):
        positiveNum += i
    else:
        negativeNum += i

print(positiveNum - negativeNum) """

n = int(input())

if n % 2==0:
    ans = n//2
if n % 2==1:
    ans = ((n-1)//2)-n
    
print(ans)

