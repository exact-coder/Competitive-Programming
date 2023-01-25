
totalTestCase = int(input())
for i in range(totalTestCase):
    a,b = map(int,input().split())
    if(a % b != 0):
        print(abs(b - a % b))
    else:
        print(0)

