
gameLevel = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if gameLevel in x or gameLevel in y:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
